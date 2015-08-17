def main():
    import matplotlib.pyplot as plt
    import numpy as np
    #import scipy.io.wavfile
    import wave as w
    song = 'sound.wav'
    #data1, rate = scipy.io.wavfile.read(song)
    file = w.open(song)
    print 'channels: ', file.getnchannels()
    print 'num frames: ', file.getnframes()
    numFrames = file.getnframes()
    rframes = file.readframes(10)
    x = map(ord, list(rframes))
    print 'read frames:', x

    fig = plt.figure(1)
    fig.clf()
    data = np.random.random((3,3))
    print 'rand: ', data
    #matrix = [[0 for time in range(numframes)] for frames in range(x)]
    #for time in range(numframes):
    #    for frames in range(x):
    #        matrix[time]
    matrix[] = [0 for time in range(numframes)]
    for time in numframes:
        matrix[time] = rframes
    print matrix

    xaxis = np.arange(0,3)
    yaxis = np.arange(0,3)
    ax = fig.add_subplot(211)
    #ax.imshow(data, interpolation='none')
    c = ax.contour(xaxis, yaxis, data, colors='k')
    #ax2 = fig.add_subplot(212)
    plt.show()

if  __name__ == '__main__':
    import sys
    try:
        main()
    except:
        print
        sys.exit(-1)
