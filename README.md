# MonkeyRunner Sample Project

Research for MonkeyRunner tool

How to run
-------------

Run MonkeyRunner from "app" module:

From Android Studio terminal, change directory to app/src/test/monkeyrunner
- cd app/src/test/monkeyrunner
- or just drag the monkeyrunner folder to terminal to open as new tab.

Execute example-test.py file 
- monkeyrunner example-test.py

![](https://www.dropbox.com/s/gd7qujzwp37airs/run_monkeyrunner.png?raw=1)

Extending MonkeyRunner with plugins
------------------------------------

Create Java project from Android Studio, create the startup class and implements Predicate&lt;PythonInterpreter&gt;
![](https://www.dropbox.com/s/nrycuuk67b0ur22/create_jython_class.png?raw=1)

Modify the manifest attribute in Java project gradle, key is "MonkeyRunnerStartupRunner" and value is your startup class path
![](https://www.dropbox.com/s/dpmixn9towx5t0c/modify_manifest_attribute.png?raw=1)

Export .jar file from Java project
![](https://www.dropbox.com/s/tail1z3sgsqh3fe/export_jar_file.png?raw=1)

Copy .jar file to ~/Library/Android/sdk/tools/lib (~/Library/Android/sdk is a default Android sdk path on Mac)
![](https://www.dropbox.com/s/hdv0ifva8dziqtf/copy_jar_file_to_sdk_lib.png?raw=1)

Import to the Python class, from &lt;the startup class package name&gt; import &lt;startup class name&gt;
![](https://www.dropbox.com/s/6tr0f652os4im0n/import_to_python_class.png?raw=1)

Now instead of executing example-test.py file, do with example-test-with-extension.py file to test

#### Android View Client library. Check here
https://github.com/dtmilano/AndroidViewClient
