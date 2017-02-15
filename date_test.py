import datetime

date = "September 8";
year = 2016;
new = date + " " + str(year);
#new = date[0].split();
print (new);
test = str(datetime.datetime.strptime(new, '%B %d %Y').date());
print (test);
print (test.replace("-",""));