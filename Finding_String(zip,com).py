text = "all zip files are zipped"
print text.find("zip",5)
text = "all zip files are compressed"
print text.find("zip",6)    # my  IDEA:

text = "all zip files are zipped"
first_zip = text.find("zip")
print text.find("zip",first_zip+1)
        # Or
print text.find("zip",text.find("zip") + 1)
