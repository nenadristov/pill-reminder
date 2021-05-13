if api.isPressed('up'):
    api.setFaceEmotion('Happy')
elif api.isPressed('down'):
    api.setFaceEmotion('Sad')
else:
    api.fableSpeak("You pressed something else", "en")