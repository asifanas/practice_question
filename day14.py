# import threading
# from threading import Thread, Lock
#
#
# class UserThread(Thread):
#     def run(self):
#         print("Before Lock - ", threading.current_thread().getName())
#         lock.acquire()
#         for count in range(5):
#             print(count)
#         lock.release()
#         print("After Lock - ", threading.current_thread().getName())
#
# lock = Lock()
# th1 = UserThread()
# th2 = UserThread()
#
# th1.start()
# th2.start()
#
# print("asif anas")
#
# if __name__ == "__main__":
#     print("as")

# from threading import Thread
#
#
# class person1(Thread):
#     def run(self):
#         for count in range(50):
#             print(count)
#
#
# class person2(Thread):
#     def run(self):
#         for count in range(10):
#             print(count)
#
#
# class Mobile:
#     def __init__(self):
#         self.person1 = person1()
#         self.person2 = person2()
#
# mobile = Mobile()
# mobile.person1.start()
# mobile.person2.start()
