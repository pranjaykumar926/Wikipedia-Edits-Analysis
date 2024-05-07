import csv
with open('filtered_dataset.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    with open('languageedition.csv', 'w', newline='') as outputfile:
        csvwriter = csv.writer(outputfile)
        for row in csvreader:
            separated_values = row[1].split(',')
            csvwriter.writerow(separated_values)