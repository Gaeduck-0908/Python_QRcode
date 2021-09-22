import qrcode

print("QR코드로 만들 URL 입력.")
url = input()

if(len(url) != 0):
    print("저장할 파일명 입력.")
    name = input()
    if(len(name) != 0):
        qr_img = qrcode.make(url)
        qr_img.save("{}.png".format(name))
        print("정상적으로 만들어졌습니다.")
    else:
        print("정상적인 파일명을 입력해주세요.")
else:
    print("정삭적인 URL을 입력해주세요")