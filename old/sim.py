"""
selfSimilarity.py
Displays a pitch and timbre self-similarity matrix.
By Joe Paxton
13 February 2015 
Usage: 
    python selfSimilarity.py timbre AUDIO_FILE.mp3
    python selfSimilarity.py pitches AUDIO_FILE.mp3
Example:
    python selfSimilarity.py pitches "C:\users\your_name\desktop\worldstar.mp3"
"""
import numpy as n
import math as mat
import matplotlib.pyplot as plt
import echonest.remix.audio as audio
from scipy.spatial import distance

def main():
    print('Program starting...')
    print('----------------------------------------------')
    
    t,p = matrix()
    print "Length of t: ", len(t)
    print "Length of p: ", len(p)
    print
    print t
    
    #kbdin=raw_input('Press enter to continue ... ')
    print "Preparing plot..."
    show_plot('Timbre', t)
    show_plot('Pitch', p)
    print "Done."

def show_plot(desc, m):
    plot = plt.imshow(m)
    plot.set_cmap('gray')
    
    plot2 = plt.imshow(invert_x(m))
    plot2.set_cmap('gray')
    #plt.set_label(desc) #need to figure out how to set TITLE/LEGEND on graph
    
    plt.show()

def invert_x(p):
    x = p
    for i in xrange(len(p)):
        #print i
        #print "x[i] = ", x,"[",i,"] = ",x[i]
        xtmp = x        
        #x[i] = x[len(x)-i-1]
        #x[len(x)-i-1] = xtmp
        
    return x

# This function calculates the euclidean distance
# for both timbre and pitches between the segments
# of the uploaded audio file
def matrix():
    # Gets the analysis of the audio file worldstar.mp3
    # and we can analyze the track by getting its ID
    segments = audio.AudioAnalysis('TRVSKVZ1467FC8250D').segments
    segs = (len(segments), len(segments))
    dist = 0.0
    
    # New array filled with zeros, import numpy
    timbreMatrix = n.zeros(segs)
    pitchesMatrix = n.zeros(segs)

    # Goes through the segments and assigns the
    # appropriate distance for the timbre's
    # self-similarity
    #for items in range(len(segments)):

    # Goes through the segments and assigns the
    # appropriate distance for the timbre's
    # self-similarity

    print "Building Matrix...segments = ", len(segments)
    
    for i in range(len(segments)):
        for j in range(len(segments)):
            #dist = euclid(segments[i].timbre, segments[j].timbre)
            dist = distance.euclidean(segments[i].timbre, segments[j].timbre)
            #print 'i=',i, ' dist=', dist
            timbreMatrix[i][j] = dist            
    print 'Building pitches...'        
    # Same thing, but for the pitches     
    for i in range(len(segments)):
        for ii in range(len(segments)):
            #dist = euclid(segments[i].pitches, segments[ii].pitches)
            dist = distance.euclidean(segments[i].pitches, segments[ii].pitches)
            pitchesMatrix[i][ii] = dist

    print 'Finished building matrix...'          
    return timbreMatrix, pitchesMatrix

"""
    for items in range(len(segments)):
        for j in range(len(segments)):
            dist = euclid(segments[items].timbre, segments[j].timbre)
            timbreMatrix[items][j] = dist
            
    # Same thing, but for the pitches     
    for i in range(len(segments)):
        for ii in range(len(segments)):
            dist = euclid(segments[i].pitches, segments[ii].pitches)
            pitchesMatrix[i][ii] = dist
            
    return timbreMatrix, pitchesMatrix    
"""

def euclid(a,b):
    sum = 0.0
    dist = 0.0
    for i in range(len(a)):
        sum += (a[i]- b[i])**2
    dist = mat.sqrt(sum)
    return dist

if __name__ == "__main__":
    main()
