import sys
import os
import pyautogui
import datetime
import time
import traceback


def retrieve_project_parameters():
    
    parameters = sys.argv

    parameters_number = parameters.index("-traces") if "-traces" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        traces = parameters[parameters_number]
    else:
        traces = ""

    parameters_number = parameters.index("-command") if "-command" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        command = parameters[parameters_number]
    else:
        command = ""

    parameters_number = parameters.index("-path") if "-path" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        path = parameters[parameters_number]
    else:
        path = ""

    parameters_number = parameters.index("-grayscale") if "-grayscale" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        grayscale = parameters[parameters_number]
    else:
        grayscale = ""

    parameters_number = parameters.index("-region") if "-region" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        region = parameters[parameters_number]
    else:
        region = "(0 , 0, " + str(pyautogui.size().width) + ", " + str(pyautogui.size().height) + ")"

    parameters_number = parameters.index("-multiple") if "-multiple" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        multiple = parameters[parameters_number]
    else:
        multiple = ""

    parameters_number = parameters.index("-number") if "-number" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        number = parameters[parameters_number]
    else:
        number = "1"

    parameters_number = parameters.index("-wait") if "-wait" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        wait = parameters[parameters_number]
    else:
        wait = "30"

    parameters_number = parameters.index("-hover") if "-hover" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        hover = parameters[parameters_number]
    else:
        hover = ""
        
    return {
        "traces": traces,
        "command": command,
        "path": path,
        "grayscale": grayscale,
        "region": region,
        "multiple": multiple,
        "number": number,
        "wait": wait,
        "hover": hover,
    }


def validate_project_parameters(parameters):
    
    traces = parameters["traces"]
    command = parameters["command"]
    path = parameters["path"]
    grayscale = parameters["grayscale"]
    region = parameters["region"]
    multiple = parameters["multiple"]
    number = parameters["number"]
    wait = parameters["wait"]
    hover = parameters["hover"]
    
    if traces == "" or traces.upper() == "FALSE":
        traces = False
    elif traces.upper() == "TRUE":
        traces = True
    else:
        return "ERROR: Invalid traces parameter! Parameter = " + str(traces)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Parameters retrieved start * ===")

    if command.upper() == "CLICK":
        command = "CLICK"
    elif command.upper() == "DOUBLECLICK":
        command = "DOUBLECLICK"
    elif command.upper() == "RIGHTCLICK":
        command = "RIGHTCLICK"
    elif command.upper() == "LOCATION":
        command = "LOCATION"
    elif command.upper() == "WAIT":
        command = "WAIT"
    else:
        return "ERROR: Invalid command parameter! Parameter = " + str(command)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tCommand = " + str(command))

    pathexists = os.path.isfile(path)
    if pathexists:
        if not path.upper().endswith(".PNG"):
            return "ERROR: The image file is not PNG!"
    else:
        return "ERROR: The image file was not found!"

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tPath = " + str(path))

    if grayscale == "" or grayscale.upper() == "FALSE":
        grayscale = False
    elif grayscale.upper() == "TRUE":
        grayscale = True
    else:
        return "ERROR: Invalid grayscale parameter! Parameter = " + str(grayscale)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tGrayscale = " + str(grayscale))

    try:
        region = eval(region)
    except:
        return "ERROR: Invalid region parameter! Parameter = " + str(region)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tRegion = " + str(region))

    if multiple == "" or multiple.upper() == 'IGNORE':
        multiple = 'IGNORE'
    elif multiple.upper() == "FALSE":
        multiple = False
    elif multiple.upper() == "TRUE":
        multiple = True
    else:
        return "ERROR: Invalid multiple parameter! Parameter = " + str(multiple)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tMultiple = " + str(multiple))

    if number == "":
        number = 0
    elif number.isdigit():
        number = int(number) - 1
    else:
        return "ERROR: Invalid number parameter! Parameter = " + str(number)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tNumber = " + str(number + 1))

    if wait.isdigit():
        wait = int(wait)
    elif command.upper() == "WAIT":
        return "ERROR: Invalid wait parameter! Parameter = " + str(wait)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tWait = " + str(wait))

    if hover == "" or hover.upper() == "FALSE":
        hover = False
    elif hover.upper() == "TRUE":
        hover = True
    else:
        return "ERROR: Invalid hover parameter! Parameter = " + str(hover)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tHover = " + str(hover))

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Parameters retrieved end * ===")
        
    return {
        "traces": traces,
        "command": command,
        "path": path,
        "grayscale": grayscale,
        "region": region,
        "multiple": multiple,
        "number": number,
        "wait": wait,
        "hover": hover,
    }


