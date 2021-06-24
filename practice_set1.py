from playsound import playsound;
import multiprocessing;

'''
  playsound('F:\\2021\\python\\python basics\\chapter1\\Kalimba.mp3')
'''
p = multiprocessing.Process(target=playsound, args=("F:\\2021\\python\\python basics\\chapter1\\Kalimba.mp3",))
p.start()
input("press ENTER to stop playback")
p.terminate()