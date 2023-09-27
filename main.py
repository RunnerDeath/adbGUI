import PySimpleGUI as sg
from adb_functions import *


def install_error_popup():
    sg.popup("Выберите устройства для выполнения дальнейших действий", title='Список устройств пуст .', location=(0, 0))


device = []
apk_file = []
package = []
layout = [
    [sg.Text(' Android устройство'),
     sg.InputText(key='_ACTUAL_DEVICE_', readonly=True, expand_x=True),
     sg.Button('Очистить', key='_CLEAR_')],
    [sg.Listbox(key='_DEV_LST_', values=devices_list(), size=(0, 3), enable_events=True,
                select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, auto_size_text=True),
     sg.Listbox(key='_PKG_LST_', values=[], enable_events=True,
                select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, auto_size_text=True, expand_x=True, expand_y=True),
     sg.Button('Удалить приложение', key='_DELETE_', size=(10, 2))],
    [sg.Button('Демонстрация экрана', key='_SHOW_SCREEN_', size=(20, 1))],
    [sg.Button('Выбрать APK-файл', key='_SELECT_', size=(20, 1)),
     sg.InputText(key='_APK_FILE_', readonly=True,expand_x=True)],
    [sg.Button('Установить APK-файл', key='_INSTALL_', size=(20, 1))]
]
window = sg.Window('adbGUI').Layout(layout)


def update_package_list():
    window.Element('_PKG_LST_').Update(app_list(device))


while True:
    event, values = window.read()
    if event == '_DEV_LST_' and len(values['_DEV_LST_']):
        window.Element('_ACTUAL_DEVICE_').Update(values['_DEV_LST_'])
        device = values['_DEV_LST_']
        update_package_list()
    if event == '_PKG_LST_' and len(values['_PKG_LST_']):
        package = values['_PKG_LST_']
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
            sg.popup(f'{r}', title='Информационное окно')
        else:
            install_error_popup()
    if event == '_DELETE_':
        if len(device) > 0 and len(package) > 0:
            r = uninstall_apk(device, package)
            sg.popup(f'{r}', title='Информационное окно')
            update_package_list()
        else:
            install_error_popup()
    if event == sg.WIN_CLOSED:
        break

window.Close()

