Title: BluetoothAdapter使用
Date: 2014-11-22 10:52
Category: android
Tags: Bluetooth
Slug: BluetoothAdapter

## Android Quick Look: BluetoothAdapter

Android SDK附带强大的蓝牙适配器,蓝牙api能够管理本地扫描附近的蓝牙设备,蓝牙设备之间传输数据,等等。本指导将向您展示最基本的必要步骤开始在Android SDK编程蓝牙应用程序。

#### Step 1: Import the Bluetooth Package

```java
import android.bluetooth.*;
```

#### Step 2: Set Bluetooth Permissions

添加permission:
```java
<uses-permission android:name="android.permission.BLUETOOTH" />
```

对于更高级的蓝牙任务，如设置本地设备为我们将在本教程的名字，你就需要配置蓝牙管理员权限。添加以下行这样做：

```java
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
```

#### Step 3: Access the Bluetooth Adapter

BluetoothAdapter是访问Android设备上蓝牙的单例。这个类必须被实例化，以便在程序执行任何蓝牙相关的任务。

```java
BluetoothAdapter bluetooth = BluetoothAdapter.getDefaultAdapter();
```

如果设备不支持蓝牙，以上将返回`null`.在实际应用中我们应该检查条件更新应用。

```java
BluetoothAdapter bluetooth = BluetoothAdapter.getDefaultAdapter();
if(bluetooth != null)
{
    // Continue with bluetooth setup.
}
```

#### Step 4: Check if Bluetooth is Enabled

```java
if (bluetooth.isEnabled()) {
    // Enabled. Work with Bluetooth.
} else {
    // Disabled. Do something else.
}
```

Step 5: Display Device Name and Address

如果蓝牙可用，我们将展示设备的名称和地址；不可用时，向用户展示信息

```java
String status;
if (bluetooth.isEnabled()) {
    String mydeviceaddress = bluetooth.getAddress();
    String mydevicename = bluetooth.getName();
    status = mydevicename + ” : ” + mydeviceaddress;
} else {
    status = “Bluetooth is not Enabled.”;
}
Toast.makeText(this, status, Toast.LENGTH_LONG).show();
```

这段代码使用getName()方法来得到蓝牙设备名称。如果您之前设置的BLUETOOTH_ADMIN权限，你也可以更改设备名称，像这样：

```java
bluetooth.setName("AndroidCoder");
```

Step 6: Display Bluetooth State

BluetoothAdapter.getState()用于获得详细的蓝牙状态。状态有以下4个值：

- STATE_TURNING_ON
- STATE_ON
- STATE_TURNING_OFF
- STATE_OFF

#### Conclusion

这篇导读简单介绍了Bluetooth的使用，上面包含的代码将检查是否启用蓝牙功能，并显示诊断信息。