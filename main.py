import cv2

a = int(input('cam or img? (1/0) '))
neuron = cv2.CascadeClassifier('neuron.xml')
if a:
    cap = cv2.VideoCapture(0)

    while True:
        a, b = cap.read()
        gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)

        results = neuron.detectMultiScale(gray, scaleFactor = 1.35, minNeighbors = 3)

        for (x, y, w, h) in results:
            cv2.rectangle(b, (x, y), (x + w, y + h), (0, 0, 255), thickness = 2)

        cv2.imshow('Cam', b)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    img = cv2.imread('images/img_1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = neuron.detectMultiScale(gray, scaleFactor=1.35, minNeighbors=3)
    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
    cv2.imshow('Cam', img)
    cv2.waitKey(0)