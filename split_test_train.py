import os
import argparse

import numpy as np
import pandas as pd

np.random.seed(1)

def main():
 
 parser = argparse.ArgumentParser()
 parser.add_argument('--test_value',type=float,default=0.2,help="1")
 args=parser.parse_args()
 split(args.test_value)

def split(test_value):
 
 print ("test_valuetosplit",test_value)
 csv_dir="csv"
 labels=pd.read_csv(os.path.join(csv_dir,'labels.csv'))
 #print labels
 label=labels.groupby('filename')
 print label
 g_list=[label.get_group(x) for x in label.groups]
 Size_train_test=int(len(g_list)*(1-test_value))
 print ("train image {} from total {} ".format(Size_train_test,len(g_list)))
 
 Train_index=np.random.choice(len(g_list),size=Size_train_test,replace=False)
 
 test_index=np.setdiff1d(list(range(len(g_list))),Train_index)
 train=pd.concat([g_list[i] for i in Train_index])
 test = pd.concat([g_list[i] for i in test_index])
 print (len(train),len(test))
 train.to_csv(os.path.join(csv_dir,'train_labels.csv'))
 test.to_csv(os.path.join(csv_dir,'test_labels.csv'))

if __name__=="__main__":

 main()

