from ClassObjects import *

def extract_aurin_language(melb, aurin):
    for item in aurin:
        sa3code = item['properties']['sa3_code16']
        info = {"lang_spoken_home_eng_only_p": item['properties']['lang_spoken_home_eng_only_p'],"lang_spoken_home_oth_lang_p": item['properties']['lang_spoken_home_oth_lang_p']}
        for district in melb.districts:
            if district == sa3code:
                melb.districts[district].aurin_lang = info

def extract_aurin_income(melb, aurin):
    for item in aurin:
        sa3code = item['properties']['sa3_code16']
        info = {"p_1_149_tot": item['properties']['p_1_149_tot'],
            "p_150_299_tot": item['properties']['p_150_299_tot'],
            "p_300_399_tot": item['properties']['p_300_399_tot'],
            "p_400_499_tot": item['properties']['p_400_499_tot'],
            "p_500_649_tot": item['properties']['p_500_649_tot'],
            "p_650_799_tot": item['properties']['p_650_799_tot'],
            "p_800_999_tot": item['properties']['p_800_999_tot']
        }
        for district in melb.districts:
            if district == sa3code:
                melb.districts[district].aurin_income = info    

def extract_aurin_health(melb, aurin):
    for item in aurin:
        sa3code = item['properties']['sa3_code']
        info = {"all_patients_avg_medicare_bfts_expenditure_patient": item['properties']['all_patients_avg_medicare_bfts_expenditure_patient'],
            "all_patients_avg_oop_cst_patient": item['properties']['all_patients_avg_oop_cst_patient'],
            "all_patients_avg_no_patient": item['properties']['all_patients_avg_no_patient'],
            "perc_patients_csts": item['properties']['perc_patients_csts']}
        for district in melb.districts:
            if district == sa3code:
                melb.districts[district].aurin_health = info 
