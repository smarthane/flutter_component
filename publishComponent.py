# -*- coding: utf-8
#################################################
# @author smarthane
# @time 2020/1/1 10:55
# @describe 打包flutter module为aar原生工程依赖脚本
#################################################

import os
import platform

# 读取gradle.properties配置
class Properties(object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = {}

    def __getDict(self,strName,dictName,value):
        if(strName.find('.')>0):
            k = strName.split('.')[0]
            dictName.setdefault(k,{})
            return self.__getDict(strName[len(k)+1:],dictName[k],value)
        else:
            dictName[strName] = value
            return

    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'Ur')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#")!=-1:
                    line=line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1]= line[len(strs[0])+1:]
                    self.__getDict(strs[0].strip(),self.properties,strs[1].strip())
        except Exception, e:
            raise e
        else:
            pro_file.close()
        return self.properties

# 构建aar并发布到maven私服
class BuildAarAndPublish(object) :
    # 修改flutter指定版本sdk路径
    properties = Properties("gradle.properties").getProperties()
    flutterSdkPath = properties['flutterSdkPath']
    sysstr = platform.system()

    # 打包flutter_module为aar
    def buildModuleAar(self):
        flutterLibVersion = self.properties['flutterLibVersion']
        print('1. start buildModuleAar ... ' + flutterLibVersion)
        os.system("cd flutter_module && " + self.flutterSdkPath + " clean")
        os.system("cd flutter_module && " + self.flutterSdkPath + " pub get")
        os.system("cd flutter_module && " + self.flutterSdkPath + " build aar --build-number " + flutterLibVersion)

    # 上传flutter_module到maven私服，中有isPublishLocal配置为false则为发布到私服否则为发布到本地
    def uploadModuleAar(self):
        isPublishLocal = self.properties['isPublishLocal']
        print('2. start uploadModuleAar ... isPublishLocal=' + isPublishLocal)
        if isPublishLocal == "false":
           if self.sysstr == "Windows":
              os.system("gradlew flutter_lib:clean publish")
           else:
              os.system("./gradlew flutter_lib:clean publish")


    # 上传flutter_lib到maven私服
    def uploadLibAar(self):
        print('3. start uploadLibAar ... ' + self.sysstr)
        if self.sysstr == "Windows":
           os.system("gradlew flutter_lib:clean uploadArchives")
        else:
           os.system("./gradlew flutter_lib:clean uploadArchives")

if __name__ == '__main__':
    buildAar = BuildAarAndPublish()
    buildAar.buildModuleAar()
    buildAar.uploadModuleAar()
    buildAar.uploadLibAar()