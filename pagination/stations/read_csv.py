import csv
def read_csv(path_to_csv):
    with open(path_to_csv, encoding='utf-8') as csv_file:
        my_csv_reader = csv.DictReader(csv_file, delimiter=',')
        return [{"Name": i['Name'], "Street": i['Street'], 'District': i['District']} for i in my_csv_reader]