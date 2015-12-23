# Imports the monkeyrunner modules used by this program
import sys, os

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

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
    packageDir = 'target/demo.apk'

    warn = 'IF YOU DON\'T WANT TO INSTALL AGAIN, PLEASE PUT THE CODE IN COMMENT TAG'
    if os.path.exists(packageDir):
        if not device.installPackage(packageDir):
            print('failed to install package. ' + warn)
        else:
            print('install package successfully. ' + warn)

    # sets a variable with the package's internal name
    package = 'com.alton.monkeyrunner'

    # sets a variable with the name of an Activity in the package
    activity = 'com.alton.monkeyrunner.LoginActivity'

    # sets the name of the component to start
    runComponent = package + '/' + activity

    # Runs the component
    device.startActivity(component=runComponent)

    # Presses the Menu button
    # device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

    #Running on Android Simulator is very slow,
    #Wait for UI
    MonkeyRunner.sleep(2.0)

    #Type to focused EditText
    device.type('test')

    MonkeyRunner.sleep(2.0)

    #Open Menu
    device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(2.0)

    # Takes a screenshot
    result = device.takeSnapshot()

    # Writes the screenshot to a file
    screenshotName = 'target/'+deviceName+'/screenshot.png'
    ensure_dir(screenshotName)
    result.writeToFile(screenshotName,'png')

#Start
main()