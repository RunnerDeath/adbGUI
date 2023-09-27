import subprocess
import re


def devices_list():
    result = []
    # Обрезаем лишние символы
    data = re.split("\t|\n", subprocess.getoutput('adb devices'))
    for i in range(len(data)):
        if data[i] != 'device' and data[i] != 'List of devices attached' and data[i] != '' and data[i] != 'offline':
            result.append(data[i])
    return result


def show_screen(device):
    if len(device) > 1:
        raise 'Функционал находиться в разработке'
    try:
        subprocess.check_call(f"screen\scrcpy.exe -s {device[0]}")
    except Exception as ex:
        raise ex


def install_apk(device, file):
    try:
        result = subprocess.getoutput(f"adb -s {device[0]} install {file}")
    except Exception as ex:
        raise ex
    return result


def uninstall_apk(device, package):
    result = []
    try:
        result = subprocess.getoutput(f"adb -s {device[0]} uninstall {package[0]}")
    except Exception as ex:
        raise ex
    return result


def app_list(device):
    result = []
    data = re.split("\t|\n", subprocess.getoutput(f'adb -s {device[0]} shell pm list packages | findstr "ru.tensor"'))
    try:
        for i in data:
            i = i.split(':')
            result.append(i[1])
    except:
        return result
    return result


def app_list_shown(device):
    result = []
    a = app_list(device)
    apps = {
        "ru.tensor.sbis.retail":        "Касса Релиз",
        "ru.tensor.sbis.retail.debug":  "Касса Дебаг",
        "ru.tensor.sbis.presto":        "Presto Релиз",
        "ru.tensor.sbis.presto.debug":  "Presto Дебаг",
        "ru.tensor.sbis.appmarket":     "Магазин приложений Релиз",
        "ru.tensor.sbis.appmarket.debug": "Магазин приложений Дебаг",
        "ru.tensor.sbis.waiter": "Официант Релиз",
        "ru.tensor.sbis.waiter.debug": "Официант Дебаг",
    }
    for item in a:
        result.append(apps.get(item))
    return result

