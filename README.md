#z/OS Sublime Text 3 plugin
The plugin improves the Sublime Text 3 editor to make it easier to work with z/OS system.

#Functionality:
+ submit job
+ submit job and wait response
+ open dataset from mainframe host
+ hlasm and jcl highlighting

#Installation
To install the plugins you should follow these steps:
1.	Copy files from this directory to a new directory created in path C:/Users/%CURRENT_USER%/AppData/Sublime Text 3/Packages/
2.	For syntax highlighting you could select HLASM or JCL highlighting type (use Preferences -> Color Scheme  -> Pastels on Dark)
3.	Additionally you could add Key Bindings to your editor to make it easier to use the plugin. Your user key bindings file could look like this:
![alt text](http://i63.tinypic.com/2vud841.png "Example ") 
```python
[
	{"keys": ["ctrl+1"], "command": "submit_job"},
	{"keys": ["ctrl+2"], "command": "submit_job_and_wait"},
    {"keys": ["ctrl+5"], "command": "submit_job_with_host"},
    {"keys": ["ctrl+6"], "command": "submit_job_with_host_and_wait"},
	{"keys": ["ctrl+3"], "command": "open_dataset"},
    {"keys": ["ctrl+4"], "command": "save_dataset"},
]
```
#Usage example
Before you could firstly use your plugin you should enter all information about the connection (setsettings command), including host address, login and password. They will be saved in settings.txt file.

#Command usage
Commands could be used from console interface or using key bindings. To use command from console type in window.run_command(“%COMMAND_NAME%”).

#Command names

+ submit_job – submit job to host
+ submit_job_and_wait – submit job to host and display results
+ submit_job_with_host – submit job to host that is typed in by user
+ submit_job_with_host_and_wait – submit job to host that is typed in by user and display the results
+ open_dataset – open dataset typed in by user 
+ save_dataset – save current tab to dataset typed in by user
+ set_settings – save new settings using user input panels
+ change_settings – opens a settings file in a new tab
