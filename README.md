
# Flutter Component（Flutter组件化工程）

## Flutter Component 
这是一个基于Flutter开发的工程，然后将其打包成aar包发布maven，最终安卓原生工程只要和普通的依赖方式依赖一个aar包就可以进行集成来达到混合开发目的。

### 工程模块说明：
- app: 此模块为集成aar(flutter_lib)来测试的host app。
- flutter_lib： 安卓原生模块，用于编写原生代码或者与flutter有交互的代码。其依赖的是flutter_module,执行发布脚本，发布成一个aar到maven,最终原生工程依赖这个aar包。
- flutter_module: flutter module，纯flutter开发代码。flutter官方集成flutter module到现有原生工程的方案。

### 打包为aar原理：
1. 在flutter_module模块根目录执行官方的打aar包命令：flutter build aar。
2. 执行完flutter_module模块的打aar包命令后，会在目录flutter_component\flutter_module\build\host\outputs\repo下生成本地maven仓库的aar依赖包。
3. 把在repo目录下生成的aar和pom上传到maven服务器仓库。脚本可以参考flutter_lib模块下的publish.gradle文件中的publishing。
4. 把flutter_lib生成的aar发布到maven服务仓库。脚本可以参考flutter_lib模块下的publish.gradle文件中的uploadArchives。
5. 最终安卓原生工程只要依赖flutter_lib发布的aar即可（flutter_module相关依赖在pom文件描述中，加载flutter_lib时就会下载flutter_module的aar和flutter依赖）。

## 配置说明 
工程根目录gradle.properties，所有配置都在此文件。
```
###################################################################################################
# flutter SDK 目录，适配不同的flutter版本
flutterSdkPath="D:\\flutter_1.14.6-beta\\bin\\flutter"
# 开发模式，如为开发模式为true则直接为源码依赖,否则为maven依赖。true: dev ,false: prod  release
isBuildDev=false
# ------------------------------------------------------------------------------------------------#
# 发布到本地为true，远程私服为false
isPublishLocal=false
# maven（NEXUS）私服用户名密码
nexusUsername=admin
nexusPassword=admin123

# flutter_lib groupId
flutterLibGroupId=com.smarthane.flutter.component.lib
# flutter_lib artifactId
flutterLibArtifactId=flutter_lib

# 发布aar的版本,版本分为快照: snapshot ;正式: release;
# 1. snapshot
# flutter_lib 发布snapshot仓库地址
repoUrl=http://localhost:8081/repository/maven-snapshots/
# flutter_lib version
flutterLibVersion=1.0.2-SNAPSHOT

# 2. release
# flutter_lib 发布release仓库地址
# repoUrl=http://localhost:8081/repository/maven-releases/
# flutter_lib version
# flutterLibVersion=1.0.4
###################################################################################################
```

## 执行脚本
- 在工程根目录执行 python .\publishComponent.py 即可发布aar到maven私服。
- 可以参看本工程flutter_component的详细配置和集成。

## 其它说明
1. [maven私服搭建](https://blog.csdn.net/yyqhwr/article/details/89922178)
2. [python环境](https://www.runoob.com/python/python-install.html)
3. [armeabi平台支持](https://www.jianshu.com/p/4fa5a66fb8de)
4. [其它打包aar集成原生工程方案](https://www.jianshu.com/p/2258760e9540)