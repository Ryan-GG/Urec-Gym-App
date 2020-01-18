#Authors Ryan Gross, Matthew Young
#Date 12/14/13
#GymProgram: Gym trainer for JMU students that go to UREC

import kivy
from kivy.app import App
from kivy.base import runTouchApp
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
import sqlite3


screen_manager = ScreenManager()

#These two classes create the backbone of program to manage the screens
#and run the main Kivy code for the program


class ScreenManagerApp(App):
    def build(self):
        return root_widget

class MyScreenManager(ScreenManager):
    pass

#All of these classes create the screens the user sees when they run the program
#Some Contain the load_from_difficult function which gets the corresponding data from our database

class CardioDirectory(Screen):
    pass

class MacDirectory(Screen):
    pass

class PoolDirectory(Screen):
    pass

class Main_Screen(Screen):
   difficult = StringProperty()

class Urec_facilities(Screen):
   pass

class AdventureDirectory(Screen):
   pass

class BoulderingDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Bouldering' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())

class TopRopeDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Top Rope' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())

class CyclingDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Cycles' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())

class EllipticalDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Elliptical' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())
class RunningTrackDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Running Track' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())
        
class BasketballDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Basketball' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())
class RaquetballDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Raquetball' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())
class FitnessCenterDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Fitness Studio' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())

class RecSwimmingDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Recreational Swimming' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())
class LapsDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Laps' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())
class VolleyballBballDirectory(Screen):
    rows = StringProperty("")

    def load_from_difficult(self, difficult):
        connection = sqlite3.connect("workoutData.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM workoutData WHERE Activity = 'Water Sports' and Difficulty = ?", (difficult,))
        self.rows = str(cursor.fetchall())



#This is the main widget that contains all of the code to show the visual representation of the program
#Screens are broken down into directorys with buttons,labels, and more to let the user move around the program and acess data


