from tkinter import *
import customtkinter as ct
import sys, os, time, urllib.request
from functools import partial
patches = ["P", "S", "T"]
def CenterWindowToDisplay(Screen: ct.CTk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"
def launch(server, types):
    if server != "Tools":
        if server == "3server":
            if os.path.exists('C:/WoTLK/Cache'):
                lab = ct.CTkLabel(master=root, text=f"Deleting Cache...", font=("Arial", 15), fg_color="transparent")
                lab.place(relx=0.5, rely=0.7, anchor=S)
                os.system('rmdir /S /Q "C:\WoTLK\Cache"')
            lab = ct.CTkLabel(master=root, text=f"Updating realmlist configuration...", font=("Arial", 15), fg_color="transparent")
            lab.place(relx=0.5, rely=0.76, anchor=S)
            os.system(f'copy "C:\\WoTLK\\Data\\enUS\\{types}\\realmlist.wtf"  "C:\\WoTLK\\Data\\enUS\\"')
            lab = ct.CTkLabel(master=root, text=f"Opening Client...", font=("Arial", 15), fg_color="transparent")
            lab.place(relx=0.5, rely=0.82, anchor=S)
            root.update()
            time.sleep(0.5)
            os.startfile('C:/WoTLK/WoW.exe')
        if server == "Bradavice-Online":
            nowy = 0.7
            gm=""
            if types != "LIVE": gm = "GM"
            if os.path.exists(f'C:/BradaviceOnline{gm}/Cache'):
                lab = ct.CTkLabel(master=root, text=f"Deleting Cache...", font=("Arial", 15), fg_color="transparent")
                lab.place(relx=0.5, rely=nowy, anchor=S)
                nowy += 0.06
                os.system(f'rmdir /S /Q "C:\BradaviceOnline{gm}\Cache"')
            lab = ct.CTkLabel(master=root, text=f"Updating realmlist configuration...", font=("Arial", 15), fg_color="transparent")
            lab.place(relx=0.5, rely=nowy, anchor=S)
            nowy += 0.06
            root.update()
            os.system(f'copy "C:\\BradaviceOnline{gm}\\Data\\enUS\\{types}\\realmlist.wtf"  "C:\\BradaviceOnline{gm}\\Data\\enUS\\"')
            for p in patches:
                #if gm == "GM" and p == "H": continue
                if os.path.exists(f'C:/BradaviceOnline{gm}/Data/patch-{p}.MPQ'):
                    if int(urllib.request.urlopen(f'https://bradavice-online.cz/patches/patch-{p}.MPQ').length) != int(os.path.getsize(f'C:/BradaviceOnline{gm}/Data/patch-{p}.MPQ')):
                        lab = ct.CTkLabel(master=root, text=f"Updating patch {p}...", font=("Arial", 15), fg_color="transparent", text_color="yellow")
                        lab.place(relx=0.5, rely=nowy, anchor=S)
                        root.update()
                        os.remove(f'C:/BradaviceOnline{gm}/Data/patch-{p}.MPQ')
                        urllib.request.urlretrieve(f'https://bradavice-online.cz/patches/patch-{p}.MPQ', f'C:/BradaviceOnline{gm}/Data/patch-{p}.MPQ')
                    else:
                        lab = ct.CTkLabel(master=root, text=f"Patch {p} already updated...", font=("Arial", 15), fg_color="transparent", text_color="lime")
                        lab.place(relx=0.5, rely=nowy, anchor=S)
                        root.update()
                else:
                    lab = ct.CTkLabel(master=root, text=f"Downloading patch {p}...", font=("Arial", 15), fg_color="transparent", text_color="red")
                    lab.place(relx=0.5, rely=nowy, anchor=S)
                    root.update()
                    urllib.request.urlretrieve(f'https://bradavice-online.cz/patches/patch-{p}.MPQ', f'C:/BradaviceOnline{gm}/Data/patch-{p}.MPQ')
                nowy += 0.06
            lab = ct.CTkLabel(master=root, text=f"Opening Client...", font=("Arial", 15), fg_color="transparent")
            lab.place(relx=0.5, rely=nowy, anchor=S)
            root.update()
            time.sleep(0.5)
            os.startfile(f'C:/BradaviceOnline{gm}/Wow.exe')
    else:
        if types == "DBEditor":
            os.startfile('C:/GMWOW/WoWDatabaseEditorCore.Avalonia.exe')
        if types == "Noggit":
            os.startfile('C:/GMWOW/NOGGIT/Noggit/noggit.exe')
        if types == "TCCreator":
            os.startfile('C:/Program Files (x86)/NotCoffee418/Trinity Creator/TrinityCreator.exe')
    sys.exit()
main = {"3server": ["LIVE","DEV","NOVAK"],"Bradavice-Online": ["LIVE","GM","DEV"],"Tools": ["DBEditor","Noggit","TCCreator"]}
ct.set_appearance_mode("dark")
root = ct.CTk()
root.wm_iconbitmap("icon.ico")
root.title("WoWLauncher by Lucy")
root.geometry(CenterWindowToDisplay(root, 300, 400, root._get_window_scaling()))
text = ct.CTkLabel(master=root, text="WoWLauncher v3.1.0", font=("Arial", 20))
text.place(relx=0.5,rely=0.05,anchor=CENTER)
cury = 0.1
for i in main:
    curx = 0.25
    l = ct.CTkLabel(master=root, text=i, font=("Arial", 20))
    l.place(relx=0.5,rely=cury,anchor=N)
    for j in main[i]:
        bt2 = ct.CTkButton(master=root, text=j, width=75, height=40, command=partial(launch, i, j))
        bt2.place(relx=curx,rely=cury+0.06,anchor=N)
        curx += 0.25
    cury += 0.17
root.mainloop()