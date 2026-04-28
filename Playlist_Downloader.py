import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
from Main import Transfer_Process
import threading

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)
        self.geometry("500x500")
        self.title("Playlist Transfer")

        self.container = ctk.CTkFrame(self, fg_color='transparent')
        self.container.pack(fill='both', expand=True)

        self.show_landing_page()
    def clear_view(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_landing_page(self):

        label = ctk.CTkLabel(self.container, text='Welcome', font=('Arial', 70))
        label.pack(pady=20)

        label2 = ctk.CTkLabel(self.container, text='Please select a service', font=('Arial', 40))
        label2.pack(pady=30)

        img = Image.open("Spotify_Youtube.png")

        button = ctk.CTkButton(self.container, 
                               width=200, 
                               height=200,
                                text="", 
                                image=CTkImage(dark_image=img, light_image=img, size=(200,200)),
                                fg_color= "transparent",
                                hover_color="#0B5324",
                                command=self.show_spotify_prompt)

        button.pack(pady=1)

    def show_spotify_prompt(self):
        self.clear_view()
        header = ctk.CTkLabel(self.container, text='Spotify Credentials', font=('Arial', 30))
        header.pack(pady=20)

        self.client_id = ctk.CTkEntry(self.container, placeholder_text="Please add your Spotify Client ID", width=300)
        self.client_id.pack(pady=10)

        
        self.client_secret = ctk.CTkEntry(self.container, placeholder_text="Please add your Spotify Client Secret", width=300, show="*")
        self.client_secret.pack(pady=10)

        readyButton = ctk.CTkButton(self.container, text='Done', command=self.show_youtube_prompt)
        readyButton.pack(pady=20)

    def show_youtube_prompt(self):
        self.cid = self.client_id.get()
        self.sec = self.client_secret.get()

        self.clear_view()
        header = ctk.CTkLabel(self.container, text="Youtube Credentials", font=('Arial', 30))
        header.pack(pady=20)

        self.drop_label = ctk.CTkLabel(self.container, text="Drag JSON here\or click to browse :D", width = 300, height=150, fg_color="#2b2b2b", corner_radius=10)
        self.drop_label.pack(pady = 20)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.handle_drop)

        self.drop_label.bind("<Button-1>", lambda e: self.browse_file())

        self.finish_btn = ctk.CTkButton(self.container, text="Next", state="disabled", fg_color="green", 
                                       command=self.Spotify_URL)
        self.finish_btn.pack(pady=10)

    def handle_drop(self, event):
        file_path = event.data.strip("{}")
        if file_path.endswith(".json"):
            self.json_path = file_path
            self.drop_label.configure(text=f"Loaded:\n{os.path.basename(file_path)}", text_color="green")
            self.finish_btn.configure(state="normal")

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.json_path = file_path
            self.drop_label.configure(text=f"Loaded:\n{os.path.basename(file_path)}", text_color="green")
            self.finish_btn.configure(state="normal")

    def Spotify_URL(self):

        self.clear_view()

        self.url_entry = ctk.CTkEntry(self.container, placeholder_text="Paste Spotify Playlist URL", width=400)
        self.url_entry.pack(pady=20)
        
        self.finish_btn = ctk.CTkButton(self.container, text="Process Transfer", fg_color="green", 
                                        command=self.run_backend)
        self.finish_btn.pack(pady=10)


    def run_backend(self):
        s_id = self.cid
        s_secret = self.sec
        y_json = self.json_path

        target_url = self.url_entry.get()

        if not target_url:
            return 
        
        self.finish_btn.configure(text = "Transferring...", state = "disabled")

        threading.Thread(target=self.threaded_process, args=(s_id, s_secret, y_json, target_url), daemon=True).start()

    def threaded_process(self, s_id, s_secret, y_json, target_url):
        
        try:
            Transfer_Process(s_id, s_secret, y_json, target_url)

            self.after(0, self.show_success)

        except Exception as e:
            self.drop_label = ctk.CTkLabel(self.container, 
                                           text=f"Error: {e}", 
                                           font = ('Arial', 50),
                                           text_color="red")
        
            self.drop_label.pack(pady = 10)
            self.finish_btn.configure(text='retry', state="normal")

    def show_success(self):
        self.clear_view()
        success_label = ctk.CTkLabel(self.container, 
                                     text="Success! :D", 
                                     font=('Arial', 50), 
                                     text_color="green")
        success_label.pack(expand=True)

if __name__ == '__main__':
    app = App() 
    app.mainloop()
