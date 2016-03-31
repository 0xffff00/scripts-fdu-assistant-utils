# -*- coding: utf-8 -*-
import sys
import os
import shutil
import subprocess
from subprocess import Popen, PIPE

VC_HOME=r'D:\data\pycharm\fdu_assist_2015q1_cpp\VC98'
SRC_HOME1=r'D:\tmp\fdu_assist_2015q1_cpp\FinalExam\D1'
SRC_HOME=SRC_HOME1
DEST_HOME=SRC_HOME+'copy'
ANS_PATH=r'h1ans1.txt'
DEF_SIZEOUT=500    #BYTES
DEF_TIMEOUT=2       #SECONDS
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
                    if probNo==21:


                        markAnswer(fpath,'8',ansf,1)
                        markAnswer(fpath,'9',ansf,2)
                        markAnswer(fpath,'90',ansf,3)
                        markAnswer(fpath,'720',ansf,4)
                        markAnswer(fpath,'2450',ansf,5)

                    elif probNo==22:
                        markAnswer(fpath,'hello world',ansf,1)
                        markAnswer(fpath,'show me the money',ansf,2)
                        markAnswer(fpath,'there is no cow level',ansf,3)
                        markAnswer(fpath,'operation cwal',ansf,4)
                        markAnswer(fpath,'how dou you turn this back to the flat fox',ansf,5)



    ansf.close()


judge(21,'f0p21.txt')
judge(22,'f0p22.txt')
