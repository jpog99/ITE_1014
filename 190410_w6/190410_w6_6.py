import imageio
img = imageio.imread('carry_grant.jpg')

size = img.shape

pixList = []

for x in range(0,size[0]):
    for y in range(0,size[1]):
        pix = img[x][y]
        pixList.append(pix)
    
data = {}
for bin in pixList:
    data[bin] = data.get(bin, 0) +1
  
for j in range(248,256):
    data[j] = 0

percsum = 0
print ('Bin\tCount\tPercentage')
for i in range (0,256) :
    perc = data[i]*100/810000
    print (i,':\t',data[i],'\t',str(round(perc,3))+ ' %')
    percsum += perc
   
print('\nSum of Percentage: ' + str(round(percsum,3)) + '%')


