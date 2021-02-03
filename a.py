from flask import Flask,redirect,url_for,render_template,request
from selenium import webdriver
from bs4 import BeautifulSoup
import os,random,sys,time
from urllib.parse import urlparse
import requests
import pickle
import pandas as pd
import re

app=Flask(__name__)

@app.route("/")
def home():
	return render_template("index2.html")

@app.route("/login",methods=['POST','GET'])
def login():
	if request.method =="POST":
		user= request.form["nm"]
		return redirect(url_for("user",usr=user))
	else:	
	    return render_template("login.html")
    #link=request.form.get('nm')
@app.route("/<path:usr>")
def user(usr):

    link=usr
    browser=webdriver.Chrome('chromedriver.exe')
    browser.get('https://www.linkedin.com/uas/login')
    file=open('config.txt')
    lines=file.readlines()
    username=lines[0]
    password=lines[1]
    elementID=browser.find_element_by_id('username')
    elementID.send_keys(username)
    elementID=browser.find_element_by_id('password')
    elementID.send_keys(password)
    elementID.submit()
    #link='https://www.linkedin.com/in/bijosh-t-27670826/'
    browser.get(link)
    SCROLL_PAUSE_TIME=5
    last_height=browser.execute_script('return document.body.scrollHeight')
    for i in range(3):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height=browser.execute_script('return document.body.scrollHeight')
        if new_height==last_height:
            break
        last_height=new_height
    src=browser.page_source
    soup = BeautifulSoup(browser.page_source, 'lxml')
    name_div=soup.find('div',{'class':'flex-1 mr5'})
    name_loc=name_div.find_all('ul')
    name=name_loc[0].find('li').get_text().strip()
    exp_section=soup.find('section',{'id':'experience-section'})
    exper=exp_section.find_all('div',{'class':"pv-entity__summary-info pv-entity__summary-info--background-section"})
    title=[]
    company=[]
    tenure=[]
    for job_elem in exper:
        title.append(job_elem.find('h3').get_text().strip())
        company.append(job_elem.find_all('p')[1].get_text().strip())
        tenure.append(job_elem.find_all('span')[3].get_text().strip())

    df = pd.DataFrame(
        {
          'Title': title,
          'Company': company,
          'Tenure': tenure
        })
    idx=0
    df.insert(loc=idx, column='Name', value=name)
    df['Tenure'] = df['Tenure'].astype(str)

    def Avg_tenure(y):
        y = str(y)
        l=re.findall(r'\d+', y)
        d=(int(l[0])*12)+int(l[1])
        return d

    df['Avg_Tenure']=df['Tenure'].apply(lambda x:Avg_tenure(x))
    df['Avg_Tenure']=df["Avg_Tenure"].mean()//12
    result= df['Avg_Tenure'][0]
    return 'The Average Tenure is: ' + str(result)
	

if __name__=="__main__":
	app.run(debug=True)



