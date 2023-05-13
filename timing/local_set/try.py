import time
import server


def login(username):
    time_sta = time.time()
    server.main(username, 'aaaa')
    time_end = time.time()
    t = time_end- time_sta
    return t

def main():
    times = 10
    correct = 0
    wrong1 = 0
    wrong2 = 0
    wrong3 = 0

    for i in range(times):
        correct += login('hochono_house')
        wrong1 += login('admin')
        wrong2 += login('roooot')
        wrong3 += login('Administrator')
    
    correct = correct / times
    wrong1 = wrong1 / times
    wrong2 = wrong2 / times
    wrong3 = wrong3 / times

    print('admin user:  ' + str(correct))
    print('op user:     ' + str(wrong1))
    print('op user:     ' + str(wrong2))
    print('op user:     ' + str(wrong3))

if __name__ == '__main__':
    main()