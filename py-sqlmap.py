#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:http://lanpang999.top/

import os
from burp import IBurpExtender

# 导入 Java 库
from javax.swing import JPanel
from javax.swing import JButton

from java.util import ArrayList
#!/usr/bin/env python        
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

import re

from burp import IHttpListener
from java.io import PrintWriter
from burp import IContextMenuFactory
from javax.swing import JMenu
from javax.swing import JMenuItem
import hashlib
import urllib
import json
import time

currentTime = time.strftime('%Y%m%d%H%M%S',time.localtime())



class BurpExtender(IBurpExtender, IHttpListener,IContextMenuFactory):

# Burp Suite使用这个接口将一组回调方法传递给扩展，扩展可以使用这些回调方法执行Burp中的各种操作。
    def registerExtenderCallbacks(self, callbacks):

        self._cb = callbacks
        self._helpers = callbacks.getHelpers()
        self._hp = callbacks.getHelpers()

        callbacks.setExtensionName("sqlmap")
        callbacks.registerHttpListener(self)
        callbacks.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callbacks.getStdout(), True)
        self.stderr = PrintWriter(callbacks.getStderr(), True)
        callbacks.issueAlert("Loaded Successfull.")


    def createMenuItems(self, invocation):
        self.menus = []
        self.mainMenu = JMenu("sqlmap")
        self.menus.append(self.mainMenu)
        self.invocation = invocation

        menuItem = ['sqlmap-get','sqlmap-post','sqlmap-level5']
        for tool in menuItem:
            #self.mainMenu.add(JMenuItem(tool))
            if tool == 'sqlmap-get':
                menu = JMenuItem(tool,None,actionPerformed=lambda x:self.sqlmap_type(x))
                self.mainMenu.add(menu)
            elif tool == 'sqlmap-post':
                menu = JMenuItem(tool,None,actionPerformed=lambda x:self.sqlmap_type(x)) 
                self.mainMenu.add(menu)
            elif tool == 'sqlmap-level5':
                menu = JMenuItem(tool,None,actionPerformed=lambda x:self.sqlmap_type(x)) 
                self.mainMenu.add(menu)
    
        return self.menus if self.menus else None


    def sqlmap_type(self,x):
        
        currentRequest = self.invocation.getSelectedMessages()[0]  #getSelectedMessages()返回数组，但有时为1个，有时2个
        requestInfo = self._helpers.analyzeRequest(currentRequest) # 该部分实际获取到的是全部的Http请求包
        url = str(requestInfo.getUrl())
        
        if x.getSource().text == 'sqlmap-get': #通过获取当前点击的子菜单的 text 属性，确定当前需要执行的 command
            exe = "start cmd /k python2 sqlmap.py -u "+url+" --batch --random-agent --beep"
            print '\n'+currentTime+'\n'+exe
            os.system(exe)

        elif x.getSource().text == 'sqlmap-post': 
            self.headers = list(requestInfo.getHeaders())
            bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():] # bytes[]类型
            self.body = self._helpers.bytesToString(bodyBytes) #bytes to string转换一下
            
            f = open('text1.txt','w')
            for x in self.headers:
                f.write(x+'\n')
            f.write('\n'+self.body)
            f.close()
            exe = "start cmd /k python2 sqlmap.py -r text1.txt --level 2 --batch --random-agent --beep"
            print '\n'+currentTime+'\n'+exe
            os.system(exe)

        elif x.getSource().text == 'sqlmap-level5': 
            self.headers = list(requestInfo.getHeaders())
            bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():] # bytes[]类型
            self.body = self._helpers.bytesToString(bodyBytes) #bytes to string转换一下
            
            f = open('text1.txt','w')
            for x in self.headers:
                f.write(x+'\n')
            f.write('\n'+self.body)
            f.close()
            exe = "start cmd /k python2 sqlmap.py -r text1.txt --level 5 --batch --random-agent --beep"
            print '\n'+currentTime+'\n'+exe
            os.system(exe)


    def getTabCaption(self):
        # 实现 ITab 接口的 getTabCaption() 方法
        return 'TestPlugin'

    def getUiComponent(self):
        # 获取面板内容
        return self.mainPanel

