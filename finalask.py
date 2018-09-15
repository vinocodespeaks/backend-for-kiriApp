from bin_questions import BinQuestion
from binary import Binary
from wh_question import WH
from tokenize import Tokenize
import sys
import pdftotext as pdf
data=""

class Ask:
    

    def main(self, k,article):
        
        print("\n\n\n\n")
        binary_questions = []
        print ("Check Point 0")
        #f=open(article,"r")
        #data=f.read()
        data=article
        T = Tokenize.main(k,article)
        sentences_top_k = T[0]
        NE = T[1]
        # print(sentences_top_k)
        questions = []
        for si in sentences_top_k:
            print("	*** org  : ", si)
            # print(" *** original sentence: ", si)
            bin_attempt = Binary.main(si)
            wh_attempt = WH.main(bin_attempt, si, NE)
            if bin_attempt:
                print("	*** bin : ", bin_attempt)
                questions.append(bin_attempt)
            if wh_attempt:
                for i in wh_attempt:
                    questions.append(i)
            print("\n")
        print("\n\n\n\n")
        return questions
        # print "------------INPUT TEXT ---------","\n"
        # print data
        # print "-----------------------------------","\n"
        # print "----------POSSIBLE QUESTIONS--------","\n"
        # #print questions,"main questions"
        # j=1
        # for i in questions:
        #     print  j,'.',i,'\n'
        #     j=j+1
        
def response(text,id):
    Tokenize = Tokenize()
    BinQuestion = BinQuestion()
    Binary = Binary()
    WH = WH()
    run = Ask()
    run.main(id,text)
    print "------------INPUT TEXT ---------","\n"
    
    print "-----------------------------------","\n"
    print "----------POSSIBLE QUESTIONS--------","\n"
    #print questions,"main questions"
    j=1
    for i in questions:
        print  j,'.',i,'\n'
        j=j+1


if __name__ == '__main__':
    Tokenize = Tokenize()
    BinQuestion = BinQuestion()
    Binary = Binary()
    WH = WH()
    run = Ask()

   # pdf.getPDFContent("sample.pdf").encode("ascii", "ignore")
    #with open('sample.txt', 'w+') as the_file:
     #   the_file.write(pdf.getPDFContent("sample.pdf").encode("ascii", "ignore"))
    questions=run.main(4,str(sys.argv[1]))
    
    print "------------INPUT TEXT ---------","\n"
    # f=open("einstein.txt","r")
    # data=f.read()
    data=sys.argv[1]
    print data
    print "-----------------------------------","\n"
    print "----------POSSIBLE QUESTIONS--------","\n"
    # #print questions,"main questions"
    # j=1
    # print "-------------------------------------\n"
    # pfile= open("qustions1.txt",'w+')
    # pfile.seek(0)
    # pfile.truncate()
    # for i in questions:
    #     print  j,'.',i,'\n'
    #     f.write(i+"\n")
    #     j=j+1
    print_question=open("question1.txt",'w+');
    print_question.seek(0)
    print_question.truncate()
    for i in questions:
        print_question.write(i+"\n")

