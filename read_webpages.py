# -*- coding: utf-8 -*-

"""
Created on Sat Jan 26 12:16:17 2019

@author: Thomas
"""

import os
import sys
import re
import urllib.request
import pdb
import pickle

class topic:
    def __init__(self,title,summary,TOC):
        self.title=title
        self.summary=summary
        self.TOC=TOC
    
    def get_high_level_topics():
        return [el[0] for el in self.TOC if el[1]==0]
    
    
    

def load_list_of_topic_urls():
    topic_url_list=[]
    with urllib.request.urlopen('https://www.gartner.com/en/research/magic-quadrant') as response:
        html = response.read()
        html=html.split(b'\n')
        html=[el.decode('utf-8') for el in html]
    #match where the url template matches"
    r=re.compile('https://www.gartner.com/doc/code/\d*') #searches and finds the domain
    
    for line in html:
        m=re.search(r,line)
        if m is not None:
            #take the rest of the line ie line[m.span()[1]:]
            url=line[m.span()[0]:m.span()[1]]
            lastpart=line[m.span()[1]:]
            title=lastpart[2:-15]
            topic_url_list.append([title,url])
    return topic_url_list

def load_topic(title,url):
    TOC_start=None
    TOC_end=None
    TOC=[]
    summary=None
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html=html.split(b'\n')
        html=[el.decode('utf-8') for el in html]
    summary_match=re.compile('<meta name="description" content=')
    start_TOC_match=re.compile('<h2>Table of Contents</h2>')
    end_TOC_match=re.compile('Gartner Recommended Reading')
    count=0
    for line in html:
        m1=re.match(summary_match,line)
        m2=re.match(start_TOC_match,line)
        m3=re.match(end_TOC_match,line)
        
        if m1 is not None and summary is None:
            summary=line[m1.span()[1]:]
            summary=summary[1:-4]
        if m2 is not None and TOC_start is None:
            TOC_start=count
        if m3 is not None and TOC_end is None:
            TOC_end=count
        count=count+1
    TOC=html[TOC_start+2:TOC_end]    
    TOC=[line for line in TOC if line not in ['<li>','</li>']]
    assigned_TOC=[]
    level=0
    for ii in range(len(TOC)):
        if TOC[ii]=='<ul>':
            level=level+1
        if TOC[ii]=='</ul>':
            level=level-1
        if TOC[ii] not in ['<ul>','</ul>']:
            assigned_TOC.append([TOC[ii],level])        
    return title,summary,assigned_TOC
    
def create_topic_list():
    tl=[]
    a=load_list_of_topic_urls()
    count=0
    for el in a:
        title=el[0]
        url=el[1]
        try:
            title,summary,assigned_TOC=load_topic(title,url)
            tl.append(topic(title,summary,assigned_TOC))
        except:
            pass
        counst=count+1
    return tl
        

def load_topic_list():
    with open('topic_pickle.txt','rb') as f:
        tl=pickle.load(f)
        f.close()
    return tl

def topic_string(t):
    print(t.title)
    fixsummary=t.summary.replace('"','\'')
    fixTOC=str(t.TOC).replace('"','\'')
    ts='''
    "title":"{}",
    "summary":"{}",
    "TOC":"{}"
    '''.format(t.title,fixsummary,fixTOC)
    return ts

def write_data_file():
    tl=load_topic_list()
    lines=[]
    with open('data_template.txt','r') as f:
        while True:
            l=f.readline()
            if l=='':
                break
            lines.append(l)
        f.close()
    write_flag_match=re.compile('%writehere%')
    whichline=None
    for ii in range(len(lines)):
        if re.match(write_flag_match,lines[ii]) is not None:
            whichline=ii
    with open('data.py','w') as f:
        for ii in range(0,whichline):
            f.write(lines[ii])
        for ii in range(len(tl)):
            f.write('{\n')
            f.write(topic_string(tl[ii]))
            f.write('},\n')
        for ii in range(whichline+1,(len(lines))):
            f.write(lines[ii])
        f.close()
            
