

import numpy

dataDir='/Users/zhiyuanchen/Documents/python'
file_name_test=dataDir + 'testTrack_hierarchy_win.txt'
file_name_train=dataDir + 'trainIdx2_matrix.txt'
output_file= dataDir + 'output2.txt'

fTest= open(file_name_test, 'r')
fTrain=open(file_name_train, 'r')
Trainline= fTrain.readline()
fOut = open(output_file, 'w')

genre_vec=[[]for i in range(6)]
trackID_vec=[0]*6
albumID_vec=[0]*6
artistID_vec=[0]*6
#make empty vector to put different ID in it
lastUserID=-1

user_rating_inTrain=numpy.zeros(shape=(6,50))
#some songs have so many genre so put 50 in it

for line in fTest:
        arr_test=line.strip().split('|')
        line_length=len(arr_test)
        userID= arr_test[0]
        trackID= arr_test[1]
        albumID= arr_test[2]
        artistID=arr_test[3]
        user_int=int(userID)

        if userID!= lastUserID:
                ii=0
                user_rating_inTrain=numpy.zeros(shape=(6,50))

        trackID_vec[ii]=trackID
        albumID_vec[ii]=albumID
        artistID_vec[ii]=artistID
        for j in range(4,(line_length)):
                genre_vec[ii].append(arr_test[j])
                                

        ii=ii+1
        lastUserID=userID
        
        #read every 6 lines then output once
        if ii==6 :
                while (Trainline):
                # for Trainline in fTrain:

                        arr_train = Trainline.strip().split('|')
                        trainUserID=arr_train[0]
                        trainItemID=arr_train[1]
                        trainRating=arr_train[2]
                        Trainline=fTrain.readline()
                        trainUser_int=int(trainUserID)


                        if trainUser_int<user_int:
                                continue
                        if trainUser_int==user_int:
                                for nn in range(0, 6):
                                        length=len(genre_vec[nn])
                                        
                                        if trainItemID==albumID_vec[nn]:
                                                user_rating_inTrain[nn, 0]=trainRating
                                        if trainItemID==artistID_vec[nn]:
                                                user_rating_inTrain[nn, 1]=trainRating
                                        for jj in range(0,length):
                                                if trainItemID==genre_vec[nn][jj]:
                                                        user_rating_inTrain[nn,(jj+2)]=trainRating
                                        #put all the score value in matrix
                        if trainUser_int>user_int:
                                #when the user change, output the score in matrix
                                for nn in range(0, 6):
                                        length=len(genre_vec[nn])
                                        outstr1=''
                                        for jj in range(0,length):                                                
                                                outstr1+='|'+str(user_rating_inTrain[nn, (jj+2)])
                                        
                                        outStr=str(userID) + '|' + str(trackID_vec[nn])+ '|' + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1])+outstr1
                                        
                                        fOut.write(outStr+'\n')
                                genre_vec=[[]for i in range(6)]
                                break



fTest.close()
fTrain.close()
fOut.close()
