# Automatic-unistall-App
A python script for unistalling  the  app  in your Phone or  Simulator automatically

## About 
开发 Android 的朋友,模拟器或者手机里面常常有大量调试的 Demo，对于手机来说还好，可是对于模拟器，就会造成调试速度以及启动速度的下降。
而且模拟器一个一个删除也是很麻烦。
利用 adb 命令，我们可以做很多事，其中就包括批量操作模拟器或者手机上的 App。当然包括删除。

## Effect

![](http://7xrl8j.com1.z0.glb.clouddn.com/Use.gif)

[another Gif see Here](http://7xrl8j.com1.z0.glb.clouddn.com/autoDelete.gif)

## Usage

*  确保你的 AS 能够使用 ADB 命令
*  配置 Python 2.7 环境
*  在 AS 提供的 CMD 中找到当前脚本路径 输入: python unistall.py
*  根据命令提示输入你想要删除 App 的包的核心关键字，如:com.example.RxCacheDemo ,输入 example 即可
*  以上步骤完成之后会有提示 删除成功与否。

**当然,脚本还可以指定具体应用进行删除**,你只需要去掉注释以及注释调用现有函数的代码即可。

## Reference
* [ADB shell 命令](http://imsardine.simplbug.com/note/android/adb/commands/pm.html)
* [ADB 常用命令](https://segmentfault.com/a/1190000000426049)
* [Python 执行系统命令 os.popen](http://www.cnblogs.com/HQMIS/archive/2013/02/03/2890892.html)

## License

The MIT License (MIT)






