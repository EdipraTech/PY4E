text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
new_num = float(text[pos:pos+6])
print(new_num)