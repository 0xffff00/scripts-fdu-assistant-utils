# -*- coding: utf-8 -*-
import sys
import os
from subprocess import Popen, PIPE
HOME='D:\\tmp\\fdu_assist_2015q1_cpp\\MidExam\\期中大作业03班'
CMD1=r'SET INCLUDE=C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\atlmfc\include;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\Include;'
CMD2=r'SET LIB=C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\lib;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\atlmfc\lib;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\Lib;'

def cmd_extract_7z(file,out):
    return '\"C:/Program Files/7-zip/7z\" x "%s" -y -o"%s"' %(file,out)
def cmd_extract_rar(file,out):
    return '\"C:/Program Files/winrar/rar\" x -y "%s" "%s"' %(file,out)
def cmd_cl(file,out):
    return 'cl "%s" /Fo"%s"' %(file,out)
    #return '"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\cl" "%s" /Fo"%s"' %(file,out)
def extractAll():   #解压zip,rar文件
    for dpath,dnames,fnames in os.walk(HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.rar'):
                #(cmd_extract_rar(fpath,dpath))
                proc =Popen(['C:/Program Files/winrar/rar','x','-y',fpath,dpath],stdout=PIPE)
                out, err = [x.decode(sys.stdout.encoding) for x in proc.communicate()]
            if fname.lower().endswith('.zip') and False:
                ps = Popen(cmd_extract_7z(fpath,dpath))
                ps.wait()


def compileAll():   #编译c/c++文件

    proc=Popen(['D:\\data\\pycharm\\prepare.bat'])
    out, err = proc.communicate()
    proc=Popen(['C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/CL'])
    out, err = proc.communicate()
    env = dict(os.environ)
    env["INCLUDE"] = r'C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\atlmfc\include;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\Include;'
    env['LIB']=r'C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\lib;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\atlmfc\lib;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\Lib;'
    for dpath,dnames,fnames in os.walk(HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)

            if fname.lower().endswith('.c') or fname.lower().endswith('.cpp'):
                x=-4
                if fname.lower().endswith('.c'):
                    x=-2
                fpath2=fpath[:x]+'.exe'
                s=cmd_cl(fpath,fpath2)
                print(s)
                Popen(['C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/CL',fpath,"/Fo"+fpath2],env=env)




compileAll()
#extractAll()