root_widget = Builder.load_string("""

ScreenManager:
    Main_Screen:
        name: 'mainScreen'
        on_difficult: bouldering.load_from_difficult(self.difficult)
        on_difficult: TopRope.load_from_difficult(self.difficult)
        on_difficult: Cycling.load_from_difficult(self.difficult)
        on_difficult: Elliptical.load_from_difficult(self.difficult)
        on_difficult: Running.load_from_difficult(self.difficult)
        on_difficult: Swimming.load_from_difficult(self.difficult)
        on_difficult: VolleyballBball.load_from_difficult(self.difficult)
        on_difficult: Laps.load_from_difficult(self.difficult)
        on_difficult: Basketball.load_from_difficult(self.difficult)
        on_difficult: RaquetBall.load_from_difficult(self.difficult)
        on_difficult: FC.load_from_difficult(self.difficult)
    Urec_facilities:
        name: 'urecFac'
    AdventureDirectory:
        name: 'AdventureDirectory'
    BoulderingDirectory:
        id: bouldering
        difficult: 'Beginner'
        name: 'BoulderingDirectory'
    TopRopeDirectory:
        id: TopRope
        difficult: 'Beginner'
        name: 'TopRopeDirectory'



    CardioDirectory:
        name: 'CardioDirectory'
    CyclingDirectory:
        id: Cycling
        difficult: 'Beginner'
        name: 'CyclingDirectory'
    EllipticalDirectory:
        id: Elliptical
        difficult: 'Beginner'
        name: 'EllipticalDirectory'
    RunningTrackDirectory:
        id: Running
        difficult: 'Beginner'
        name: 'RunningTrackDirectory'


            
    MacDirectory:
        name: 'MacDirectory'
    BasketballDirectory:
        id: Basketball
        difficult: 'Beginner'
        name: 'BasketballDirectory'
    RaquetballDirectory:
        id: RaquetBall
        difficult: 'Beginner'
        name: 'RaquetballDirectory'
    FitnessCenterDirectory:
        id: FC
        difficult: 'Beginner'
        name: 'FitnessCenterDirectory'


    PoolDirectory:
        name: 'PoolDirectory'
    RecSwimmingDirectory:
        id: Swimming
        difficult: 'Beginner'
        name: 'RecSwimmingDirectory'
    VolleyballBballDirectory:
        id: VolleyballBball
        difficult: 'Beginner'
        name: 'VolleyballBballDirectory'
    LapsDirectory:
        id: Laps
        difficult: 'Beginner'
        name: 'LapsDirectory'
    
    

<Main_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "mainScreenImage.png"

    Label:
        text: "Select your dificulty"
        font_size: 50
        color: (0.9,0.8,0,1)
        background_color: (0,0,0,0)
        pos_hint: {"x": 0, "y": 0.20}

    Button:
        text: 'Beginner'
        font_size: 30
        size_hint: 0.2,0.2
        color: (0.9,0.8,0,1)
        background_color: (0,0,0,0)
        pos_hint: {"x": 0.16, "y": 0.1}
        on_release:
            root.difficult =  "Beginner"
            app.root.current = 'urecFac'

    Button:
        text: 'Intermediate'
        font_size: 30
        size_hint: 0.2,0.2
        color: (0.9,0.8,0,1)
        background_color: (0,0,0,0)
        pos_hint: {"x": 0.41, "y": 0.1}
        on_release:
            root.difficult = "Intermediate"
            app.root.current = 'urecFac'

    Button:
        text: 'Advanced'
        font_size: 30
        size_hint: 0.2,0.2
        color: (0.9,0.8,0,1)
        background_color: (0,0,0,0)
        pos_hint: {"x": 0.66, "y": 0.1}
        on_release:
            root.difficult = "Advanced"
            app.root.current = 'urecFac'
            



                
<Urec_facilities>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Adventure Center"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "adventureCenterImage.jpg"
            on_release: app.root.current = "AdventureDirectory"
        Button:
            text: "Cardio Deck"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "cardioDeckImage.jpg"
            on_release: app.root.current = "CardioDirectory"
        Button:
            background_normal: "miscActivityCenters.jpg"
            text: "Miscellanious Activity Centers"
            font_size: 50
            color: (0.9,0.8,0,1)
            on_release: app.root.current = "MacDirectory"
        Button:
            background_normal: "multiActivityPool.jpeg"
            text: "Multi-Activity Pool"
            font_size: 50
            color: (0.9,0.8,0,1)
            on_release: app.root.current = "PoolDirectory"
        Button:
            background_normal: "mainScreenImage.png"
            text: "Back"
            font_size: 50
            color: (0.9,0.8,0,1)
            on_release: app.root.current = "mainScreen"

<AdventureDirectory>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Bouldering"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "boulderingImages.jpg"
            on_release:
                app.root.current = "BoulderingDirectory"
        Button:
            text: "Top Rope"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "adventureCenterImage.jpg"
            on_release:
                app.root.current = "TopRopeDirectory"
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "urecFac"

<BoulderingDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
            
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "AdventureDirectory"

<TopRopeDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "AdventureDirectory"

<CardioDirectory>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Cycles"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "cyclesImagejpeg.jpeg"
            on_release:
                app.root.current = "CyclingDirectory"
        Button:
            text: "Ellipticals"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "ellipticalsImage.jpg"
            on_release:
                app.root.current = "EllipticalDirectory"
        Button:
            text: "Running Track"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "trackImage.jpg"
            on_release:
                app.root.current = "RunningTrackDirectory"
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "urecFac"


<CyclingDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "CardioDirectory"

<EllipticalDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "CardioDirectory"


<RunningTrackDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "CardioDirectory"
                

<MacDirectory>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Basketball"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "basketballImage.jpg"
            on_release: app.root.current = "BasketballDirectory"
        Button:
            text: "Racquetball"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "racquetballImage.jpg"
            on_release: app.root.current = "RaquetballDirectory"
        Button:
            text: "Fitness Studios"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "FCImage.jpeg"
            on_release: app.root.current = "FitnessCenterDirectory"
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "urecFac"



<BasketballDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "MacDirectory"

<RaquetballDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "MacDirectory"

<FitnessCenterDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "MacDirectory"



<PoolDirectory>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Recreational Swimming"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "volleyBballImage.jpg"
            on_release:
                app.root.current = "RecSwimmingDirectory"
        Button:
            text: "Volleyball/Basketball"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "volleyBballImage.jpg"
            on_release:
                app.root.current = "VolleyballBballDirectory"
        Button:
            text: "Laps"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_normal: "lapsImage.jpg"
            on_release:
                app.root.current = "LapsDirectory"
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "urecFac"


<RecSwimmingDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "PoolDirectory"

<VolleyballBballDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "PoolDirectory"

<LapsDirectory>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.rows
            text_size: (root.width - 175), None
        Button:
            text: "Go back"
            font_size: 50
            color: (0.9,0.8,0,1)
            background_color: (0,0,0,1)
            on_release:
                app.root.current = "PoolDirectory"

""")



screen_manager.add_widget(Main_Screen(name = "mainScreen"))
screen_manager.add_widget(Urec_facilities(name = "urecFac"))
screen_manager.add_widget(AdventureDirectory(name = "AdventureDirectory"))
screen_manager.add_widget(CardioDirectory(name = "CardioDirectory"))
screen_manager.add_widget(MacDirectory(name = "MacDirectory"))
screen_manager.add_widget(PoolDirectory(name = "PoolDirectory"))
screen_manager.add_widget(BoulderingDirectory(name = "BoulderingDirectory"))
screen_manager.add_widget(TopRopeDirectory(name = "TopRopeDirectory"))
screen_manager.add_widget(CyclingDirectory(name = "CyclingDirectory"))
screen_manager.add_widget(EllipticalDirectory(name = "EllipticalDirectory"))
screen_manager.add_widget(RunningTrackDirectory(name = "RunningTrackDirectory"))
screen_manager.add_widget(RecSwimmingDirectory(name = "RecSwimmingDirectory"))
screen_manager.add_widget(LapsDirectory(name = "LapsDirectory"))
screen_manager.add_widget(VolleyballBballDirectory(name = "VolleyballBballDirectory"))
screen_manager.add_widget(BasketballDirectory(name = "BasketballDirectory"))
screen_manager.add_widget(RaquetballDirectory(name = "RaquetballDirectory"))
screen_manager.add_widget(FitnessCenterDirectory(name = "FitnessCenterDirectory"))








ScreenManagerApp().run()



    
