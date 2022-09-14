import os.path
import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter import StringVar, IntVar
from tkinter.ttk import *
from PIL import Image, ImageTk


class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.label_icon = None
        self.weather = None
        self.frameControls = None
        self.frameDetails = None
        self.frameInfo = None
        self.comboSearch = None
        self.frameSearchBar = None
        self.geometry("380x380")
        self.title("Current Weather")

        self.controller = controller
        self.bind('<Return>', self.controller.handle_button_search)

        self.varSearch = StringVar()
        self.varTemp = StringVar()
        self.varLocation = StringVar()
        self.varCondition = StringVar()
        self.varFeelsLike = StringVar()
        self.varWindSpeed = StringVar()
        self.varWindDir = StringVar()
        self.varUnits = IntVar()
        self.varIcon = StringVar()

        # Icon has to be initially set before Controller can update with the real time weather.
        self.varIcon.set("../weather_icons/64x64/day/143.png")
        script_dir = os.path.dirname(__file__)
        rel_path = self.varIcon.get()
        abs_file_path = os.path.join(script_dir, rel_path)
        weather_icon = Image.open(abs_file_path)
        self.icon_image = ImageTk.PhotoImage(weather_icon)

        self.varTemp.set("")
        self.varLocation.set("")

        self.mainframe = Frame(self)
        self.mainframe.pack()
        self.create_frame_search_bar()
        self.create_frame_info()
        self.create_frame_details()
        self.create_frame_controls()

    def create_frame_search_bar(self):
        self.frameSearchBar = Frame(self.mainframe)

        self.comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        button_search = Button(self.frameSearchBar, text="Search", command=self.controller.handle_button_search)

        self.comboSearch.bind('<KeyRelease>', self.controller.handle_combo_search)

        self.comboSearch.pack(padx=10, side=LEFT)
        button_search.pack(side=RIGHT)
        self.frameSearchBar.pack()

    def create_frame_info(self):
        self.frameInfo = Frame(self.mainframe)

        label_temp = Label(self.frameInfo, textvariable=self.varTemp)
        label_location = Label(self.frameInfo, textvariable=self.varLocation)

        self.label_icon = Label(self.frameInfo, image=self.icon_image)

        label_temp.pack(pady=5)
        label_location.pack(pady=5)
        self.label_icon.pack(pady=5)
        self.frameInfo.pack()

    def create_frame_details(self):
        self.frameDetails = Frame(self.mainframe)

        label_condition_left = Label(self.frameDetails, text='Current Condition:')
        label_feels_like_left = Label(self.frameDetails, text='Feels Like:')
        label_wind_speed_left = Label(self.frameDetails, text='Wind Speed:')
        label_wind_dir_left = Label(self.frameDetails, text='Wind Direction:')

        label_condition_right = Label(self.frameDetails, textvariable=self.varCondition)
        label_feels_like_right = Label(self.frameDetails, textvariable=self.varFeelsLike)
        label_wind_speed_right = Label(self.frameDetails, textvariable=self.varWindSpeed)
        label_wind_dir_right = Label(self.frameDetails, textvariable=self.varWindDir)

        label_condition_left.grid(row=0, column=0, pady=5, sticky=W)
        label_condition_right.grid(row=0, column=1, pady=5, sticky=E)
        label_feels_like_left.grid(row=1, column=0, pady=5, sticky=W)
        label_feels_like_right.grid(row=1, column=1, pady=5, sticky=E)
        label_wind_speed_left.grid(row=2, column=0, pady=5, sticky=W)
        label_wind_speed_right.grid(row=2, column=1, pady=5, sticky=E)
        label_wind_dir_left.grid(row=3, column=0, pady=5, sticky=W)
        label_wind_dir_right.grid(row=3, column=1, pady=5, sticky=E)
        self.frameDetails.pack()

    def create_frame_controls(self):
        self.frameControls = Frame(self.mainframe)

        radio_f = Radiobutton(self.frameControls, text='Fahrenheit', variable=self.varUnits, value=1,
                              command=self.controller.update_gui)
        radio_c = Radiobutton(self.frameControls, text='Celsius', variable=self.varUnits, value=2,
                              command=self.controller.update_gui)

        radio_c.invoke()

        radio_f.pack(side=LEFT, padx=7.5, pady=5)
        radio_c.pack(side=RIGHT, padx=7.5, pady=5)
        self.frameControls.pack()

    def main(self):
        self.mainloop()
