# -*- coding: utf-8 -*-
import sys
import os
import shutil
from subprocess import Popen, PIPE

VC_HOME=r'D:\data\pycharm\fdu_assist_2015q1_cpp\VC98'


SRC_HOME1=r'D:\tmp\fdu_assist_2015q1_cpp\homeworks\第八次作业'
SRC_HOME=SRC_HOME1
DEST_HOME=SRC_HOME+'copy'

def extractAll():   #解压zip,rar文件
    for dpath,dnames,fnames in os.walk(SRC_HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.rar'):
                proc =Popen(['C:/Program Files/winrar/rar','x','-y',fpath,dpath])
                out, err = proc.communicate()
            if fname.lower().endswith('.zip'):
                proc = Popen(['C:/Program Files/7-zip/7z','x',fpath,'-y','-o'+dpath])
                out, err = proc.communicate()


def compileAll():   #编译c/c++文件
    env = dict(os.environ)
    env["INCLUDE"] = VC_HOME+'\Include;'
    env['LIB']=VC_HOME+'\Lib;'
    k=0
    for dpath,dnames,fnames in os.walk(SRC_HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.c'):
                fn=fname[:-2]
                canCompile=True
            elif fname.lower().endswith('.cpp'):
                fn=fname[:-4]
                canCompile=True
            else:
                canCompile=False

            if canCompile:
                proc=Popen([VC_HOME+r'\BIN\CL',fpath,'/Fo'+dpath+'/','/Fe'+dpath+'/'],env=env)
                out, err = proc.communicate()


def copyAllToNewDir():
    for dname in os.listdir(SRC_HOME):  #dname should like '$stuName($stuNo)'
        dpath1=os.path.join(SRC_HOME,dname)
        dpath2=os.path.join(DEST_HOME,dname)
        os.makedirs(dpath2, exist_ok=True)
        for dpath,dnames,fnames in os.walk(dpath1):
            num_cpp=0
            for fname in fnames:
                shutil.copy(os.path.join(dpath,fname),os.path.join(dpath2,fname))
                if fname.lower().endswith('.c') or fname.lower().endswith('.cpp'):
                    num_cpp+=1
            print(num_cpp,'\t',dpath)



extractAll()
compileAll()
copyAllToNewDir()