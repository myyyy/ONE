import pickle

data1 = 1232

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

output.close()

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
print type(data1)
# 
# data2 = pickle.load(pkl_file)
# print data2
# pprint.pprint(data2)
# 
# pkl_file.close()