import binascii
# decode input text n times
# decode U2FtcGxlIHRleHQ=
# decode VGhpcyBpcyB0b28gZWFzeQ==
# decode (encoded multiple times) VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFFvPQo=

text = raw_input("Enter text: ")
loopTimes = int(raw_input("Enter loop amount: "))

for i in range(loopTimes):
  try:
    decodedText = text.decode("base64")
    print decodedText
    text = decodedText
  except binascii.Error as err:
    print "Incorrect padding error"