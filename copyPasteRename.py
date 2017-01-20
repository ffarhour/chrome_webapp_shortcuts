# Author: Farmehr Farhour
# Script to create a manifest.json file that would create a chrome webapp shortcut to a user-specified website

import os
name = raw_input("Please type the name of the Website (no spaces)")
longname = raw_input("Please enter the long name[optional]")
if(longname==""):
    longname = name
url = raw_input("Input url of the website")

if not os.path.exists(name):
    os.makedirs(name)


text_file = open(os.path.join(name,"manifest.json"), "w")
text = '{ "manifest_version": 2, "name": "' + longname + '", "description": "' + longname + ' WebApp", "version": "1.0", "icons": { "128": "128.png" }, "app": { "urls": [ "' + url + '" ], "launch": { "web_url": "' + url + '" } }, "permissions": [ "unlimitedStorage", "notifications" ] }'
text_file.write(text)
text_file.close()

print("PLEASE ENSURE THAT YOU DOWNLOAD A LOGO FOR THE WEBSITE AND PLACE IT IN THE RELATIVE FOLDER WITH THE NAME '128.png'")
