import joblib

import pandas as pd
class prediction:
    
    def pr(data):
        find = {
            'city_development_index': data[0],
            'gender': data[1],
            'relevant_experinece': data[2],
            'enrolled_university': data[3],
            'education_level': data[4],
            'major_disvipline': data[5],
            'experience': data[6],
            'company_size': data[7],
            'company_type': data[8],
            'last_new_job': data[9],
            'training_hours': data[10]
        }
        model = joblib.load('model.pkl')
       
        test = pd.DataFrame(find,index=[0])
        y_pr = model.predict(test)
        if y_pr == 0:
            return 'accepted he will keep with us'
        elif y_pr == 1:
            return 'he will not stay with us, refused'
