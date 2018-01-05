import pyautogui
import time

def easyApplyModal():
	
	#chooseRecent2Location = pyautogui.locateCenterOnScreen('ChooseRecent2.png')
	
	pyautogui.click(617,467)
	

	#uploadNew2Location = pyautogui.locateCenterOnScreen('UploadNew2.png')
	pyautogui.click(515, 549)
	
	#selectResume()
	time.sleep(0.5)
	pyautogui.click(282, 305)
	pyautogui.hotkey('alt','o')
	time.sleep(0.1)

	#submitAppLocation = pyautogui.locateCenterOnScreen('SubmitApplication.png')
	
	pyautogui.click(841, 660)
	time.sleep(0.2)

	#X2Location = pyautogui.locateCenterOnScreen('X2.png')
	
	pyautogui.click(915,111)


def easyApplyNewPage():
	#time.sleep(0.2)

	pyautogui.press('pagedown')
	time.sleep(0.2)	
	#uploadResumeLocation = pyautogui.locateCenterOnScreen('UploadResume.png')
	
	pyautogui.click(411, 444)
	
	#selectResume()
	time.sleep(1)
	pyautogui.click(282, 305)
	pyautogui.hotkey('alt','o')
	time.sleep(0.1)

	pyautogui.press('pagedown')
	
	#submitLocation = pyautogui.locateCenterOnScreen('Submit.png')
	pyautogui.click(982, 544)
	pyautogui.click(982, 554)
	pyautogui.click(982, 564)
	time.sleep(0.5)
	pyautogui.hotkey('ctrl','w')




easyApplyLocation = pyautogui.locateCenterOnScreen('EasyApply.png')
#if easyApplyLocation == None:
	#pyautogui.hotkey('ctrl','w')
#else:

pyautogui.click(432,440)
pyautogui.click(432,450)
pyautogui.click(432,460)
time.sleep(0.1)
submitAppLocation = pyautogui.locateCenterOnScreen('SubmitApplication.png')
if submitAppLocation == None:
	easyApplyNewPage()
else:
	easyApplyModal()