import numpy

dataDir='/Users/zhiyuanchen/Documents/python/'
file_name_test=dataDir + 'output2.txt'
output_file= dataDir + 'out2.txt'

fTest= open(file_name_test, 'r')
fOut = open(output_file, 'w')
ii=0
outstr=''
a_vec=[0]*50
a_vec[0]=1
a_vec[1]=1
#a_vec means the weight you put on different hierarchy
for line in fTest:
 
        ii=ii+1
        su=0
        count=1
        arr_test=line.strip().split('|')
        line_length=len(arr_test)
        userID= arr_test[0]
        trackID= arr_test[1]
        for j in range(2,50):
                if line_length==4:
                        a_vec[j]=0
                else:
                        a_vec[j]=1
        
        for i in range(2,line_length):
                score=float(arr_test[i])
                su+=score*a_vec[i-2]
                if score!=0:
                        count=count+1
        a=0
        if su==0:
            a=0
        else:
            a=(su/(count-1))
        outstr+=str(a)+'\n'
        #a means the average value of one song, replace su with a, then get the sum
                
        fOut.write(outstr)
        outstr=''

        
fTest.close()
fOut.close()
