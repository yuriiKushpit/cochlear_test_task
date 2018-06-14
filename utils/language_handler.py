import subprocess


def adb_shell(command, serial=None, adbpath='adb shell'):
    args = adbpath
    if serial is not None:
        args += ' -s ' + serial
    args += ' ' + command
    return subprocess.check_output(args, shell=True)


def change_language(language="en"):
    cmd = "am start -n net.sanapeli.adbchangelanguage/.AdbChangeLanguage -e language {}".format(language)
    return adb_shell(cmd)