import pyautogui
import time

def selectResume():
	time.sleep(0.5)
	resumeLocation = pyautogui.locateCenterOnScreen('Resume.png')
	print('resume location ' +str(resumeLocation))
	pyautogui.moveTo(resumeLocation)
	pyautogui.click()
	pyautogui.hotkey('alt','o')
	


def easyApplyModal():
	#time.sleep(0.1)
	chooseRecent2Location = pyautogui.locateCenterOnScreen('ChooseRecent2.png')
	print('choose recent ' +str(chooseRecent2Location))
	pyautogui.click(chooseRecent2Location)
	#time.sleep(0.2)

	uploadNew2Location = pyautogui.locateCenterOnScreen('UploadNew2.png')
	if uploadNew2Location == None:
		uploadNew2Location = pyautogui.locateCenterOnScreen('UploadNew2Highlight.png')
	print('upload new ' + str(uploadNew2Location))
	pyautogui.click(uploadNew2Location)
	
	selectResume()
	time.sleep(0.1)
	submitAppLocation = pyautogui.locateCenterOnScreen('SubmitApplication.png')
	print('submit app ' +str(submitAppLocation))
	pyautogui.click(submitAppLocation)
	time.sleep(0.2)

	X2Location = pyautogui.locateCenterOnScreen('X2.png')
	print('x2 location ' +str(X2Location))
	pyautogui.click(X2Location)


def easyApplyNewPage():
	time.sleep(0.2)

	pyautogui.press('pagedown')
	time.sleep(0.2)
	uploadResumeLocation = pyautogui.locateCenterOnScreen('UploadResume.png')
	print('upload resume ' + str(uploadResumeLocation))
	pyautogui.click(uploadResumeLocation)

	selectResume()
	pyautogui.press('pagedown')
	time.sleep(0.2)
	submitLocation = pyautogui.locateCenterOnScreen('Submit.png')
	print('submit loc' + str(submitLocation))
	pyautogui.click(submitLocation)
	time.sleep(0.5)
	pyautogui.hotkey('ctrl','w')




easyApplyLocation = pyautogui.locateCenterOnScreen('EasyApply.png')
print('easy apply location ' +str(easyApplyLocation))
pyautogui.click(easyApplyLocation)
time.sleep(0.1)
submitAppLocation = pyautogui.locateCenterOnScreen('SubmitApplication.png')
if submitAppLocation == None:
	easyApplyNewPage()
else:
	easyApplyModal()