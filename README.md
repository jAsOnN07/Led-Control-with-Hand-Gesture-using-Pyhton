# Led-Control-with-Hand-Gesture-using-Pyhton
This is a Arduino and Python Project where we can turn on/off leds and change brightness with Hand Gesture using (Opencv , Mediapipe , cvzone , Pyfirmata2)

# Circuit Diagram
![Arduino Circuit Designer](https://github.com/jAsOnN07/Led-Control-with-Hand-Gesture-using-Pyhton/assets/90206616/e918e8dd-d42d-4899-97be-401aa7476448)

# How to Run the Project
First you need to open your ardunio ide , ther you have to download a library called "firmata"
![image](https://github.com/jAsOnN07/Led-Control-with-Hand-Gesture-using-Pyhton/assets/90206616/8a867421-5959-4980-835b-4315860de8c3)

After downloading firmata follow the steps shown and upload the code onto your arduino Board
![image](https://github.com/jAsOnN07/Led-Control-with-Hand-Gesture-using-Pyhton/assets/90206616/f60ae74e-e26f-4e5a-b973-b832017f38a3)

Now open any coding ide and Clone the repository using the following command. 

**git clone https://github.com/jAsOnN07/Led-Control-with-Hand-Gesture-using-Pyhton.git**

Now we need to install 4 Python packages you can download them using the following  command 

**pip install opencv-python pyFirmata cvzone mediapipe**

Now you can simply run the main.py file and your project should be working .

If you have the latest python version you may face an error like this 
![image](https://github.com/jAsOnN07/Led-Control-with-Hand-Gesture-using-Pyhton/assets/90206616/281a0e5c-6622-465d-acb3-01eba169d940)
Then you just have to click the link in the error and change the 231 line to  **len_args = len(inspect.getfullargspec(func)[0])**
Now there should be no errors and the project should be working fine.



