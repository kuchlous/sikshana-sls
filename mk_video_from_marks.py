#!/usr/local/bin/python3

import sys

end_times = []
with open(sys.argv[1]) as f:
    for l in f:
        time = int(l.split(",")[0][8:])/1000
        end_times.append(time)

end_times = end_times[1:]

print(end_times)

with open("ffmp.in", "w") as f:
    prev_time = 0.0
    for i in range(len(end_times)):
        duration = float(end_times[i]) - prev_time
        f.write("file \'images-sikshana/{0}.jpg\' \n".format(i))
        f.write("duration {} \n".format(duration))
        prev_time = float(end_times[i])

    f.write("file \'images-sikshana/{0}.jpg\' \n".format(len(end_times)))
    f.write("duration {} \n".format(0.5))

