package monkeyrunner.ext;

import com.android.monkeyrunner.MonkeyDevice;
import com.android.monkeyrunner.MonkeyImage;
import com.google.common.base.Predicate;

import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

public class MonkeyRunnerExt implements Predicate<PythonInterpreter> {

    //Tap on screen with x, y coordinate
    public static void tap(MonkeyDevice device, int x, int y){
        PyObject[] args = {
                new PyInteger(x),
                new PyInteger(y),
                new PyString("DOWN_AND_UP")
        };
        device.touch(args, null);
    }

    //Press button with keycode of button
    public static void pressButton(MonkeyDevice device, String keyCode){
        PyObject[] args = {
                new PyString(keyCode),
                new PyString("DOWN_AND_UP"),
                new PyString("")
        };
        device.press(args, null);
    }

    //Take and save snapshot in output filename, optionally including its path
    public static void saveSnapshotToFile(MonkeyDevice device, String fileName){
        MonkeyImage monkeyImage = device.takeSnapshot();
        PyObject[] obj = { new PyString(fileName), new PyString("png") };
        monkeyImage.writeToFile(obj, null);
    }

    @Override
    public boolean apply(PythonInterpreter pythonInterpreter) {

        /*
        * Examples of creating and initializing variables in the monkeyrunner environment's
        * namespace. During execution, the monkeyrunner program can refer to the variables "newtest"
        * and "use_emulator"
        *
        */
        pythonInterpreter.set("newtest", "enabled");
        pythonInterpreter.set("use_emulator", 1);

        return false;
    }
}