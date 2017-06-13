ตัวอย่างการใช้ OpenCV ทำ Shape Detection รูปแบบหนึ่ง



ขั้นตอนการทำ
```
1. โหลดรูป RGB
2. แปลงเป็น Grey
3. ตัด Threshold
4. นำภาพ Mask มา Inverse
5. หา Contours ของภาพ [จะได้ Contours มาเป็น List ตามจำนวนวัตถุ Mask]
6. นำ Contours มาวนทีละชิ้น
  - หา Moments
  - หา Center of mass
  - หา Approximation
  - วาดจุด และ ข้อความลงบนรูป
7. จะได้ Output Image ออกมา
```
To differentiate between Rectangle & Square
```
1. Find the point we need to calculate
2. Find the magnitude of 2 side which the angle between it is 90 degrees
3. Compare it!
```
![ScreenShot](https://raw.github.com/FIBO-Robotics/Beginer/master/ImageRecognition/Output.png?raw=true "Output Image")
Output Image

