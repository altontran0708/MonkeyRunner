# MonkeyRunner

Research for monkeyrunner tool

Integrate
-------------

####Run MonkeyRunner with Sample Project

Change Directory to app/src/test/monkeyrunner
- cd app/src/test/monkeyrunner

Execute example-test.py file 
- monkeyrunner example-test.py

[![](https://photos-1.dropbox.com/t/2/AAD0FQzrRUHXTp5h5jfDKNBKoDkBEmCKGJRbEldjaioiQA/12/231954667/png/32x32/3/1450872000/0/2/run_monkeyrunner.png/ELC6lcQBGImdASAHKAc/tPVlufO4cLnorHVgSPqxdfPcFnVbEqn0R9ryo2ExS8U?size_mode=3&size=800x600)]
(https://www.dropbox.com/s/gd7qujzwp37airs/run_monkeyrunner.png?dl=0)

####Extending monkeyrunner with Plugins

Export .jar file from Jython project

[![](https://photos-4.dropbox.com/t/2/AAB8R2b5aB-VdvAT8KfS-rBiu2hBj7HtQPMkp9gFt7x8xw/12/231954667/png/32x32/3/1450872000/0/2/export_jar_file.png/ELC6lcQBGImdASAHKAc/GYX3b_ItsRQ5z5TsGlACtUyqLp5QFqnENMpYcjnnBv8?size_mode=3&size=800x600)]
(https://www.dropbox.com/s/tail1z3sgsqh3fe/export_jar_file.png?dl=0)

Copy .jar file to ~/Library/Android/sdk/tools/lib (regular Android sdk path on Mac. For Windows, please replace ~/Library/Android/ to your sdk path) 

[![](https://photos-6.dropbox.com/t/2/AAA5n_enENU6NhOu9PmWdtLJpALdsreh_9zM40R3tboxsg/12/231954667/png/32x32/3/1450872000/0/2/copy_jar_file_to_sdk_lib.png/ELC6lcQBGImdASAHKAc/PBCwzR79Le0dZsjSVWp-zgDz6y-2Zny3Ujrc1S74dLM?size_mode=3&size=800x600)]
(https://www.dropbox.com/s/hdv0ifva8dziqtf/copy_jar_file_to_sdk_lib.png?dl=0)

Now instead of executing example-test.py file, 
Execute example-test-with-extension.py file

####More Extension from Python library
https://github.com/dtmilano/AndroidViewClient
