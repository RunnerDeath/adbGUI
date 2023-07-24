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
        subprocess.check_call(["screen\scrcpy.exe", "-s", f"{device}"])
    except Exception as ex:
        raise ex

