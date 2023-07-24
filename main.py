import PySimpleGUI as sg
from adb_functions import devices_list

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
    # Нажатие на кнопку из списка устройств
    if event == '_DEV_LST_' and len(values['_DEV_LST_']):
        window.Element('_ACTUAL_DEVICE_').Update(values['_DEV_LST_'])
        device = values['_DEV_LST_']
    # Нажатие на кнопку показать экран
    if event == '_SHOW_SCREEN_':
        if len(device) == und:
            sg.popup("Device list is empty")
        else:
            for i in range(len(device)):
                show_screen(device[i])

    if event == sg.WIN_CLOSED:
        break

window.Close()

