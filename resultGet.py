import numpy

dataDir='/Users/zhiyuanchen/Documents/python/'
file_name_test=dataDir + 'out2.txt'
output_file= dataDir + 'new1.txt'

fTest= open(file_name_test, 'r')
fOut = open(output_file, 'w')

ii=0
outstr=''
su_vec=[0]*6
pt=numpy.zeros(shape=(6,1))

for line in fTest:
        
        arr_test=line.strip()
        su_vec[ii]= float(arr_test)
        
        ii=ii+1
        #every 6 lines output once
        if ii==6:
            ii=0
            for nn in range(0,6):
                if su_vec[nn]==max(su_vec):
                    pt[nn,0]=1
                    su_vec[nn]=-2000000
                    break
            
            for nn in range(0,6):
                if su_vec[nn]==max(su_vec):
                    pt[nn,0]=1
                    su_vec[nn]=-2000000
                    break
            for nn in range(0,6):
                if su_vec[nn]==max(su_vec):
                    pt[nn,0]=1
                    su_vec[nn]=-2000000
                    break
            #put the highest three value as"1"
            #could be changed to lowest 3 value as"0" by change zeros martix to ones
            #max function to min 

            
            for jj in range(0,6):
                
                outstr=str(int(pt[jj,0]))
                fOut.write(outstr+'\n')




        outstr=''
        pt=numpy.zeros(shape=(6,1))
 

        
fTest.close()
fOut.close()
