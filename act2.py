# -*- coding: utf-8 -*-
import sys
import os
import shutil
from subprocess import Popen, PIPE
SRC_HOME= 'D:\\tmp\\fdu_assist_2015q1_cpp\\MidExam\\期中大作业03班'
VC_HOME=r'D:\data\pycharm\fdu_assist_2015q1_cpp\VC98'
DEST_HOME='D:\\tmp\\fdu_assist_2015q1_cpp\\MidExam\\期中大作业03班ES'
def extractAll():   #解压zip,rar文件
    for dpath,dnames,fnames in os.walk(SRC_HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.rar'):
                #(cmd_extract_rar(fpath,dpath))
                proc =Popen(['C:/Program Files/winrar/rar','x','-y',fpath,dpath],stdout=PIPE)
                out, err = [x.decode(sys.stdout.encoding) for x in proc.communicate()]
            if fname.lower().endswith('.zip') and False:
                ps = Popen(['C:/Program Files/7-zip/7z','x',fpath,'-y','-o'+dpath])
                ps.wait()


def compileAll():   #编译c/c++文件

    proc=Popen(['D:\\data\\pycharm\\prepare.bat'])
    out, err = proc.communicate()
    proc=Popen([VC_HOME+'\BIN\CL'])
    out, err = proc.communicate()
    env = dict(os.environ)
    env["INCLUDE"] = VC_HOME+'\Include;'
    env['LIB']=VC_HOME+'\Lib;'
    k=0
    for dpath,dnames,fnames in os.walk(SRC_HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)

            if fname.lower().endswith('.c') or fname.lower().endswith('.cpp'):
                x=-4
                if fname.lower().endswith('.c'):
                    x=-2
                fpath2=fpath[:x]+'.exe'
                #Popen('@echo ------------->',k);k+=1;
                proc=Popen([VC_HOME+r'\BIN\CL',fpath,"/Fe"+dpath+'/'],env=env,cwd="genexes")
                out, err = proc.communicate()


def copyExesAndClassifyAll():
    for dname in os.listdir(SRC_HOME):  #dname should like '$stuName($stuNo)'
        dpath1=os.path.join(SRC_HOME,dname)
        dpath2=os.path.join(DEST_HOME,dname)
        os.makedirs(dpath2, exist_ok=True)
        for dpath,dnames,fnames in os.walk(dpath1):
            for fname in fnames:
                shutil.copy(os.path.join(dpath,fname),os.path.join(dpath2,fname))


#compileAll()
#extractAll()
copyExesAndClassifyAll()