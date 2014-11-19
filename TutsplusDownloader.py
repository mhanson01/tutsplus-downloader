#! /usr/bin/env python
#-*- coding: utf-8 -*-
 
import urllib
import urllib2
import re
import os
from cookielib import CookieJar
from bs4 import BeautifulSoup
 
class Tutsplus:
 
    login_url= 'https://tutsplus.com/sign_in'
    login_post = 'https://tutsplus.com/sessions'
    home_url = 'https://tutsplus.com'
 
    def __init__(self, config):
 
        cj = CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
 
        self.username = config['username']
        self.password = config['password']
 
        self.login()
        self.download_courses(config['courses'])
 
    # Return the html source for a specified url
    def get_source(self, url, data=None):
 
        src = self.opener.open(url)
        return src.read()
 
    # Return the soup for a specified html
    def get_soup(self, url, data=None):
 
        source = self.get_source(url, data)
        return BeautifulSoup(source)
 
    # It logs in and store the sesson for the future requests
    def login(self):
 
        soup = self.get_soup(self.login_url)
        token = soup.find(attrs={"name":"authenticity_token"})
 
        data = {
            "session[login]":self.username,
            "session[password]":self.password,
            "authenticity_token": soup.find(attrs={"name":"authenticity_token"})['value'],
            "utf8":"✓"
        }
 
        postdata = urllib.urlencode(data)
 
        self.opener.open(self.login_post, postdata)
 
        return True
 
    # Download all video from a course url
    def download_course(self, url):
 
        # Variable needed to increment the video number
        self.video_number = 1
 
        soup = self.get_soup(url)
 
        # the course's name
        self.course_title = soup.select('h1')[0].string
        if not os.path.exists("courses/" + self.course_title) :
            os.makedirs("courses/" + self.course_title)
 
        self.csrf_token = soup.find(attrs={"name":"csrf-token"})['content']
 
        # array who stores the information about a course
        course_info = self.get_info_from_course(soup)
 
        for video in course_info:
            print video['link']
            print "[+] Downloading " + video['titolo']
            name = self.course_title + '/[' + str(self.video_number).zfill(2) + '] ' + video['titolo']
            self.download_file(video['link'], name, self.csrf_token)
            self.video_number = self.video_number + 1
 
 
    def download_courses(self,courses):
 
        for course in courses:
 
            self.download_course(course)
 
    # pass in the info of the lesson and it will download the video
    # lesson = {
    #   "titolo": 'video title',
    #   "link" : 'http://link_to_download'
    # }
 
    # Function who downloads the file itself
    def download_file(self,url, name, token):
        # name = url.split('/')[-1]
        # NOTE the stream=True parameter
        name = name + '.mp4'
 
        data = {
            "authenticity_token": token
        }
        postdata = urllib.urlencode(data)
        vid = self.opener.open(url, postdata)
 
        if not os.path.isfile("courses/" + name) :
            with open("courses/" + name, 'wb') as f:
                f.write(vid.read())
        return name
 
    # return an array with all the information about a video (title, url)
    def get_info_from_course(self, soup):
        arr = []
        videos = soup.select('.lesson-index__lesson')
 
        for video in videos:
 
            titolo = video.select('.lesson-index__lesson-title')[0].string
            link = video.select('a')[0]['href']
 
            info = {
                "titolo":titolo,
                "link":link
            }
            arr.append(info)
 
        return arr
