# Uninstall-App-Automatically
A python script for uninstalling  the  app  in your Phone or  Simulator automatically

**中文说明 | [README-EN](https://github.com/wuchangfeng/Automatic-unistall-App/blob/master/README-English.MD)**

## About 
开发 Android 的朋友,模拟器或者手机里面常常有大量调试的 Demo，对于手机来说还好，可是对于模拟器，有可能就会造成调试速度以及启动速度的下降。
而且模拟器中 App 一个一个删除也是很麻烦。利用 ADB 命令，我们可以做很多事，其中就包括批量操作模拟器或者手机上的 App。当然包括删除操作啦。
利用 Python 脚本和 ADB shell 命令以及 AS 自带的 CMD 窗口,我们就可以将这一切浓缩成一个命令行啦。


## Usage

``` python
pip install uninstall_app
```
批量卸载模拟器第三方 App

``` python
$  ca
```


## Effect

![](http://7xrl8j.com1.z0.glb.clouddn.com/Use.gif)


## Reference
* [ADB shell 命令](http://imsardine.simplbug.com/note/android/adb/commands/pm.html)
* [ADB 常用命令](https://segmentfault.com/a/1190000000426049)
* [Python 执行系统命令 os.popen](http://www.cnblogs.com/HQMIS/archive/2013/02/03/2890892.html)

## License

The MIT License (MIT)






