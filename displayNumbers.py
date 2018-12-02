import sys
import time
startTime = time.time()
for i in range(10000):
  sys.stdout.write("\rTesting %s" % i)
print ""
print "Time taken: %.04f seconds" % (time.time() - startTime)