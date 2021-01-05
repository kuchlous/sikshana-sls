import os
txt = "This is an amazing short story for kids, the ugly duckling story. Once upon a time, there was a duck. She lived in the forest. One day she laid some eggs. After warming them carefully, the duck waited for the eggs to hatch. As she watched, three of her eggs cracked and three lovely ducklings came into the world."
words = txt.split(' ')
prefix = ""
for i in range(len(words)):
    prefix = ' '.join(words[0:i])
    highlighted_word = '<span style="color:red;">' + words[i] + '</span>'
    suffix = ' '.join(words[i + 1: len(words)])
    html = prefix + ' ' + highlighted_word + ' ' + suffix
    with open("tmp.html", "w") as f:
        f.write(html)
        cmd = "node puppet.js file://{0}/tmp.html images-sikshana/{1}.jpg".format(os.getcwd(), str(i))
    os.system(cmd)
