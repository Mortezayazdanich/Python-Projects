import qrcode
import cv2

action = input("What action you wish to proceed with?(e:Encode, D:Decode)")

match action:
    case "e":
        data = input("Enter the data for encoding into a QR:")
        code = qrcode.make(data)
        code.save("qr.png")
    case "d":
        file_name = input("please enter the QR Code location: ")  
        img = cv2.imread(file_name)
        data, v_array, b_code = cv2.QRCodeDetector().detectAndDecode(img)
        print(data)

