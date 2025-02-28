from playsound import playsound
import tkinter as tk
from tkinter import filedialog
import os


root=tk.Tk()
root.withdraw()

dirname = os.path.dirname(__file__)
ammumu=os.path.join(dirname , "songs\\ammumu.mp3")
jojo=os.path.join(dirname , "songs\jojo.mp3")
class Stack:
    def __init__(self):
        self.list=[]
    
    def Add_Song(self,val):
            self.list.append(val)

    def peek(self):
        return self.list[len(self.list)-1]
    
    def get_file_path(self):
        return filedialog.askopenfilename(title="Please select a song")
    
    def pop(self):
        if self.list==[]:
            print(f" stack is empty")
        else:
            self.list.pop()

Playlist=Stack()
Playlist.Add_Song(ammumu)
Playlist.Add_Song(jojo)
def play_Song(ll):
    while True:
        print(f"Press 1 to play First Song\n Press 2 to Play Next Song.\n Press 3 to Add Song.\n Press 4 to Delete Current Song. \n Press 5 to Show Playlist \n Press 0 to Exit Music Player")
        choice=int(input())
        for i in ll.list:
            if choice==1:
                print(f"Playing song located at {ll.list[len(ll.list)-1]}")
                playsound(ll.peek())
                break
            elif choice==2:
                if ll.list==[]:
                    print("Playlist is Empty")
                    break
                else:
                    ll.pop()
                    print(f"Playing song located at {ll.list[len(ll.list)-1]}")
                    playsound(ll.list[len(ll.list)-1])
                    break
            elif choice==3:
                root.deiconify()
                root.title("Choose dialog")
                ll.Add_Song(ll.get_file_path())
                # root.destroy()
                root.withdraw()
                break
            elif choice==4:
                ll.list.pop()
            elif choice==5:
                print(i)
            elif choice==0:
                root.destroy()
                return
            else:
                root.destroy()
                print("Invalid Input")
                return

play_Song(Playlist)
