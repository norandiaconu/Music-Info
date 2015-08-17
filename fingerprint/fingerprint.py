import sys
import numpy as np
#import pyaudio as pa
import wave as wav
sys.path.append('/u/css/diaconuna/other/music/fingerprint/db')
sys.path.append('/u/css/diaconuna/other/music/fingerprint/queries')
queries = {'1': 'query1.wav', '2': 'query2.wav', '3': 'query3.wav', '4': 'query4.wav',
           '5': 'query5.wav', '6': 'query6.wav'}
db = {'1': 'song1.wav', '2': 'song2.wav', '3': 'song3.wav', '4': 'song4.wav',
      '5': 'song5.wav', '6': 'song6.wav'}

def main():
    query1 = wav.open(queries['1'])
    frame_num = 0
    frames_num = query1.getnframes()
    frames = query1.readframes(frames_num)
    
    fig = plt.figure(1)
    fig.clf()
    data = queries#np.random.random((3,3))
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

