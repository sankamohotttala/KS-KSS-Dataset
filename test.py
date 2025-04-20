#make sure direcotories are correctly named or dictionary_map_class is change accordinhg to the directory names 
#currupt videos are taken care ; is that the difference between this code and convertToStandardForm.py

import os
import re
import json

# ROOT='./All final subsets/json-child-set-2'
# ROOT='./All final subsets/json-adult-5-classes'
ROOT='./All final subsets/json-adult-3-classes'

# NEW_JSON_ROOT='./All final subsets/json-child-set-2-final'
# NEW_JSON_ROOT='./All final subsets/json-adult-5-classes-final'
NEW_JSON_ROOT='./All final subsets/json-adult-3-classes-final'

tmpDict={} 

directory_map_class={'catching or throwing baseball':48,'hopscotch':156,'climbing tree':68,'cutting watermelon':83,'squat':330,
                     'bouncing on trampoline':30,'pull ups':255,'clapping':57 }

def main():
    subDirNames,subDirPaths=getSubDir(ROOT) #class old paths
    newJsonPaths=createNewDir(subDirNames,NEW_JSON_ROOT) #class new path

    for className, currentPath, futurePath in zip(subDirNames,subDirPaths,newJsonPaths):
        allVideos=os.listdir(currentPath)
        for video in allVideos: #iterate through all videos in a one class
            dataDic={}
        
            videoPath=os.path.join(currentPath,video) #original video path
            # jsonPathFinal=createNewDir([video],futurePath) #this returns the final json file path (as a jist with one value)
            
            #get file name
            frameFiles=os.listdir(videoPath)
            if len(frameFiles)==0:
                print("no json files availanle: ", videoPath)
                continue

            jsonPathFinal=createNewDir([video],futurePath) # shifted here from above; no issue since no effect; because we don't want empty directories

            filename=getFileNameFromFrameJson(frameFiles[0])
            finalFileName=os.path.join(jsonPathFinal[0],filename+'.json')
            
            # sampleDict={i:i for i in range(10)}

            # get the data in the standard format
            orderedList=getFrameNumberAscendingFrameList(frameFiles)
            data=[]
            numOfFrames=len(orderedList)

            for frameName, frameIndex in orderedList:
                tmpFrame={}
                framPath=os.path.join(videoPath,frameName)
                frameContent=LoadJSON(framPath)
                
                tmpSkeletonList=[]
                tmpFrame['frame_index']=frameIndex
                
                
                allSkeletons=frameContent['people']
                numOfSkeletons=len(allSkeletons)
                for index,skeleton in enumerate(allSkeletons):
                    # tmpListOriginal.append(skeleton['pose_keypoint_2d'])
                    tmp=skeleton['pose_keypoints_2d']
                    pose,score=poseScoreExtract(tmp)
                    skeletonDic={'pose':pose,'score':score}
                    tmpSkeletonList.append(skeletonDic)

                tmpFrame['skeleton']=tmpSkeletonList
                data.append(tmpFrame)

            dataDic['data']=data
            dataDic['label']=className 
            dataDic['label_index']=directory_map_class[className]   

            jsonFileCreate(finalFileName,dataDic)
            # tmpDict.clear() #actual dictionary is cleared 


            
            
        pass


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

def getFileNameFromFrameJson(filename):
    filename_useful=filename.strip().split('.')[0]
    indices = [i.start() for i in re.finditer('_', filename_useful)]
    end_index=indices[-4]
    fileRealName=filename_useful[:end_index]
    return fileRealName    

def jsonFileCreate(path,dictionary):
    with open(path, "w+") as outfile:
        json.dump(dictionary, outfile)

def getFrameNumberAscendingFrameList(frameList):
    finalList=[]
    for frame in frameList:
        filename_useful=frame.strip().split('.')[0]
        indices = [i.start() for i in re.finditer('_', filename_useful)]
        start,end=(indices[-2], indices[-1])
        numStr=filename_useful[start+1:end]
        finalList.append((frame,int(numStr)))
    finalList.sort(key=lambda i:i[1],reverse=False)
    # print(finalList)
    return finalList


def LoadJSON(fileDirectory):
    with open(fileDirectory, "r") as write_file:
        # print(type(write_file))
        return json.load(write_file)

def poseScoreExtract(pose_keypoint_2d): #gives assert error if not BODY_25 or missiong values
    assert len(pose_keypoint_2d)==75
    x_values=pose_keypoint_2d[::3]
    y_values=pose_keypoint_2d[1::3]
    
    score=pose_keypoint_2d[2::3]
    pose=[]
    for x,y in zip(x_values,y_values):
        pose.extend([x,y])
    
    return pose,score

    
if __name__=='__main__':
    main()