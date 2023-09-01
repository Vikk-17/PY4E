# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'
semi_coln = str.find(':')
# print(semi_coln)
flt = float(str[semi_coln+1:])

print(type(flt), f">{flt}")
