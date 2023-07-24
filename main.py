import PySimpleGUI as sg
import subprocess, re
from adb_functions import devices_list
def show_screen(device):
    subprocess.check_call(["screen\scrcpy.exe", "-s", f"{device}"])
device = []
layout = [
    [sg.Text('Выбранные Android-устройства'), sg.InputText(key='_ACTUAL_DEVICE_',readonly=True)],
    [sg.Listbox(key='_DEV_LST_' ,values=devices_list(),size=(0,5),
                enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED),
     sg.Button('Show Screen', key='_SHOW_SCREEN_')],
    []
]
window = sg.Window('Test').Layout(layout)
while True:
    event, values = window.read()
    if event == '_DEV_LST_' and len(values['_DEV_LST_']):
        window.Element('_ACTUAL_DEVICE_').Update(values['_DEV_LST_'])
        device = values['_DEV_LST_']

    if event == '_SHOW_SCREEN_':
        if len(device) == 0:
            sg.popup("Device list is empty")
        else:
            show_screen(device[0])

    if event == sg.WIN_CLOSED:
        break

window.Close()
def devices_list():
    result = []
    # Обрезаем лишние символы
    data = re.split("\t|\n", subprocess.getoutput('adb devices'))
    for i in range(len(data)):
        if data[i] != 'device' and data[i] != 'List of devices attached' and data[i] != '' and data[i] !='offline':
            result.append(data[i])
    return result
