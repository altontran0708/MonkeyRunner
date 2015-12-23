# Imports the monkeyrunner modules used by this program
import sys, os

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from monkeyrunner.ext import MonkeyRunnerExt

#Ensure Directory class
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

#Main class
def main():
    print('start')
    # Connects to the current device, returning a MonkeyDevice object
    timeOut = 10;

    if len(sys.argv) >= 2:
        deviceName = sys.argv[1]
        device = MonkeyRunner.waitForConnection(timeOut, deviceName)
    else:
        deviceName = 'defaultDevice'
        device = MonkeyRunner.waitForConnection(timeOut)

    print(deviceName)

    # Installs the Android package. Notice that this method returns a boolean, so you can test
    # to see if the installation worked.
    # packageDir = 'target/demo.apk'

    # if os.path.exists(packageDir):
    #     if not device.installPackage(packageDir):
    #         print('failed to install package')
    #     else:
    #         print('install package successfully')

    # sets a variable with the package's internal name
    package = 'com.alton.monkeyrunner'

    # sets a variable with the name of an Activity in the package
    activity = 'com.alton.monkeyrunner.LoginActivity'

    # sets the name of the component to start
    runComponent = package + '/' + activity

    # Runs the component
    device.startActivity(component=runComponent)

    MonkeyRunner.sleep(1.0)

    # Press Home Button
    MonkeyRunnerExt.pressButton(device, 'KEYCODE_HOME')

    MonkeyRunner.sleep(1.0)

    # Takes a screenshot and Writes the screenshot to a file
    screenshot = 'target/'+deviceName+'/screenshot-extension.png'
    MonkeyRunnerExt.saveSnapshotToFile(device, screenshot)

#Start
main()