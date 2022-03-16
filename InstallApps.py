#########################
##   StartUp Options   ##
#########################

skipModuleInstall = False
    # If "True", this skips the module install (see the required modules section)                                        | Recommended Option: False
hideLoadingBars = False
    # If "True", this will hide all loading bars, with the exception of downloads.                                       | Recommended Option: False

################
##   Signal   ##
################

def main():

    #################
    ##   Imports   ##
    #################

    import os

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    cls()

    print('Importing Modules. This may take some time.')

    #######  Required Modules

    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'prompt_toolkit'])

    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'wget'])

    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'termcolor'])
                
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'progress'])

    ####### Other Modules

    import prompt_toolkit
    from prompt_toolkit import prompt
    import webbrowser
    import wget
    import getpass
    import zipfile
    import platform
    from os.path import exists
    from time import sleep
    from progress.bar import Bar
    import termcolor
    from termcolor import colored

    ####### Loading Bar

    if hideLoadingBars == False:
        print(colored('INITIALIZING', 'yellow'))
        with Bar('Loading', fill='█', suffix='%(percent).1f%% - %(eta)ds') as bar:
                for i in range(100):
                    sleep(0.01)
                    bar.next()

    cls()

    ###################
    ##   Functions   ##
    ###################

    def Games():
        user = getpass.getuser()
        url = (f'https://download1522.mediafire.com/hn45b03jj3zg/fehlz39edzzcjqi/Games.zip')
        path = (f'/Users/{user}/Downloads/Games.zip')
        path2 = (f'/Users/{user}/Downloads/')
        wget.download(url, path)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path2)
        os.remove(path)
        print(" ")
        print(colored("Done! Check your", 'yellow'), colored('DOWNLOADS', 'red'), colored('folder.', 'yellow'))
        currentplatform = platform.system()
        if currentplatform == 'Windows':
            os.system("pause")
        else:
            os.system('read -s -n 1 -p "Press any key to continue..."')
            print()
        cls()
        Openingprompt()

    def Apps():
        user = getpass.getuser()
        url = (f'https://download1323.mediafire.com/gdc4zoouh8mg/u2692w5cyhnyaur/Apps.zip')
        path = (f'/Users/{user}/Downloads/Apps.zip')
        path2 = (f'/Users/{user}/Downloads/')
        wget.download(url, path)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path2)
        os.remove(path)
        print(" ")
        print(colored("Done! Check your", 'yellow'), colored('DOWNLOADS', 'red'), colored('folder.', 'yellow'))
        currentplatform = platform.system()
        if currentplatform == 'Windows':
            os.system("pause")
        else:
            os.system('read -s -n 1 -p "Press any key to continue..."')
            print()
        cls()
        Openingprompt()

    def Utilities():
        user = getpass.getuser()
        url = (f'https://download1515.mediafire.com/setes6gp2xpg/7jj24y89bwi5pte/Utilities.zip')
        path = (f'/Users/{user}/Downloads/Utilities.zip')
        path2 = (f'/Users/{user}/Downloads/')
        wget.download(url, path)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path2)
        os.remove(path)
        print(" ")
        print(colored("Done! Check your", 'yellow'), colored('DOWNLOADS', 'red'), colored('folder.', 'yellow'))
        currentplatform = platform.system()
        if currentplatform == 'Windows':
            os.system("pause")
        else:
            os.system('read -s -n 1 -p "Press any key to continue..."')
            print()
        cls()
        Openingprompt()

    def Dev():
        user = getpass.getuser()
        url = (f'https://download1587.mediafire.com/f9y1p3by03ng/7aslkv3zjzq7nkh/Development.zip')
        path = (f'/Users/{user}/Downloads/Development.zip')
        path2 = (f'/Users/{user}/Downloads/')
        wget.download(url, path)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path2)
        os.remove(path)
        print(" ")
        print(colored("Done! Check your", 'yellow'), colored('DOWNLOADS', 'red'), colored('folder.', 'yellow'))
        currentplatform = platform.system()
        if currentplatform == 'Windows':
            os.system("pause")
        else:
            os.system('read -s -n 1 -p "Press any key to continue..."')
            print()
        cls()
        Openingprompt()

    def AllApps():
        user = getpass.getuser()
        url = (f'https://download1079.mediafire.com/bii2t2uvqlng/c1h98zkbnqt13yz/AllApps.zip')
        path = (f'/Users/{user}/Downloads/AllApps.zip')
        path2 = (f'/Users/{user}/Downloads/')
        wget.download(url, path)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path2)
        os.remove(path)
        print(" ")
        print(colored("Done! Check your", 'yellow'), colored('DOWNLOADS', 'red'), colored('folder.', 'yellow'))
        currentplatform = platform.system()
        if currentplatform == 'Windows':
            os.system("pause")
        else:
            os.system('read -s -n 1 -p "Press any key to continue..."')
            print()
        cls()
        Openingprompt()

    def Openingprompt():
        print(colored('Welcome to M4X4s App Downloader, A python script for people to download some everyday applications and games. Usually used for recovering apps during a clean install.', 'yellow'))
        print(colored("---------------------------", 'cyan'))
        print(colored('Py', 'blue'), colored('Script', 'yellow'), colored('|', 'blue'), colored('by M4X4#6494', 'green'))
        print(colored("---------------------------", 'cyan'))
        print(colored("Don't know where to get started?", 'blue'))
        print(colored("Choose something from the list below.", 'blue'))
        print(colored("----------------------------------------------------------------------------------------------------", 'cyan'))
        print(colored("     1", 'cyan'), ("    >>     All Apps                            "))
        print(colored("     2", 'cyan'), ("    >>     Games                               "))
        print(colored("     3", "cyan"), ("    >>     General Applications                "))
        print(colored("     4", "cyan"), ("    >>     Utilities                           "))
        print(colored("     6", "cyan"), ("    >>     Development                         "))
        print(colored("----------------------------------------------------------------------------------------------------", 'cyan'))
        while True:
            text = prompt('Option # >> ')

            ########################
            ##   Call Functions   ##
            ########################

            if text == "1":
                AllApps()
            elif text == "2":
                Games()
            elif text == "3":
                Apps()
            elif text == "4":
                Utilities()
            elif text == "5":
                Dev()
            elif text == "cls":
                cls()
                Openingprompt()
            else:
                print(colored('Syntax Error: Unknown Option "','red'), colored(text,'cyan'), colored('"', 'red'))

    #############
    ##  Main   ##
    #############

    Openingprompt()

######################
##   Script Check   ##
######################

if __name__ == '__main__':
    main()