def execute_command(parameters):
    
    try:
        traces = parameters["traces"]
        command = parameters["command"]
        path = parameters["path"]
        grayscale = parameters["grayscale"]
        region = parameters["region"]
        multiple = parameters["multiple"]
        number = parameters["number"]
        wait = parameters["wait"]
        hover = parameters["hover"]

        location = None
        
        if "WAIT" not in command.upper():

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Locating image start * ===")
                
            if multiple == 'IGNORE':
                
                location = pyautogui.locateOnScreen(path, grayscale=grayscale, region=region)

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\t" + " Image located succesfully.")
                
            else:

                location = list(pyautogui.locateAllOnScreen(path, grayscale=grayscale, region=region))

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\t" + str(len(location)) + " image(s) located succesfully.")

                if len(location) >= 2 and multiple is False:
                    return "ERROR: Multiple image matches found!"

                if (len(location) - 1) >= number and number >= 0:
                    location = location[number]

                    if traces is True:
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tImage number " + str(number + 1) + " selected to work with.")

                else:
                    return "ERROR: The specified image number parameter " + str(number) + " is not valid compared to the number of images found = " + str(len(location))

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Locating image end * ===")

            if "CLICK" in command.upper():

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform click command start * ===")

                mouse_location_x, mouse_location_y = pyautogui.position()

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tCurrent location of the mouse = " + str(pyautogui.position()))
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to perform click...")

                if command.upper() == "CLICK":
                    pyautogui.click(pyautogui.center(location))

                elif command.upper() == "DOUBLECLICK":
                    pyautogui.doubleClick(pyautogui.center(location))

                elif command.upper() == "RIGHTCLICK":
                    pyautogui.rightClick(pyautogui.center(location))

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tClick completed!")
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform click command end * ===")

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Move mouse back to original position start * ===")

                if hover is False:
                    if traces is True:
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to move mouse back to position...")

                    pyautogui.moveTo(mouse_location_x, mouse_location_y)

                    if traces is True:
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tMoving mouse back to position complete!")

                else:
                    if traces is True:
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tHovering mouse activated, therefore, do NOT move mouse back in position")

                if traces is True:
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Move mouse back to original position end * ===")
                    
            elif "LOCATION" in command.upper():
                print(f"IMAGE LOCATION: {str(location)}")

        else:

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Calculating wait time start * ===")
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tWait time set to " + str(wait) + " seconds.")

            wait = time.time() + wait

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tTimeout set to = " + str(wait))
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Calculating wait time end * ===")

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Locating image start * ===")

            while location is None and time.time() < wait:
                try:
                    time.sleep(0.5)

                    if traces is True:
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tAttempting to locate image...")

                    location = pyautogui.center(pyautogui.locateOnScreen(path, grayscale=grayscale, region=region))
                except:
                    continue

            if location is None:
                return("ERROR: Image not found on the screen!")

            if traces is True:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Locating image end * ===")
    
    except:
        print(traceback.format_exc())
        return "ERROR: Unexpected issue!"
    
    return True


def main():
    
    parameters = retrieve_project_parameters()
    
    parameters = validate_project_parameters(parameters)
    if not isinstance(parameters, dict):
        print(str(parameters))
        return
    
    valid = execute_command(parameters)
    if not valid is True:
        print(str(valid))
        return
    
    print("SUCCESS")
    
    
if __name__ == "__main__":
    main()
