import PySimpleGUI as sg
from adb_functions import *


def install_error_popup():
    sg.popup("Выберите устройства для выполнения дальнейших действий", title='Список устройств пуст .')


device = []
apk_file = []
layout = [
    [sg.Text('Выбранное Android-устройства'),
     sg.InputText(key='_ACTUAL_DEVICE_',readonly=True),
     sg.Button('Очистить', key='_CLEAR_')],
    [sg.Button('Демонстрация экрана', key='_SHOW_SCREEN_')],
    [sg.Listbox(key='_DEV_LST_', values=devices_list(), size=(0, 5), enable_events=True,
                select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, auto_size_text=True),
     sg.Listbox(key='_APP_LST_', values=[], size=(30, 5), enable_events=True,
                select_mode=sg.LISTBOX_SELECT_MODE_SINGLE),
     sg.Button('Удалить приложение', key='_DELETE_')],

    [sg.Button('Выбрать APK-файл', key='_SELECT_'),
     sg.InputText(key='_APK_FILE_'),
     sg.Button('Установить APK-файл', key='_INSTALL_')]
]
window = sg.Window('Test').Layout(layout)
while True:
    event, values = window.read()
    if event == '_DEV_LST_' and len(values['_DEV_LST_']):
        window.Element('_ACTUAL_DEVICE_').Update(values['_DEV_LST_'])
        device = values['_DEV_LST_']
        window.Element('_APP_LST_').Update(app_list(device))
    if event == '_SHOW_SCREEN_':
        if len(device) == 0:
            sg.popup("Список устройств пуст. Выберите устройства для выполнения дальнейших действий")
        else:
            show_screen(device)
    if event == '_CLEAR_':
        window.Element('_ACTUAL_DEVICE_').Update('')
        device = []
    if event == '_SELECT_':
        apk_file = sg.popup_get_file(
            'APK-файл для установки',
            title='APK-файл для установки',
            file_types=(("APK Files", "*.apk"),),
            no_window=True
        )
        window.Element('_APK_FILE_').Update(apk_file)
    if event == '_INSTALL_':
        if len(device) > 0 and len(apk_file) > 0:
            r = install_apk(device, apk_file)
            for i in range(0, len(r)):
                sg.popup(f'{r[i]}', title='Информационное окно')
        else:
            install_error_popup()
    if event == '_DELETE_':
        if len(device) > 0 and len(apk_file) > 0:
            sg.popup('Surprice')
    if event == sg.WIN_CLOSED:
        break

window.Close()

