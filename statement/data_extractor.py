from pdf_to_json import convert_to_json


def extract(file_name):
    d = convert_to_json(file_name)
    date = []
    desc = []
    debit= []
    credit=[]
    balance=[]
    
    i = 3
    while(i<25):
        dt = d[0]['data'][i][0]['text']
        ds = d[0]['data'][i][2]['text']
        db = d[0]['data'][i][4]['text']
        cr = d[0]['data'][i][5]['text']
        bal= d[0]['data'][i][6]['text']
        while(d[0]['data'][i+1][0]['text']=='' or (d[0]['data'][i+1][0]['text']=='2017')):
            ds= ds+d[0]['data'][i+1][2]['text']
            if(d[0]['data'][i+1][0]['text'] != ''):
                dt= dt + d[0]['data'][i+1][0]['text']
            i=i+1
        date.append(dt)
        desc.append(ds)
        debit.append(db)
        credit.append(cr) 
        balance.append(bal)
        i=i+1

    extracted_data = []
    extracted_data.append(date)
    extracted_data.append(desc)
    extracted_data.append(balance)
    extracted_data.append(credit)
    extracted_data.append(debit)
    
    return extracted_data 
