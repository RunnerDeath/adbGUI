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
    try:
        subprocess.check_call(f"screen\scrcpy.exe -s {device}")
    except Exception as ex:
        raise ex


def install_apk(device, file):
    result = []
    try:
        for i in range(0,len(device)):
            result.append(subprocess.getoutput(f"adb -s {device[i]} install {file}"))
    except Exception as ex:
        raise ex
    return result


def app_list(device):
    result = re.split("\t|\n", subprocess.getoutput(f'adb -s {device[0]} shell pm list packages | findstr "ru.tensor"'))
    return result


def app_list_shown(device):
    result = []
    app_list = re.split("\t|\n", subprocess.getoutput(f'adb -s {device[0]} shell pm list packages | findstr "ru.tensor"'))
    apps = {
        "ru.tensor.sbis.retail":        "Касса Релиз",
        "ru.tensor.sbis.retail.debug":  "Касса Дебаг",
        "ru.tensor.sbis.presto":        "Presto Релиз",
        "ru.tensor.sbis.presto.debug":  "Presto Дебаг",
    }
    for item in app_list:
        result.append(apps.get(item))
    return result

