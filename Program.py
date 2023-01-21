import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os.path as path

print("Enter path to csv file:")
while True:
    csv_path=input()
    if not (path.isfile(csv_path)):
        print("File isn't found. Please enter path again")
    else:
        print("File found")
        break
print("Enter separator for csv header")
separator=","
while True:
    separator=input()
    if(len(separator)==0):
        print("Empty separator isn't allowed. Please enter separator again:")
    else:
        break
df = pd.read_csv(csv_path,sep=separator)
df.head()
print("Last valid index="+str(df.last_valid_index()))
print("Header:")
print(df.columns)
print("Enter horizontal indexes head name")
indexName=""
while True:
    indexName=input()
    if(len(indexName)==0):
        print("Empty Index Name isn't allowed. Please enter again:")
    else:
        break
x = df[indexName]
heads=""
print("Enter heads for plotting with ; example withuout quotes: 'a;b'")
while True:
    heads=input()
    if(len(heads)==0):
        print("Empty head (Y values on plot) isn't allowed. Please enter again:")
    else:
        break

for head in heads.split(";"):
    y = df[head]
    plt.plot(x, y, label = head)
plt.legend()
plt.show()