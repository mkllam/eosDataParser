import pandas as pd
import math


if __name__ == '__main__':
    filename = input("Enter your filename: ")
    point = float(input("Enter your point for analysis: "))
    pointOutput = []
    output = []
    data = pd.read_csv(filename).to_numpy()
    for row in data:
        count=0
        avg=0
        stats={}
        parse = []

        if(row[0]<30): #Distance 30m
            continue
        parse.append(row[0])

        for i in row:
            if (count == 0):
                count += 1
                continue  # Skip distance
            avg += i
            count += 1
            if(i in stats.keys()):
                stats[i] = stats[i]+1
            else:
                stats[i] = 1
            
        parse.append(avg/(count-1))
        if(row[0]>point):
            for key in sorted(stats):
                pointOutput.append([key, stats[key]])
            af = pd.DataFrame(pointOutput, columns=['Value', 'Frequency'])
            af.to_csv(str(point)+'.csv', index=False, header=True)
            point = 9999

        output.append(parse)

    df = pd.DataFrame(output, columns=['Distance', 'Average'])
    df.to_csv('average.csv', index=False, header=True)