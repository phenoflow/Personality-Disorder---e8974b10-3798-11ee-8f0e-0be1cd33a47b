# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"E211100","system":"readv2"},{"code":"E211300","system":"readv2"},{"code":"E214.11","system":"readv2"},{"code":"E21y300","system":"readv2"},{"code":"E21y600","system":"readv2"},{"code":"E21z.00","system":"readv2"},{"code":"Eu21.18","system":"readv2"},{"code":"Eu60013","system":"readv2"},{"code":"Eu60200","system":"readv2"},{"code":"Eu60213","system":"readv2"},{"code":"Eu60300","system":"readv2"},{"code":"Eu60311","system":"readv2"},{"code":"Eu60412","system":"readv2"},{"code":"Eu60512","system":"readv2"},{"code":"Eu60700","system":"readv2"},{"code":"Eu60711","system":"readv2"},{"code":"Eu60713","system":"readv2"},{"code":"Eu60714","system":"readv2"},{"code":"Eu60y12","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('personality-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["personality-disorder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["personality-disorder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["personality-disorder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
