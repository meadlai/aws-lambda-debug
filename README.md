# aws-lambda-debug

由于Eclipse没有AWS toolkit, 于是使用PyCharm进行开发,发现只有PRO的付费版本才能有调试功能,并且使用专用调试器pydevd_pycharm. 比较麻烦的是必须配合sftp进行调试,这对应win本地调试并不友好,遂放弃.https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html#summary

然后换了VSCode 

### 环境准备

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html

主要是安装Python3, AWS CLI 2, AWS SAM, Docker desktop



### 配置账号

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html

```
    aws configure
    aws configure list
```


### VSCode 开发环境

主要参考文章: https://github.com/aws/aws-toolkit-vscode/blob/master/docs/debugging-python-lambda-functions.md

  ```bash
  cd ${project_root}
  ```

 - 初始化虚拟环境
  
  ```bash
  python3 -m venv ./.venv
  ```

 - 激活虚拟环境
 
 ```bash
. ./.venv/bin/activate
```

 - 其中的requirements.txt,添加了最新版本的ptvsd, 发现ptvsd==4.2.4其实是有问题的,最新版本是4.3.2

 - 安装依赖
 
 ```
   python3 -m pip install -r ${workspace}/vscode/hello_world/requirements.txt
   python3 -m pip install -r /Users/dev_local/Documents/Project/aws/vscode/vscode/hello_world/requirements.txt
```

 - 编译项目,每次修改代码,都要手动执行编译,不然断点位置不对

```bash
    sam build
```

 - 启动项目,开启debug端口5678,等待连接

```bash
    sam local invoke -e events/event.json HelloWorldFunction -d 5678
```

 - 按F5进行编译,代码将停止在断点位置.

<sam app root>/.vscode/launch.json 里面的路径映射貌似不对,会报以下错误:
        pydev debugger: unable to find translation for: "/Users/dev_local/Documents/Project/aws/vscode/vscode/hello_world/app.py" in ["/Users/dev_local/Documents/Project/aws/vscode/hello_world/build"] (please revise your path mappings).

改成下面的路径映射, 断点可以使用

```
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/vscode/hello_world",
                    "remoteRoot": "/var/task"
                }
            ]
```
