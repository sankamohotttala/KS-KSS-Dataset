import os
import shutil
import json

# INPUT_PATH=R'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-child-set-2-final' #HERE WE HAVE ALL CLASSES OF DATA
# OUTPUT_PATH=R'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-child-set-2-final-dataset'  #we save the final dataset here

# INPUT_PATH=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-adult-5-classes-final' #HERE WE HAVE ALL CLASSES OF DATA
# OUTPUT_PATH=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-adult-5-final-dataset'  #we save the final dataset here

INPUT_PATH=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-adult-3-classes-final' #HERE WE HAVE ALL CLASSES OF DATA
OUTPUT_PATH=r'F:\Data Sets\Skeleton\2D\Child\Kinetics Subsets\All final subsets\json-adult-3-final-dataset'  #we save the final dataset here

directory_map_class={'catching or throwing baseball':48,'hopscotch':156,'climbing tree':68,'cutting watermelon':83,'squat':330,
                     'bouncing on trampoline':30,'pull ups':255,'clapping':57 }

def main():
    subDirNames,subDirPaths=getSubDir(INPUT_PATH) #class old paths
    # newJsonPaths=createNewDir(subDirNames,OUTPUT_PATH) #class new path

    finalDirPath=os.path.join(OUTPUT_PATH,'data')
    if not os.path.exists(finalDirPath):
        os.mkdir(finalDirPath) #create data folder

    #create the path for json file
    finalFileName=os.path.join(OUTPUT_PATH,'data_label.json')


    jsonLabelDic={}
    for className, currentPath in zip(subDirNames,subDirPaths):
        allVideos=os.listdir(currentPath)
        for video in allVideos: #iterate through all videos in a one class
            tmpDic={}
        
            videoPath=os.path.join(currentPath,video) #original video path
            jsonFile=os.listdir(videoPath)
            assert len(jsonFile)==1
            dataJsonPath=os.path.join(videoPath,jsonFile[0])

            shutil.copy2(dataJsonPath, finalDirPath)

            #read_skeleton_true
            content=LoadJSON(dataJsonPath)
            if len(content['data'])==0:
                tmpDic['has_skeleton']=False
            else:
                tmpDic['has_skeleton']=True
            
            tmpDic['label']=className
            tmpDic['label_index']=directory_map_class[className]

            #add to original json file
            jsonLabelDic[video]=tmpDic



    jsonFileCreate(finalFileName,jsonLabelDic)




def getSubDir(directory): #here this to be sued when we know there area no files on the directory;onlu subdirectories
    subDirList=os.listdir(directory)
    subDirPathList=[os.path.join(directory,subDir) for subDir in subDirList]
    return subDirList,subDirPathList

def createNewDir(dirNames,directory):
    subDirPaths=[os.path.join(directory,dirName) for dirName in dirNames]
    for subDirPath in subDirPaths:
        if not os.path.exists(subDirPath):
            os.mkdir(subDirPath)
    
    return subDirPaths

def jsonFileCreate(path,dictionary):
    with open(path, "w+") as outfile:
        json.dump(dictionary, outfile)

def LoadJSON(fileDirectory):
    with open(fileDirectory, "r") as write_file:
        # print(type(write_file))
        return json.load(write_file)

if __name__=='__main__':
    main()