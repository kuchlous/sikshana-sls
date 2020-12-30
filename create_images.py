import os
# txt = "she takes us on lots of field trips in the Magic school bus. Believe me, it's not called magic for nothing. We never know what's going to happen when we get on that bus."
#txt = "There is a fail at the local dispute ground to friends. Jr and I are planning to go to the failed to buy Some Thais love each other. Did you hear about the door, Fay? No, There is a located. It is happening at our local district Ground. It is a very beautiful Phil. Really. We should go. Then I will ask Averted friends to We can all go on by Lords of toys for ourselves. I'm so excited. Jail me Dove e j. After the field, J R and B J came back home and displayed their ties. Why did you get for yourself, BJ? I bought the more control card for myself and the teddy bear for my little brother. What did you get? J Im bought a pair of top choice words for my sister on myself. We will play with this war Like that show in the back gardens. You love everything we bought journal. It's Colisee things We will all play together"
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
    cmd = "wkhtmltoimage tmp.html images-sikshana/" + str(i) + ".jpg"
    os.system(cmd)
