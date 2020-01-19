# -*- coding: utf-8 -*-
"""
@script-author:jnanavi k r
@script-description:Predicting the value using
knn algorithm
"""
#assign the train and test data
train=[[1,2,3],[4,5,6],[7,8,9]]
test=[3,6,9]
diff=[]
#Compute the difference matrix
for i in range(len(train)):
    im=[]
    for j in range(len(test)):
        im.append(test[j]-train[i][j])
        diff.append(im)
        dist=[]
#Compute the distance using Euclidian formula
for i in range(len(train)):
    s=0
    for j in range(len(test)):
        s+=diff[i][j]**2
dist.append(s)

dict={} 
# creating a dictionary to link the train data and the distance 
for i in range(len(dist)):
    dict[dist[i]]=train[i]
#sort the distances 
dict=sorted(dict.items())
dict
#Using the k values estimate the predicted value
predict,s=[],0
for i in range(len(dict)):
    s+=dict[i][1][2]
    predict.append(s/(i+1))
predict
#Estimating error
error=[]
for i in range(len(predict)):
    error.append((test[2]-
    predict[i])*100/test[2])
    error
#estimate the accurate value
print("The Accurate value is",predict[error.index(min(error))])
      