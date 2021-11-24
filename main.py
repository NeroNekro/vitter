import imageio
import PySimpleGUI as sg
import os
import webbrowser


class GUI ():
    def __init__(self):
        sg.theme('DarkAmber')
        self.layout = [
            [sg.Text('Save every X Frame:', size=(20, 1), font=("Helvetica", 15), key="text_export")],
            [sg.Input(default_text="1")],
            [sg.Text('Choose your video', size=(20, 1), font=("Helvetica", 15), key="text")],
            [sg.In(), sg.FileBrowse(file_types=(("Video Files", "*.mp4"),))],
            [sg.Button('Split', bind_return_key=True, key='split')],
            [sg.Text('TJ 2021 V1.0 Vitter https://2090s-games.de', click_submits=True, key="LINK")]]

    def start(self):
        self.window = sg.Window('Vitter - Video Splitter', self.layout)

        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            if event == 'split':
                path, filename = os.path.split(values[1])
                try:
                    os.mkdir(path + "/tmp")
                except:
                    pass
                try:
                    reader = imageio.get_reader(values[1], "ffmpeg")
                except:
                    continue
                for number, frame in enumerate(reader):
                    if number % int(values[0]) == 0:
                        imageio.imwrite(f'{path}/tmp/{number}_{filename}.jpg', frame)
            elif event == 'LINK':
                webbrowser.open_new("https://2090s-games.de")
        self.window.close


if __name__ == '__main__':
    vitter = GUI()
    vitter.start()

