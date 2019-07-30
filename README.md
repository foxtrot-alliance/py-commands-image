# py-commands-image
This program allows you work with UI automation based on images, pixel matching. You can run the program via the CMD or as part of an automation script in an RPA tool like Foxtrot. This solution is meant to supplement Foxtrots core functionality and enable you to perform certain actions based on the position of images on the screen rather than Foxtrots own targeting technology. The solution is written in Python using the modules "pyautogui". You can see the [full source code here](https://github.com/foxtrot-alliance/py-commands-iamge/blob/master/py-commands-image.py).

## Expectations
You should not expect this solution to work flawlessly. Basically, "pyautogui" takes the provided image file and reads all the pixels to scan the whole screen (or specified region of the screen) for matching pixels. This is a lengthy process, therefore, it is not a fast solution. You should expect each command to take between 2-10 seconds pending on various factors. Also, you have to be very aware that it is extremely sensitive and will literally match the exact pixels from the image with the pixels on the screen. Therefore, even the slightest differences will cause the solution to not be able to find a match. For example, if the focus is on the app at the moment of taking the screenshot, making the app 'brighter', but not in focus at the moment of execution will most likely make it unable to find a match.

By default, the solution will assume that you only wish to continue if exactly one match is found on the screen. So, in case you have taken a screenshot of an "OK" button that appears twice on the screen, the solution will error stating that more than one match was found. If you expect more than one match to be found and you wish to always interact with the second match, for example, you can use the -multiple and -number parameters as explained in the below guide.

When using any of the click commands, be aware that the solution will locate the image on the screen and then click exactly in the middle of that match. Therefore, you have to be precise in your screenshots and make sure that you have the spot you wish to click on exactly in the middle of your screenshot. In case you wish to click somewhere else than in the middle, you can use the "location" command to extract the location of the match and then click based on custom coordinates.

## Installation
1. Download the [latest version](https://github.com/foxtrot-alliance/py-commands-image/releases/download/v0.0.1/py-commands-image_v0.0.1.zip).
2. Unzip the folder somewhere appropriate, we suggest directly on the C: drive for easier access. So, your path would be similar to "C:\py-commands-image_v0.0.1".
3. After unzipping the files, you are now ready to use the program. The only file you will have to be concerned about is the actual .exe file in the folder, however, all the other files are required for the solution to run properly.
4. Open Foxtrot (or any other RPA tool) to set up your action. In Foxtrot, you can utilize the functionality of the program via the DOS Command action (alternatively, the Powershell action).

## Usage
When using the program via Foxtrot, the CMD, or any other RPA tool, you need to reference the path to the program exe file. If you placed the program directly on your C: drive as recommended, the path to your program will be similar to: 
```
C:\py-commands-image_v0.0.1\py-commands-image_v0.0.1.exe
```
TIP: Make sure NOT to surround the path with quotation marks in your commands.

## Commands
All the available commands are specified [here](#all-available-parameters). Note, all parameters surrounded by [-x "X"] means that they are optional. For a more detailed description of each command, read the [detailed command description section](#detailed-command-description).

The solution offers three main commands:
* Wait for an image to appear on the screen
```
PROGRAM_EXE_PATH -command "wait" -path "X" [-wait "X"] [-grayscale "X"] [-region "X"]
```
* Find an image on the screen and click on it
```
PROGRAM_EXE_PATH -command "click" -path "X" [-region "X"] [-grayscale "X"] [-multiple "X"] [-number "X"] [-hover "X"]
```
* Find an image on the screen and return the location of it
```
PROGRAM_EXE_PATH -command "location" [-region "X"] [-grayscale "X"] [-multiple "X"] [-number "X"]
```

## Examples
```
PROGRAM_EXE_PATH -command "wait" -path "c:\image.png" -wait "60"
PROGRAM_EXE_PATH -command "click" -path "c:\image.png"
PROGRAM_EXE_PATH -command "rightclick" -path "c:\image.png" -hover "true"
PROGRAM_EXE_PATH -command "doubleclick" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
PROGRAM_EXE_PATH -command "click" -path "c:\image.png" -region "(0, 0, 1000, 1000)" -grayscale "true" -multiple "true" -number "2"
PROGRAM_EXE_PATH -command "doubleclick" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
PROGRAM_EXE_PATH -command "location" -path "c:\image.png"
```

## All available parameters
```
-command: "click"/"doubleclick"/"rightclick"/"location"/"wait", required
  This is the command you wish the solution to execute.

-path: "X", required
  This is the path to the .PNG file you wish to solution to look for.

-grayscale: "true/false", default = "false"
  This determines whether the pixel matching should be color aware. Setting this to true makes it faster.

-region: "(StartLeft, StartTop, Width, Height)", default = "(0 , 0, ScreenWidth, ScreenHeigth)"
  This determines the region of the screen you wish to scan. The smaller the region, the faster the execution.

-multiple: "ignore"/"true"/"false", default = "ignore"
  This determines whether you wish to allow that more than one match is found. If set to ignore, it will allows engage with the first one. If set to false, it will error in case more than one is detected. If set to true, make sure to consider the "-number" parameter.

-number: "X", default = "1"
  If the "-multiple" parameter is set to true, this determines which match it will engage with. They are numbered with the lowest top-pixel first.

-hover: "true/false", default = "false"
  If a click command is selected, this determines whether the mouse should remain in the position after clicking.

-wait: "X", default = "30"
  If the "wait" command is selected, this determines for how long the solution will wait for the image to appear on the screen.

-traces: "true"/"false", default = "false"
  This determines whether you wish the output to include traces, information about the execution.
```

## Detailed command description

### Wait
Parameters:
```
-command "wait" -path "X" [-wait "X"] [-grayscale "X"] [-region "X"]
```
Examples:
```
-command "wait" -path "c:\image.png"
-command "wait" -path "c:\image.png" -wait "120"
-command "wait" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
-command "wait" -path "c:\image.png" -region "(1000, 1000, 1500, 1500)" -grayscale "true"
```

### Click
Parameters:
```
-command "click" -path "X" [-region "X"] [-grayscale "X"] [-multiple "X"] [-number "X"] [-hover "X"]
```
Examples:
```
-command "click" -path "c:\image.png"
-command "click" -path "c:\image.png" -hover "true"
-command "click" -path "c:\image.png" -multiple "true" -number "2"
-command "click" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
-command "click" -path "c:\image.png" -region "(1000, 1000, 1500, 1500)" -grayscale "true"
```

### Double-click
Parameters:
```
-command "doubleclick" -path "X" [-region "X"] [-grayscale "X"] [-multiple "X"] [-number "X"] [-hover "X"]
```
Examples:
```
-command "doubleclick" -path "c:\image.png"
-command "doubleclick" -path "c:\image.png" -hover "true"
-command "doubleclick" -path "c:\image.png" -multiple "true" -number "2"
-command "doubleclick" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
-command "doubleclick" -path "c:\image.png" -region "(1000, 1000, 1500, 1500)" -grayscale "true"
```

### Right-click
Parameters:
```
-command "rightclick" -path "X" [-region "X"] [-grayscale "X"] [-multiple "X"] [-number "X"] [-hover "X"]
```
Examples:
```
-command "rightclick" -path "c:\image.png"
-command "rightclick" -path "c:\image.png" -hover "true"
-command "rightclick" -path "c:\image.png" -multiple "true" -number "2"
-command "rightclick" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
-command "rightclick" -path "c:\image.png" -region "(1000, 1000, 1500, 1500)" -grayscale "true"
```

### Location
Parameters:
```
-command "location" [-region "X"] [-grayscale "X"] [-multiple "X"] [-number "X"]
```
Examples:
```
-command "location" -path "c:\image.png"
-command "location" -path "c:\image.png" -multiple "true" -number "2"
-command "location" -path "c:\image.png" -region "(0, 0, 1000, 1000)"
-command "location" -path "c:\image.png" -region "(1000, 1000, 1500, 1500)" -grayscale "true"
```
