# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os;

# 删除所有你指定包名的 APP
def delAllapp( ):
    
    print 'start delete all your app in your Phone or Simulator '
    os.popen('adb wait-for-device');
    corename = raw_input("input your app package corename:")
    oriPackages = os.popen('adb shell pm list packages {name}'.format(name=corename));

    for oriPackage in oriPackages:
        
        deletePackage = oriPackage.split(':')[1]
        os.popen('adb uninstall ' + deletePackage );
        print deletePackage + "is deleted"
        

# 删除所有你指定包名的特定 APP
def listAllpackage( ):
    
    i = 0
    os.popen('adb wait-for-device');
    corename = raw_input("input your app package corename:")
    oriPackages = os.popen('adb shell pm list packages {name}'.format(name=corename));

    for oriPackage in oriPackages:
        
        deletePackage = oriPackage.split(':')[1]
        print str(i) + ":" + deletePackage
        deleteList.append(deletePackage)
        i += 1

def deleteApp(number):
    os.popen('adb uninstall ' + deleteList[number] );
    print 'delete '+ deleteList[number] + "success"
    

if __name__ == '__main__':
    
    delAllapp()
    ```
    another fun here
    ```
    #deleteList = []
    #listAllpackage()
    #number = raw_input("input the number of app you want to delete:")
    #deleteApp(int(number))
