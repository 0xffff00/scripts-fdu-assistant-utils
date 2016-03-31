# -*- coding: utf-8 -*-
import sys
import os
import shutil
import subprocess
from subprocess import Popen, PIPE

VC_HOME=r'D:\data\pycharm\fdu_assist_2015q1_cpp\VC98'
SRC_HOME1=r'D:\tmp\fdu_assist_2015q1_cpp\homeworks\第一次作业'
SRC_HOME=SRC_HOME1
DEST_HOME=SRC_HOME+'copy'
ANS_PATH=r'h1ans1.txt'
DEF_SIZEOUT=500    #BYTES
DEF_TIMEOUT=1       #SECONDS
def markAnswer(filePath, textIn,outFile,caseNo=0, timeout=DEF_TIMEOUT):
    outFile.write('\n<---- Case %d ---->\n' %(caseNo))
    proc=Popen(filePath, stdin=PIPE, stdout=PIPE, universal_newlines=True)

    try:
        outs, errs = proc.communicate(textIn, timeout=timeout)
        if len(outs)>DEF_SIZEOUT:
            outFile.write('[JUDGER-ERROR] Output Limit Exceeded (len=%s) !!!'%(len(outs)))
        else:
            outFile.write(outs)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        outFile.write('[JUDGER-ERROR] Time Limit Exceeded!!!')
    except Exception:
        outFile.write('[JUDGER-ERROR] Runtime Error!!!')
    outFile.flush()


    print('markAnswer complete: %s [CASE %d]'%(filePath,caseNo))

def judge(probNo,ansfilepath):
    ansf=open(ansfilepath,'w')
    ansf.write('\n******************************************************************************************************\n')
    ansf.write('Answers from Problem %d Auto Judgement Result\n'%(probNo))
    ansf.write('******************************************************************************************************\n\n')
    cntMark=0
    for dpath,dnames,fnames in os.walk(DEST_HOME):
        for fname in fnames:
            fpath=os.path.join(dpath,fname)
            if fname.lower().endswith('.exe'):
                if fname[:-4].endswith((str(probNo))):

                    ansf.write('\n\n######## '+fpath+' ########\n')
                    ansf.flush()
                    if probNo==1:

                        markAnswer(fpath,'j',ansf,1)
                        markAnswer(fpath,'A',ansf,2)


                    elif probNo==2:
                        markAnswer(fpath,'3 4 5',ansf,1)
                        markAnswer(fpath,'8 8 5',ansf,2)
                        markAnswer(fpath,'2 30 11',ansf,3)

                    elif probNo==3:
                        markAnswer(fpath,'59',ansf,1)
                        markAnswer(fpath,'98',ansf,2)
                        markAnswer(fpath,'76',ansf,3)
                    elif probNo==4:
                        markAnswer(fpath,'59',ansf,1)
                        markAnswer(fpath,'98',ansf,2)
                        markAnswer(fpath,'76',ansf,3)
                    elif probNo==5:
                        markAnswer(fpath,'3200',ansf,1)
                        markAnswer(fpath,'4350',ansf,2)
                        markAnswer(fpath,'7643',ansf,3)

    ansf.close()



#judge(1,'h1p1.txt')
#judge(2,'h1p2.txt')
#judge(3,'h1p3.txt')
#judge(4,'h1p4.txt')
judge(5,'h1p5.txt')