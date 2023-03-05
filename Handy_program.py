import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import keyboard
import os
class Hfunctions():
    @staticmethod
    def __innit__():
        None

    def increase(self):
        vol = [0.0, -1.58, -3.34, -5.33, -7.63, -10.32, -13.61, -17.82, -23.65, -33.24, -65.25]
        vol.reverse()
        audiodevice = AudioUtilities.GetSpeakers()
        audiointerface = audiodevice.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(audiointerface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        found = False
        found_index = 0
        while found == False:
            if currentVolumeDb > vol[found_index] - 0.5:
                if found_index != 10:
                    found_index += 1
                    print(found_index)
                else:
                    found = True
            else:
                found = True
        if found_index != 10:
            volume.SetMasterVolumeLevel(vol[found_index], None)
        else:
            volume.SetMasterVolumeLevel(0.0, None)

    def decrease(self):
        vol = [0.0, -1.58, -3.34, -5.33, -7.63, -10.32, -13.61, -17.82, -23.65, -33.24, -65.25]
        audiodevice = AudioUtilities.GetSpeakers()
        audiointerface = audiodevice.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(audiointerface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        found = False
        found_index = 0
        while found == False:
            if currentVolumeDb < vol[found_index] + 0.5:
                if found_index != 10:
                    found_index += 1
                    print(found_index)
                else:
                    found = True
            else:
                found = True
        if found_index != 10:
            volume.SetMasterVolumeLevel(vol[found_index], None)
        else:
            volume.SetMasterVolumeLevel(-65.25, None)

    def tab(self):
        keyboard.press_and_release('tab')

    def down_key(self):
        keyboard.press_and_release('down')

    def windows(self):
        keyboard.press_and_release('windows')

    def up(self):
        keyboard.press_and_release('up')

    def close_tab(self):
        keyboard.press_and_release('ctrl+w')

    def enter(self):
        keyboard.press_and_release('enter')

    def youtube(self):
        keyboard.press_and_release('windows+r')
        time.sleep(1)
        keyboard.write('chrome')
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('tab')
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('ctrl+t')
        time.sleep(1)
        keyboard.write('youtube.com')
        time.sleep(1)
        keyboard.press_and_release('enter')
