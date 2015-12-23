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

[![](https://www.dropbox.com/s/gd7qujzwp37airs/run_monkeyrunner.png?raw=1)]
(https://www.dropbox.com/s/gd7qujzwp37airs/run_monkeyrunner.png?dl=0)

Extending MonkeyRunner with plugins
------------------------------------

Create Java project from Android Studio, create the startup class and implements Predicate<PythonInterpreter>
[![](https://www.dropbox.com/s/nrycuuk67b0ur22/create_jython_class.png?raw=1)]
(https://www.dropbox.com/s/nrycuuk67b0ur22/create_jython_class.png?dl=0)

Modify the manifest attribute in Java project gradle, key is "MonkeyRunnerStartupRunner" and value is your startup class path

[![](https://www.dropbox.com/s/dpmixn9towx5t0c/modify_manifest_attribute.png?raw=1)]
(https://www.dropbox.com/s/dpmixn9towx5t0c/modify_manifest_attribute.png?dl=0)

Export .jar file from Java project

[![](https://www.dropbox.com/s/tail1z3sgsqh3fe/export_jar_file.png?raw=1)]
(https://www.dropbox.com/s/tail1z3sgsqh3fe/export_jar_file.png?dl=0)

Copy .jar file to ~/Library/Android/sdk/tools/lib (regular Android sdk path on Mac. For Windows, please replace ~/Library/Android/ to your sdk path) 

[![](https://www.dropbox.com/s/hdv0ifva8dziqtf/copy_jar_file_to_sdk_lib.png?raw=1)]
(https://www.dropbox.com/s/hdv0ifva8dziqtf/copy_jar_file_to_sdk_lib.png?dl=0)

Import to the Python class, from <the startup class package name> import <startup class name>

[![](https://www.dropbox.com/s/6tr0f652os4im0n/import_to_python_class.png?raw=1)]
(https://www.dropbox.com/s/6tr0f652os4im0n/import_to_python_class.png?dl=0)

Now instead of executing example-test.py file, do with example-test-with-extension.py file to test

####More extension from Python library
https://github.com/dtmilano/AndroidViewClient
