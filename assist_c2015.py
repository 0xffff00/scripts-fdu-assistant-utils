import sys
import os
import subprocess
HOME='D:\\tmp\\fdu_assist_2015q1_cpp\\MidExam\\期中大作业03班'
def cmd_extract_7z(file,out):
    return '\"C:/Program Files/7-zip/7z\" x \"%s\" -y -o\"%s\"' %(file,out)
def cmd_extract_rar(file,out):
    return '\"C:/Program Files/winrar/rar\" x -y \"%s\" \"%s\"' %(file,out)
def cmd_cl(file,out):
    return

def extractAll():
    for dpath,dnames,fnames in os.walk(HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.rar'):
                print(cmd_extract_rar(fpath,dpath))
                ps = subprocess.Popen(cmd_extract_rar(fpath,dpath))
                ps.wait()
            if fname.lower().endswith('.zip'):
                ps = subprocess.Popen(cmd_extract_7z(fpath,dpath))
                ps.wait()


def compileAll():
    for dpath,dnames,fnames in os.walk(HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.c') or fname.lower().endswith('.cpp'):

                ps = subprocess.Popen(cmd_extract_rar(fpath,dpath))
                ps.wait()
            if :
                ps = subprocess.Popen(cmd_extract_7z(fpath,dpath))
                ps.wait()