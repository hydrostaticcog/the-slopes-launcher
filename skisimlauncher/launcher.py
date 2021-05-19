from tkinter import *
from tkinter import ttk
import os
import subprocess
import json
import requests

with open('/home/hydrostaticcog/.sim1/release.json') as f:
    release = json.load(f)

def run():
    download_build()
    os.chdir(f"{os.path.expanduser('~')}/.local/share/the_slopes/builds")
    try:
        subprocess.check_call(["./build1"])
    except subprocess.CalledProcessError as e:
        runningne.set(str(e))

def check_for_files():
    path = os.path.join(os.path.expanduser('~'), '.local/share/the_slopes')
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)
        os.mkdir(path + '/builds')

def download_build():
    url = 'https://github.com/pyrostaticcog/hydrostaticcog.org/raw/master/stuff/raylib_test.sh'
    path = path = os.path.join(os.path.expanduser('~'), '.local/share/the_slopes/builds')
    os.chdir(path)
    if os.path.isfile(path + '/build1'): return
    build = requests.get(url)
    open(path + '/build1', 'wb').write(build.content)
    os.chmod('build1', 0o777)
    print('New Build downloaded!')


def main():
    root = Tk()
    root.title('Ski Resort Simulator')
    root.geometry('450x225')

    mainframe = ttk.Frame(root, padding=20)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    runningne = StringVar()
    ttk.Label(mainframe, textvariable=runningne).grid(column=3, row=6, sticky=N)

    ttk.Button(mainframe, text='Run', command=run).grid(column=3, row=5, sticky=N)

    ttk.Label(mainframe, text="Run Ski Sim!").grid(column=3, row=4, sticky=N)
    ttk.Label(mainframe, text=f"Game Version {release['gameVersion']} released on {release['gRDate']}").grid(column=3, row=8, sticky=N)
    ttk.Label(mainframe, text=f"Launcher Version {release['launcherVersion']} released on {release['LRDate']}").grid(column=3, row=9, sticky=N)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=10, pady=10)

    root.bind("<Return>", run)
    root.mainloop()

if __name__ == '__main__':
    check_for_files()
    main()