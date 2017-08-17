import sys
import os

print 'Change from "path length class" to "path start_frame class step"'
name = os.path.basename(sys.argv[1])
name = os.path.splitext(name)[0]

with open("%s_modified.txt" % name, 'w') as g:
    with open(sys.argv[1], 'r') as f:
        for line in f:
            video = line.split(' ')[0]
            clas = line.split(' ')[2]
            g.write("%s 1 %s 1 \n" % (video, clas))

print "Finished! Output: %s_modified.txt" % name
