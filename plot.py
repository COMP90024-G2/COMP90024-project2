import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

def main():
    with open("output.json",'r') as f:
        data = json.load(f)
    content = data['rows'][0]['doc']["historical_analysis"]["features"]
    non_eng_speaker_pct = []
    average_emotion = []
    aurin_income_lvl = []
    health_att = []
    aurn_health_expenditure = []
    employment_att = []
    for district in content:
        non_eng_speaker_pct.append(district['properties']['proportion_non_english_tweets'])
        average_emotion.append(district['properties']['general_emotion'])
        lv1_income = district['properties']['aurin_income']["p_1_149_tot"]
        lv2_income = district['properties']['aurin_income']["p_150_299_tot"]
        lv3_income = district['properties']['aurin_income']["p_300_399_tot"]
        lv4_income = district['properties']['aurin_income']["p_400_499_tot"]
        lv5_income = district['properties']['aurin_income']["p_500_649_tot"]
        lv6_income = district['properties']['aurin_income']["p_650_799_tot"]
        lv7_income = district['properties']['aurin_income']["p_800_999_tot"]
        employment_att.append(district['properties']["employment_attitude"]) 
        healthcare_attitude = district['properties']["healthcare_attitude"]
        #healthcare_attitude = district['properties']["aurin_health"]["all_patients_avg_medicare_bfts_expenditure_patient"]
        if healthcare_attitude != None:
            health_att.append(district['properties']["healthcare_attitude"])
            aurn_health_expenditure.append(district['properties']["aurin_health"]["all_patients_avg_medicare_bfts_expenditure_patient"])
            print(healthcare_attitude)
        average = (lv1_income * 149 + lv2_income * 299 + lv3_income * 399 + lv4_income * 499 + lv5_income * 649 + lv6_income * 799 + lv7_income * 999)/(lv1_income + lv2_income + lv3_income + lv4_income + lv5_income + lv6_income + lv7_income)
        aurin_income_lvl.append(average)
        
    for i in range(len(non_eng_speaker_pct)):
        print("Non-english speaker percent:",non_eng_speaker_pct[i] ,"average income in that district:",aurin_income_lvl[i])
    plot_data = pd.DataFrame()
    health_plot = pd.DataFrame()
    plot_data["Non-english speaker percent"] = non_eng_speaker_pct
    plot_data["average income in that district"] = aurin_income_lvl
    plot_data["general_emotion"] = average_emotion
    plot_data["employment_attitude"] = employment_att
    health_plot["healthcare_attitude"] = health_att
    health_plot["Aurin avrg patient medical expenditure"] = aurn_health_expenditure

    #print(health_plot)
    #print(plot_data)
    #sns.set_theme(style="whitegrid", palette="pastel", color_codes=True)
    #sns.color_palette("dark:salmon_r", as_cmap=True)
    sns.regplot(x = "Non-english speaker percent", y = "average income in that district", data = plot_data, color = "red")
    plt.show()
    sns.regplot(y = "employment_attitude", x = "Non-english speaker percent", data = plot_data, color = "red")
    plt.show()
    sns.regplot(x = "general_emotion", y = "average income in that district", data = plot_data, color = "red")
    plt.show()
    sns.regplot(x = "healthcare_attitude", y = "Aurin avrg patient medical expenditure", data = health_plot, color = "red")
    plt.show()

    current_content = data['rows'][0]['doc']["new_analysis"]["features"]
    cur_general_emotion = []
    past_general_emotion = []
    change_in_gen_emo = []
    for district in current_content:
        if district['properties']["tweet_count"] != 0:
            cur_general_emotion.append(district['properties']["general_emotion"])
            district = district['properties']["sa3code"]
            for district2 in content:
                if district2['properties']["sa3code"] == district:
                    past_general_emotion.append(district2['properties']["general_emotion"])
                    
    study_df = pd.DataFrame()
    study_df["Past general emotion"] = past_general_emotion
    for i in range(len(cur_general_emotion)):
        change_in_gen_emo.append(cur_general_emotion[i] - past_general_emotion[i])
    study_df["Change"] = change_in_gen_emo
    print(study_df)
    sns.regplot(x = "Past general emotion", y = "Change", data = study_df, color = "red")
    plt.show()

os.chdir('F:/CCCproject2')
main()
