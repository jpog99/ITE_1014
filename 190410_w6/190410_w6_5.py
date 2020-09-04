import imageio

img = imageio.imread('carry_grant.jpg')

size = img.shape

pixList = []
totPix = 0
count = 0

for x in range(0,size[0]):
    for y in range(0,size[1]):
        pix = img[x][y]
        pixList.append(pix)
        totPix += pix
        count += 1
    
data = {}
for bin in pixList:
    data[bin] = data.get(bin, 0) +1


dataList = list(data.items())

#sorting the dictionary in decending order
for max in range(len(dataList)-1, -1, -1):
    change = False
    for i in range(max):
        if dataList[i][1] < dataList[i+1][1]:
            dataList[i], dataList[i+1] = dataList[i+1], dataList[i]
            change= True
    if not change:
        break

#calculate mean
mean = totPix / count

#cakculate median
mid = int(len(dataList)/2)
mid2 = mid - 1 #because data in decrease order
median = (dataList[mid][0]+dataList[mid2][0])/2

#calculate variance
sum = 0
for idx in range (0,len(dataList)):
    sum = sum + (dataList[idx][0]-mean)**2
variance = sum/(len(dataList)-1)


print('Maximum pixel values: '+ str(dataList[0][0]) + ' ('+ str(dataList[0][1]) +' pixels)')
print('\nMinimum pixel values: '+ str(dataList[-1][0])+ ' ('+ str(dataList[-1][1]) +' pixels)')
print('\nMedian pixel value: '+str(median))
print('\nMean Value (Total pixel value per pixel): '+ str(mean))
print('\nVariance of pixel values: '+ str(variance))
