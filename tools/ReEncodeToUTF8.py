

# Import the os module, for the os.walk function
import os
import codecs
from shutil import copyfile

def createDirIfNotExist(dirPath):
	if not os.path.exists(dirPath):
	    os.makedirs(dirPath)

def encodeFileToUTF8(srcFilePath, targetFilePath):
	source = open(srcFilePath)
	target = open(targetFilePath, "w")
	target.write(unicode(source.read(), 'big5').encode('utf8'))

 
# Set the directory you want to start from
workDir = os.path.dirname(os.path.abspath(__file__))
outputDir = workDir + '/../output/allPay/'
traverseDir = workDir + '/../allPay/'

createDirIfNotExist(outputDir)

print('output dir : %s' % outputDir)
print('traverseDir dir : %s\n' % traverseDir)

for dirName, subdirList, fileList in os.walk(traverseDir):
	outputPackageDir = outputDir + dirName.rsplit(traverseDir,1).pop()
	createDirIfNotExist(outputPackageDir)
	print('check package dir : %s' % dirName)
	for fname in fileList:
		if not fname.startswith('.'):
			srcFilePath = dirName + '/' + fname
			targetFilePath = outputPackageDir + '/' +fname
			try:
				encodeFileToUTF8(srcFilePath, targetFilePath)
				print('\tconvert file: %s' % fname)
			except:
				copyfile(srcFilePath, targetFilePath)
				print('\tcopy file: %s' % fname)




