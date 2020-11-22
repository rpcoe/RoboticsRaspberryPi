import config

from guizero import App, Text

app = App(title="User Interface", bg="black", width=config.displayWidth, height=config.displayHeight)
#title = Text(app, 'Speed:', grid=[0, 0])
#text = Text(app, "xx", grid=[1, 0])

def loop():
    #check json file and change values

def start():
    print('starting ui')

app.display()

#app = App(title='Sensor Display!', height=100, width=200, layout='grid')
