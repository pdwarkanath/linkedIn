import pyautogui
import time

def easyApplyModal():
	
	#chooseRecent2Location = pyautogui.locateCenterOnScreen('ChooseRecent2.png')
	#time.sleep(0.2)
	pyautogui.click(617,467)
	#time.sleep(0.5)
	pyautogui.click(717,467)
	#submitAppLocation = pyautogui.locateCenterOnScreen('SubmitApplication.png')
	
	pyautogui.click(841, 660)
	time.sleep(0.2)

	#X2Location = pyautogui.locateCenterOnScreen('X2.png')
	
	pyautogui.click(915,111)
	time.sleep(0.2)
	pyautogui.press('browserback')

	
	"""
	uploadNew2Location = pyautogui.locateCenterOnScreen('UploadNew2.png')
	pyautogui.click(uploadNew2Location)
	
	#selectResume()
	time.sleep(1)
	pyautogui.click(282, 305)
	pyautogui.hotkey('alt','o')
	time.sleep(0.1)
	"""
	
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
	time.sleep(0.2)
	pyautogui.press('browserback')

def easyApply():
	#easyApplyLocation = pyautogui.locateCenterOnScreen('EasyApply.png')
	pyautogui.click(432,470)
	pyautogui.click(432,450)
		
	time.sleep(0.1)
	submitAppLocation = pyautogui.locateCenterOnScreen('SubmitApplication.png')
	
	if submitAppLocation == None:
		easyApplyNewPage()
	else:
		easyApplyModal()

easyApply()

"""
for i in range(3):
	x = 220
	y = 300+i*140
	pyautogui.click(x,y)
	pyautogui.click(x,y+20)
	pyautogui.click(x,y+20)
	time.sleep(0.2)
	easyApply()

"""