import imageio
import PySimpleGUI as sg
import os


class GUI ():
    def __init__(self):
        sg.theme('DarkAmber')
        self.layout = [
            [sg.Text('Wähle das Video aus', size=(20, 1), font=("Helvetica", 25), key="text")],
            [sg.Input(default_text="1")],
            [sg.In(), sg.FileBrowse(file_types=(("Video Files", "*.mp4"),))],
            [sg.Button('Split', bind_return_key=True, key='split')],
            [sg.Text('TJ 2021 V1.0 Vitter')]]

    def start(self):
        self.window = sg.Window('Vitter - Video Splitter', self.layout)

        # Display and interact with the Window using an Event Loop
        while True:
            event, values = self.window.read()
            # See if user wants to quit or window was closed
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            if event == 'split':
                #print(values[0])
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
        self.window.close


if __name__ == '__main__':
    vitter = GUI()
    vitter.start()

