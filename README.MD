# How to run tests on Appium

## Mac:

1. To make application workable on your device please move to configuration_data/ios_config.json change uidi and app to your
device uidi, path to archived .ipa file.
2. Install Appium Client and Appium Desktop http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/
3. Run Appium Desktop 1.6.1 on Mac machine;
4. After launch Appium Desktop you need to connect iPhone to Mac machine (using USB cable);
5. Make sure that application is build in Xcode with correct settings (prepared for automation testing) (see step 3);
6. Install appium library using next command (pip3 install Appium-Python-Client==0.26)


## Ubuntu:

1. To make application workable on your device please move to configuration_data/ios_config.json change platformVersion and 
deviceName to your device platform and your device id.
2. Download project from repository.
3. Connect Android device to Ubuntu machine (using USB cable);
4. Install ADB Change Language https://play.google.com/store/apps/details?id=net.sanapeli.adbchangelanguage on your Android.
5. Run command adb shell pm grant net.sanapeli.adbchangelanguage android.permission.CHANGE_CONFIGURATION from command line to 
enable possibility to change language by ADB Change Language.
6. Install appium library using next command (pip3 install Appium-Python-Client==0.26).
