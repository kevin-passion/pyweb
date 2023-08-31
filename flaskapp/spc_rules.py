import pandas as pd
import numpy as np
import os
import statistics
import statistics as stats
#from scipy.stats import shapiro  


# path 설정
import sys
sys.path.append(r'C:\Python311\Lib\site-packages')
#ys.path.append(r'C:\Users\anb\anaconda3\Lib\site-packages')

# from sklearn.preprocessing import StandardScaler          # StandardScaler 스케일링을 진행
# import seaborn as sns 

# # chart 출력
# import matplotlib.pyplot as plt
import io
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
import base64

# chart 출력시 경고 무시
import warnings
warnings.simplefilter("ignore", UserWarning)

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

# #한글폰트 설정
# plt.rc('font', family='Malgun Gothic')         # 한글 폰트 
# plt.rcParams['axes.unicode_minus'] = False    # 음수 표시 (빼기, 음수 부호)


# 관리도 상수 값 : Control Limit Constants 
#--------------------------------------------------
def setCLConstants():
    
    df = pd.DataFrame(data = [[2,2.121,1.88,2.659,'-',3.267,'-',2.606,'-',3.686,'-',3.267,0.7979,1.2533,1.128,0.8865,1.88,2.695,1,0.853,0.6028],
            [3,1.732,1.023,1.954,'-',2.568,'-',2.276,'-',4.358,'-',2.574,0.8862,1.1284,1.693,0.5907,1.19,1.826,1.16,0.888,0.4633],
            [4,1.5,0.729,1.628,'-',2.266,'-',2.088,'-',4.698,'-',2.282,0.9213,1.0854,2.059,0.4857,0.8,1.522,1.092,0.88,0.3888],
            [5,1.342,0.577,1.427,'-',2.089,'-',1.964,'-',4.918,'-',2.114,0.94,1.0638,2.326,0.4299,0.69,1.363,1.198,0.864,0.3412],
            [6,1.225,0.483,1.287,0.03,1.97,0.029,1.874,'-',5.078,'-',2.004,0.9515,1.051,2.534,0.3946,0.55,1.263,1.135,0.848,0.3075],
            [7,1.134,0.419,1.182,0.118,1.882,0.113,1.806,0.204,5.204,0.076,1.924,0.9594,1.0423,2.704,0.3698,0.51,1.194,1.214,0.833,0.2822],
            [8,1.061,0.373,1.099,0.185,1.815,0.179,1.751,0.388,5.306,0.136,1.864,0.965,1.0363,2.847,0.3512,0.43,1.143,1.16,0.82,0.2621],
            [9,1,0.337,1.032,0.239,1.761,0.232,1.707,0.547,5.393,0.184,1.816,0.9693,1.0317,2.97,0.3367,0.41,1.104,1.223,0.808,0.2458],
            [10,0.949,0.308,0.975,0.284,1.716,0.276,1.669,0.687,5.469,0.223,1.777,0.9727,1.0281,3.078,0.3249,0.36,1.072,1.176,0.797,0.2322],
            [11,0.905,0.285,0.927,0.321,1.679,0.313,1.637,0.811,5.535,0.256,1.744,0.9754,1.0252,3.173,0.3152,'-','-','-',0.787,0.2207],
            [12,0.866,0.266,0.886,0.354,1.646,0.346,1.61,0.922,5.594,0.283,1.717,0.9776,1.0229,3.258,0.3069,'-','-','-',0.778,0.2107],
            [13,0.832,0.249,0.85,0.382,1.618,0.374,1.585,1.025,5.647,0.307,1.693,0.9794,1.021,3.336,0.2998,'-','-','-',0.77,0.2019],
            [14,0.802,0.235,0.817,0.406,1.594,0.399,1.563,1.118,5.696,0.328,1.672,0.981,1.0194,3.407,0.2935,'-','-','-',0.763,0.1942],
            [15,0.775,0.223,0.789,0.428,1.572,0.421,1.544,1.203,5.741,0.347,1.653,0.9823,1.018,3.472,0.288,'-','-','-',0.756,0.1872],
            [16,0.75,0.212,0.763,0.448,1.552,0.44,1.526,1.282,5.782,0.363,1.637,0.9835,1.0168,3.532,0.2831,'-','-','-',0.75,0.181],
            [17,0.728,0.203,0.739,0.466,1.534,0.458,1.511,1.356,5.82,0.378,1.622,0.9845,1.0157,3.588,0.2787,'-','-','-',0.744,0.1753],
            [18,0.707,0.194,0.718,0.482,1.518,0.475,1.496,1.424,5.856,0.391,1.608,0.9854,1.0148,3.64,0.2747,'-','-','-',0.739,0.1702],
            [19,0.688,0.187,0.698,0.497,1.503,0.49,1.483,1.487,5.891,0.403,1.597,0.9862,1.014,3.689,0.2711,'-','-','-',0.734,0.1655],
            [20,0.671,0.18,0.68,0.51,1.49,0.504,1.47,1.549,5.921,0.415,1.585,0.9869,1.0133,3.735,0.2677,'-','-','-',0.729,0.1611],
            [21,0.655,0.173,0.663,0.523,1.477,0.516,1.459,1.605,5.951,0.425,1.575,0.9876,1.0126,3.778,0.2647,'-','-','-',0.724,'-'],
            [22,0.64,0.167,0.647,0.534,1.466,0.528,1.448,1.659,5.979,0.434,1.566,0.9882,1.0119,3.819,0.2618,'-','-','-',0.72,'-'],
            [23,0.626,0.162,0.633,0.545,1.455,0.539,1.438,1.71,6.006,0.443,1.557,0.9887,1.0114,3.858,0.2592,'-','-','-',0.716,'-'],
            [24,0.612,0.157,0.619,0.555,1.445,0.549,1.429,1.759,6.031,0.451,1.548,0.9892,1.0109,3.895,0.2567,'-','-','-',0.712,'-'],
            [25,0.6,0.153,0.606,0.565,1.435,0.559,1.42,1.806,6.056,0.459,1.541,0.9896,1.0105,3.931,0.2544,'-','-','-',0.708,'-'],
            [1000,'-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-',1.253,'-','-']], 
            columns=['n', 'A', 'A2', 'A3', 'B3', 'B4', 'B5', 'B6', 'D1', 'D2', 'D3', 'D4','c4', '1/c4', 'd2', '1/d2', 'A4', 'A9', 'm3', 'd3', 'c5'])
    return df


# 특정 관리도계수값 찾기  
# df : 관리도 상수 값,  setCLConstants()
# sample_size : 부분군의 샘플 크기 (샘플갯수)
# constants_level : 검색할 상수항  'A', 'A2', 'A3', 'B3', 'B4', 'B5', 'B6', 'D1', 'D2', 'D3', 'D4','c4', '1/c4', 'd2', '1/d2', 'A4', 'A9', 'm3', 'd3', 'c5'
#------------------------------------------------------------------------------------------------------------------------------------------------------------
def getCLConstant(df, sample_size, constants_level):
    n = pd.Series([-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,1000])   # sample size, 부분군 갯수 
    constants_value = df.loc[n[sample_size],constants_level]
    if constants_value == '-':
        constants_value = 0
    return constants_value

# Data에서 sample size 구하기 : sample size = n
# data : 데이터 
# subgroup_name : sample size을 구하기위한 subgroup 컬럼명
#-------------------------------------------------------------------
def getSampleSize(data, subgroup_name):
    size = np.array(data.groupby(subgroup_name).size())
    if size[0] == size.mean():
        return size[0]
    else:
        return 0
    

# Rule check class
#------------------------------------
class spcRuleAnomalyDetector:    

    # Rule 1: One point is more than 3 standard deviations from the mean (outlier)
    def rule1(self, data, mean, sigma, column_nm):

        def isBetween(value, lower, upper):
            isBetween = value < upper and value > lower
            return 0 if isBetween else 1

        upperLimit = mean + 3 * sigma
        lowerLimit = mean - 3 * sigma

        data['Rule1'] = data.apply(lambda row: isBetween(row[column_nm], lowerLimit, upperLimit), axis = 1)
        return data

    # Rule 2: Nine (or more) points in a row are on the same side of the mean (shift)
    def rule2(self, data, mean, column_nm):
        values = [0]*len(data)

        # +1 means upside, -1 means downside
        upsideOrDownside = 0
        count = 0
        for i in range(len(data)):
            amount = data.iloc[i][column_nm]
            if amount > mean:
                if upsideOrDownside == 1:
                    count += 1
                else: 
                    upsideOrDownside = 1
                    count = 1
            elif amount < mean: 
                if upsideOrDownside == -1:
                    count += 1
                else: 
                    upsideOrDownside = -1
                    count = 1

            #rule 위배 셋팅
            if count >= 9:
                for n in range(count):
                    values[i-n] = 1


        data['Rule2'] = values    
        return data

    # Rule 3: Six (or more) points in a row are continually increasing (or decreasing) (trend)
    def rule3(self, data, column_nm):
        values = [0]*len(data)

        previousAmount = data.iloc[0][column_nm]
        # +1 means increasing, -1 means decreasing
        increasingOrDecreasing = 0
        count = 0
        for i in range(1, len(data)):
            amount = data.iloc[i][column_nm]
            if amount > previousAmount:
                if increasingOrDecreasing == 1:
                    count += 1
                else:
                    increasingOrDecreasing = 1
                    count = 1
            elif amount < previousAmount:
                if increasingOrDecreasing == -1:
                    count += 1
                else:
                    increasingOrDecreasing = -1
                    count = 1

            #rule 위배 셋팅
            if count >= 6:
                for n in range(count):
                    values[i-n] = 1

            previousAmount = amount

        data['Rule3'] = values 
        return data


    # Rule 4: Fourteen (or more) points in a row alternate in direction, increasing then decreasing (bimodal, 2 or more factors in data set)
    def rule4(self, data, column_nm):
        values = [0]*len(data)

        previousAmount = data.iloc[0][column_nm]
        # +1 means increasing, -1 means decreasing
        bimodal = 0
        count = 1
        for i in range(1, len(data)):
            amount = data.iloc[i][column_nm]

            if amount > previousAmount:
                bimodal += 1
                if abs(bimodal) != 1:
                    count = 0
                    bimodal = 0
                else:
                    count += 1
            elif amount < previousAmount:
                bimodal -= 1
                if abs(bimodal) != 1:
                    count = 0
                    bimodal = 0
                else:
                    count += 1

            previousAmount = amount
            
            #rule 위배 셋팅
            if count >= 14:
                for n in range(count):
                    values[i-n] = 1

        data['Rule4'] = values 
        return data

    # Rule 5: Two (or three) out of three points in a row are more than 2 standard deviations from the mean in the same direction (shift)
    def rule5(self, data, mean, sigma, column_nm):
        if len(data) < 3: return

        values = [0]*len(data)
        upperLimit = mean - 2 * sigma
        lowerLimit = mean + 2 * sigma        

        for i in range(len(data) - 3):
            first = data.iloc[i][column_nm]
            second = data.iloc[i+1][column_nm]
            third = data.iloc[i+2][column_nm]

            setValue = False
            validCount = 0
            if first > mean and second > mean and third > mean:
                validCount += 1 if first > lowerLimit else 0
                validCount += 1 if second > lowerLimit else 0
                validCount += 1 if third > lowerLimit else 0
                setValue = validCount >= 2
            elif first < mean and second < mean and third < mean:
                validCount += 1 if first < upperLimit else 0
                validCount += 1 if second < upperLimit else 0
                validCount += 1 if third < upperLimit else 0
                setValue = validCount >= 2
            
            #rule 위배 셋팅
            if setValue:
                if first > lowerLimit or first < upperLimit: values[i] = 1
                if second > lowerLimit or second < upperLimit: values[i+1] = 1
                if third > lowerLimit or third < upperLimit: values[i+2] = 1

        data['Rule5'] = values
        return data

    # Rule 6: Four (or five) out of five points in a row are more than 1 standard deviation from the mean in the same direction (shift or trend)
    def rule6(self, data, mean, sigma, column_nm):
        if len(data) < 5: return

        values = [0]*len(data)
        upperLimit = mean - sigma
        lowerLimit = mean + sigma   

        for i in range(len(data) - 5):
            pVals = list(map(lambda x: data.iloc[x][column_nm], range(i, i+5)))

            setValue = False
            if len(list(filter(lambda x: x > mean, pVals))) == 5:
                setValue = len(list(filter(lambda x: x > lowerLimit, pVals))) >= 4
            elif len(list(filter(lambda x: x < mean, pVals))) == 5:
                setValue = len(list(filter(lambda x: x < upperLimit, pVals))) >= 4

            #rule 위배 셋팅
            if setValue:
                for n in range(5):
                    if pVals[n] > lowerLimit or pVals[n] < upperLimit: values[i+n] = 1
                    
        data['Rule6'] = values
        return data
    
    
    # Rule 7: Fifteen points in a row are all within 1 standard deviation of the mean on either side of the mean (reduced variation or measurement issue)
    def rule7(self, data, mean, sigma, column_nm):
        if len(data) < 15: return
        values = [0]*len(data)
        upperLimit = mean + sigma
        lowerLimit = mean - sigma 

        for i in range(len(data) - 15):
            setValue = True
            for y in range(15):
                item = data.iloc[i + y][column_nm]
                if item >= upperLimit or item <= lowerLimit: 
                    setValue = False
                    break

            #rule 위배 셋팅
            if setValue:
                for n in range(15):
                    if data.iloc[i+n][column_nm] > lowerLimit or data.iloc[i+n][column_nm] < upperLimit: values[i+n] = 1                

        data['Rule7'] = values
        return data

    # Rule 8: Eight points in a row exist with none within 1 standard deviation of the mean and the points are in both directions from the mean (bimodal, 2 or more factors in data set)
    def rule8(self, data, mean, sigma, column_nm):
        if len(data) < 8: return
        values = [0]*len(data)

        for i in range(len(data) - 8):
            setValue = True
            for y in range(8):
                item = data.iloc[i + y][column_nm]
                if abs(mean - item) < sigma:
                    setValue = False
                    break

            #rule 위배 셋팅
            if setValue:
                for n in range(8):
                    if abs(mean - data.iloc[i+n][column_nm]) > sigma: values[i+n] = 1 

        data['Rule8'] = values
        return data


# df  : Data Frame 분석대상 데이터
# outlier : df와 동일한 크기의 outlier flag ( 1 : outlier )  Data Frame
# sigma : df와 동일한 크기의 sigma 값 Data frame
# def spcRuleChart(df, outlier, sigma, title):
#     # 샘플데이터 읽기 
#     #data = pd.read_csv('body_fat_data_reduced.csv') 
#     #df = pd.DataFrame(data)

#     # Standard Scalering 
#     standardScaler = StandardScaler()

#     # df standardScaler
#     standardScaler.fit(df)
#     df_standardScaled = standardScaler.transform(df)
#     scaled_df = pd.DataFrame(df_standardScaled, columns=df.columns)

#     # 시각화 
#     feature = scaled_df.columns
#     n_feature = len(feature) 
#     fig = plt.figure(figsize = (20,15))
#     for i in range(n_feature):
#         #1) 표준화 밀도 함수 시각화
#         fig.add_subplot(3, n_feature, i + 1)
#         mean = round(abs(scaled_df[feature[i]].mean()),3)
#         #std = round(abs(scaled_df[feature[i]].std()),3)       # 모수에서 표준편차
#         std = round(abs(stats.stdev(scaled_df[feature[i]])),3)  # 샘플에서 표준편차
#         #shapiro_test = round(shapiro(scaled_df[feature[i]]).pvalue,5)
        
#         # 시각화 
#         #sns.distplot(scaled_df[feature[i]], kde=True, rug=True, label='mean : '+ str(mean) +' std : '+ str(std)+'\n shapiro검정 : '+str(shapiro_test))
#         #sns.histplot(data=scaled_df[feature[i]], kde=True, label='mean : '+ str(mean) +' std : '+ str(std)+'\n shapiro Test : '+str(shapiro_test))
#         sns.histplot(data=scaled_df[feature[i]], kde=True, label='mean : '+ str(mean) +' std : '+ str(std))
#         #sns.kdeplot(scaled_df[feature[i]], color="blue", label="Density ST")
#         plt.axvline(std*3, 0, 0.8,color='red',linestyle='--',linewidth=1)
#         plt.axvline(std*-3, 0, 0.8,color='red',linestyle='--',linewidth=1)
#         plt.title(feature[i] + " Dist Plot", fontsize=20)
#         plt.legend(fontsize=15)
#         plt.grid(True, alpha=0.4, linestyle='--', which='both')


#         #2) raw data 에서 표준화에서 이상치라 표시한 데이터 표시하기 scatter plot
#         x = df.index                    # x 축
#         y = df[feature[i]]              # raw 데이터 값
#         raw_mean = y.mean()             # rsw data 평균 
#         raw_std = sigma                 # rsw data 표준편차 
#         ucl3 = raw_mean + raw_std * 3   # raw data Upper Control Line
#         ucl2 = raw_mean + raw_std * 2
#         ucl1 = raw_mean + raw_std * 1
#         lcl1 = raw_mean - raw_std * 1
#         lcl2 = raw_mean - raw_std * 2
#         lcl3 = raw_mean - raw_std * 3    # raw data lower Control Line

#         # 표준화값에서 이상치 위치를 찾아 raw data의 값을 찾는다. 
#         std_y = scaled_df[feature[i]]       # 표준화된 값 

#         # 표준화데이터에서 이상치 위치 찾기  
#         outlier_idx = outlier
#         #outlier_y = [y[i] for i in outlier_idx]                  # raw data에서 이상치 값 찾기 
#         outlier_y = pd.DataFrame(y, index=outlier_idx)  # raw data에서 이상치 값 찾기 
#         outlier_x = outlier_idx
        
#         #시각화  raw data scatter  
#         fig.add_subplot(3, n_feature, n_feature + i + 1)
#         plt.scatter(x,y)  
#         plt.axhline(raw_mean, 0, 1, color = 'gray', linestyle = '-', linewidth=1)

#         # 시각화 raw data scatter UCL 이상치  
#         plt.scatter(outlier_x, outlier_y, s=200, facecolor='none', color='red', label='SPC Rules Outlier')  
#         plt.title(feature[i] + ' ' + title, fontsize=20)
#         plt.axhline(ucl3, 0, 1, color = 'red', linestyle = '--', linewidth=1, label='UCL3')
#         plt.axhline(ucl2, 0, 1, color = 'green', linestyle = '--', linewidth=1, label='UCL2')
#         plt.axhline(ucl1, 0, 1, color = 'blue', linestyle = '--', linewidth=1, label='UCL1')
#         plt.axhline(lcl1, 0, 1, color = 'blue', linestyle = '--', linewidth=1, label='LCL1')
#         plt.axhline(lcl2, 0, 1, color = 'green', linestyle = '--', linewidth=1, label='LCL2')
#         plt.axhline(lcl3, 0, 1, color = 'red', linestyle = '--', linewidth=1, label='LCL3')    
#         #plt.legend(fontsize=15)  
        
#         # 3) 시각화 box-plot
#         ax = fig.add_subplot(3, n_feature, n_feature * 2 + i + 1)
#         box = ax.boxplot(df[feature[i]], notch=False, whis=0.5, vert=False)
#         ax.set_xlabel('Value')
#         ax.set_ylabel('Data Type')

#         whiskers = [item.get_xdata() for item in box['whiskers']]
#         medians = [item.get_xdata() for item in box['medians']]
#         fliers = [item.get_xdata() for item in box['fliers']]
        
#         #print('whiskers : ', whiskers)
#         #print('medians : ', medians)
#         #print('outliers : ', fliers)

#         # 웹 화면에 직접 출력하기 
#         #----------------------------
#         output = io.BytesIO()

#         # Embed the result in the html output.
#         plt.savefig(output, format='png', dpi=500)
#         output.seek(0)
#         l_chart = base64.b64encode(output.getbuffer()).decode("ascii")
#         #print(f' df_rate : {df_rate.T}')
#         #return df_rate.T
#         return l_chart



# df  : Data Frame 분석대상 데이터
# outlier : df와 동일한 크기의 outlier flag ( 1 : outlier )  Data Frame
# sigma : df와 동일한 크기의 sigma 값 Data frame
#-----------------------------------------------------------------------------
# def spcRuleScatterChart(df, outlier, sigma, title):
    
#     # 시각화 
#     print(f' >>> spcRuleScatterChart <<<<')
#     print(f' >>> spcRuleScatterChart df : {df}')
#     feature = df.columns
#     n_feature = len(feature) 

#     print(f' >>> spcRuleScatterChart feature : {feature}')
#     print(f' >>> spcRuleScatterChart n_feature : {n_feature}')

#     x = df.index              # x 축
#     print(f' >>> spcRuleScatterChart X : {x}')

#     fig = plt.figure(figsize = (20,15))
#     for i in range(n_feature):
#         # raw data 에서 표준화에서 이상치라 표시한 데이터 표시하기 scatter plot
#         # x = df.index              # x 축
#         y = df[feature[i]]            # raw 데이터 값
#         raw_mean = y.mean()           # rsw data 평균 
#         raw_std = sigma             # rsw data 표준편차 
#         ucl3 = raw_mean + raw_std * 3   # raw data Upper Control Line
#         ucl2 = raw_mean + raw_std * 2
#         ucl1 = raw_mean + raw_std * 1
#         lcl1 = raw_mean - raw_std * 1
#         lcl2 = raw_mean - raw_std * 2
#         lcl3 = raw_mean - raw_std * 3    # raw data lower Control Line

#         # 표준화데이터에서 이상치 위치 찾기  
#         outlier_idx = outlier
#         #outlier_y = [y[i] for i in outlier_idx]                  # raw data에서 이상치 값 찾기 
#         outlier_y = pd.DataFrame(y, index=outlier_idx)  # raw data에서 이상치 값 찾기 
#         outlier_x = outlier_idx
        
#         #print(f' >>> spcRuleScatterChart X : {x}')
#         print(f' >>> spcRuleScatterChart Y : {y}')
#         print(f' >>> spcRuleScatterChart outlier_x : {outlier_x}')
#         print(f' >>> spcRuleScatterChart outlier_y : {outlier_y}')
        
#         # 시각화 raw data scatter UCL 이상치  
#         fig.add_subplot(3, n_feature, n_feature + i + 1)
#         plt.scatter(x,y,color='gray')   # raw data 차트
#         plt.scatter(outlier_x, outlier_y, s=200, facecolor='none', color='red', label='SPC Rules Outlier')  
#         plt.axhline(raw_mean, 0, 1, color = 'gray', linestyle = '-', linewidth=1, label=f'mean : {round(raw_mean,5)}')             #평균값
#         plt.axhline(ucl3, 0, 1, color = 'red', linestyle = '--', linewidth=1, label='UCL3')
#         plt.axhline(ucl2, 0, 1, color = 'green', linestyle = '--', linewidth=1, label='UCL2')
#         plt.axhline(ucl1, 0, 1, color = 'blue', linestyle = '--', linewidth=1, label='UCL1')
#         plt.axhline(lcl1, 0, 1, color = 'blue', linestyle = '--', linewidth=1, label='LCL1')
#         plt.axhline(lcl2, 0, 1, color = 'green', linestyle = '--', linewidth=1, label='LCL2')
#         plt.axhline(lcl3, 0, 1, color = 'red', linestyle = '--', linewidth=1, label='LCL3')  
#         plt.title(feature[i] + ' ' + title, fontsize=20)
#         plt.legend(fontsize=15)

#         # 웹 화면에 직접 출력하기 
#         #----------------------------
#         output = io.BytesIO()

#         # Embed the result in the html output.
#         plt.savefig(output, format='png', dpi=500)
#         output.seek(0)
#         l_chart = base64.b64encode(output.getbuffer()).decode("ascii")
#         #print(f' df_rate : {df_rate.T}')
#         #return df_rate.T
#         return l_chart



# df  : Data Frame 분석대상 데이터
# outlier : df와 동일한 크기의 outlier flag ( 1 : outlier )  Data Frame
# sigma : df와 동일한 크기의 sigma 값 Data frame
#-----------------------------------------------------------------------------
# def spcRuleCheckChart(df, outlier, sigma, title):
    
#     # raw data 에서 표준화에서 이상치라 표시한 데이터 표시하기 scatter plot
#     feature = df.columns
#     x = df.index              # x 축
#     y = df[feature]            # raw 데이터 값
#     raw_mean = y.mean()           # raw data 평균 
#     raw_std = sigma             # rsw data 표준편차 
#     ucl3 = raw_mean + raw_std * 3   # raw data Upper Control Line
#     ucl2 = raw_mean + raw_std * 2
#     ucl1 = raw_mean + raw_std * 1
#     lcl1 = raw_mean - raw_std * 1
#     lcl2 = raw_mean - raw_std * 2
#     lcl3 = raw_mean - raw_std * 3    # raw data lower Control Line

#     # 표준화데이터에서 이상치 위치 찾기  
#     outlier_idx = outlier
#     #outlier_y = [y[i] for i in outlier_idx]                  # raw data에서 이상치 값 찾기 
#     outlier_y = pd.DataFrame(y, index=outlier_idx)  # raw data에서 이상치 값 찾기 
#     outlier_x = outlier_idx
    
#     # 시각화 raw data scatter UCL 이상치  
#     fig = plt.figure(figsize = (10,10))
#     plt.subplot(111)
#     plt.scatter(x,y,color='gray')   # raw data 차트
#     plt.scatter(outlier_x, outlier_y, s=200, facecolor='none', color='red', label='SPC Rules Outlier')  
#     plt.axhline(raw_mean, 0, 1, color = 'gray', linestyle = '-', linewidth=1, label=f'mean : {round(raw_mean,5)}')             #평균값
#     plt.axhline(ucl3, 0, 1, color = 'red', linestyle = '--', linewidth=1, label='UCL3')
#     plt.axhline(ucl2, 0, 1, color = 'green', linestyle = '--', linewidth=1, label='UCL2')
#     plt.axhline(ucl1, 0, 1, color = 'blue', linestyle = '--', linewidth=1, label='UCL1')
#     plt.axhline(lcl1, 0, 1, color = 'blue', linestyle = '--', linewidth=1, label='LCL1')
#     plt.axhline(lcl2, 0, 1, color = 'green', linestyle = '--', linewidth=1, label='LCL2')
#     plt.axhline(lcl3, 0, 1, color = 'red', linestyle = '--', linewidth=1, label='LCL3')  
#     plt.title(feature + ' ' + title, fontsize=20)
#     plt.legend(fontsize=15)
    
#     # 웹 화면에 직접 출력하기 
#     #----------------------------
#     output = io.BytesIO()

#     # Embed the result in the html output.
#     plt.savefig(output, format='png', dpi=500)
#     output.seek(0)
#     l_chart = base64.b64encode(output.getbuffer()).decode("ascii")
#     #print(f' df_rate : {df_rate.T}')
#     #return df_rate.T
#     return l_chart
    

# 주어진 data을 이용하여     
# Nelson Rules 검사
#------------------------------------
# def nelson_rules_check(rule_no, file_read_data, group_colname=None, colname=None):

#     print(f' nelson_rules_check rule_no : {rule_no}')
#     print(f' nelson_rules_check file_read_data : {file_read_data}')
#     print(f' nelson_rules_check group_colname : {group_colname}')
#     print(f' nelson_rules_check colname : {colname}')
#     print(f" >>>>>>> nelson_rules_check file_read_data colname : {colname} <<<<<<")
#     print(f" >>>>>>> nelson_rules_check file_read_data group_colname : {group_colname} <<<<<<")

#     # DataFrame 새로 만들기
#     if group_colname == '[None]':
#        idx = list(range(0,len(file_read_data)))
#        df = pd.DataFrame({ "new_gcol_name" : idx, colname : file_read_data[colname] })
#        group_colname = "new_gcol_name"
#     else:
#         # subgroup의 데이터를 분석하기 쉽게 일련번호로 수정하여 원데이터를 변경하기   
#         temp_data = pd.DataFrame({group_colname:file_read_data[group_colname], colname:file_read_data[colname]})
#         temp_data = temp_data.dropna()   # 결측치 데이터 있으면 삭제하기

#         sample_size = getSampleSize(temp_data, group_colname) # subgroup sample size 구하기 
#         print(f'nelson_rules_check temp_data : {temp_data}')
#         print(f'nelson_rules_check sample_size : {sample_size}')

#         # subgroup의 데이터를 계산하기 쉽게 일련번호로 변경하기 (0 ~ subgroup수량)
#         sample_group = np.repeat(range(0,len(temp_data.groupby(group_colname).mean())),sample_size)
#         print(f'nelson_rules_check sample_group : {sample_group}')

#         # 변경된 신규 data frame
#         df = pd.DataFrame({group_colname:sample_group, colname:temp_data[colname]})
#         df = df.dropna()   # 결측치 데이터 있으면 삭제하기
#         #print(data)
    
#     print(" >>>>>>> nelson_rules_check new generation data : df <<<<<<")
#     print(df)
    

#     # Group masures by sample group (x_bar)
#     df_grouped = df.groupby(group_colname).mean()

#     # Rename x-bar column
#     df_grouped.columns = [colname]
#     #print(df_grouped)
#     print(f' >>> nelson_rules_check df_grouped : {df_grouped}')

#     # 관리도 상수값 
#     sample_size = getSampleSize(df, group_colname)
#     print(f' >>> nelson_rules_check sample size 2 : {sample_size}')

#     # Xbar 관리도 (= X바 + A2 * R)
#     data_cl = setCLConstants()
#     if sample_size <= 9 and sample_size > 1:
#         A2 = getCLConstant(data_cl, sample_size, 'A2')
#         print(' >>>>> A2 <<<<<<< :', A2)

#         # Add R (range) Column
#         df_max = df.groupby(group_colname).max()
#         df_min = df.groupby(group_colname).min()
#         df_grouped['R'] = df_max[colname] - df_min[colname]

#         print(' >>>>> TEST <<<<<<< :', df_max[colname], df_min[colname])

#         # unbiased estimate 불편추정량 
#         df_data = pd.DataFrame(df_grouped[colname])              # subgroup 의 평균 
#         rbar = (statistics.mean(df_grouped['R']) * A2) / 3       # r-bar의 불편추정량, sigma 값 
#         xbar = statistics.mean(df_grouped[colname])              # x-bar
#     # Xbar 관리도 ( = X바 + A3*S바) 
#     elif sample_size > 9:
#         A3 = getCLConstant(data_cl, sample_size, 'A3')
#         print(' >>>>> A3 <<<<<<< :', A3)

#         # unbiased estimate 불편추정량 
#         df_data = pd.DataFrame(df_grouped[colname])              # subgroup 의 평균 
#         rbar = (statistics.stdev(df_grouped[colname]) * A3) / 3  # s-bar의 불편추정량, sigma 값 
#         xbar = statistics.mean(df_grouped[colname])              # x-bar
#     # X 관리도 (=X + 3 * mR바 / d2)
#     elif sample_size == 1:
#         d2 = 1.128
#         print(' >>>>> d2 <<<<<<< :', d2)

#         # Define list variable for moving ranges
#         MR = [np.nan] * len(df)

#         # Get and append moving ranges
#         i = 1
#         for data in range(1, len(df)):
#             MR.append(abs(df[colname][i] - df[colname][i-1]))
#             i += 1

#         # Convert list to pandas Series objects    
#         MR = pd.Series(MR)
#         df_grouped['R'] = MR

#         # unbiased estimate 불편추정량 
#         df_data = pd.DataFrame(df_grouped[colname])              # subgroup 의 평균 
#         rbar = statistics.mean(df_grouped[colname]) / d2         # s-bar의 불편추정량, sigma 값 
#         xbar = statistics.mean(df_grouped[colname])              # x-bar

    
#     print(f' >>>>>> nelson_rules_check df_data <<<<<<:  {df_data} ')

#     # -------------------
#     #  SPC RULE TEST 
#     #--------------------------------------------
#     # spc rules test
#     column_nm = colname
#     detector = spcRuleAnomalyDetector()
#     if rule_no == 'spc_rule1':
#         spc_out1 = detector.rule1(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out1['Rule1']
#     elif rule_no == 'spc_rule2':
#         spc_out2 = detector.rule2(df_data, xbar, column_nm)  
#         spec_out_flag = spc_out2['Rule2']
#     elif rule_no == 'spc_rule3':    
#         spc_out3 = detector.rule3(df_data, column_nm)
#         spec_out_flag = spc_out3['Rule3']
#     elif rule_no == 'spc_rule4':
#         spc_out4 = detector.rule4(df_data, column_nm)
#         spec_out_flag = spc_out4['Rule4']
#     elif rule_no == 'spc_rule5':
#         spc_out5 = detector.rule5(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out5['Rule5']
#     elif rule_no == 'spc_rule6':
#         spc_out6 = detector.rule6(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out6['Rule6']
#     elif rule_no == 'spc_rule7':
#         spc_out7 = detector.rule7(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out7['Rule7']
#     elif rule_no == 'spc_rule8':
#         spc_out8 = detector.rule8(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out8['Rule8']

#     spec_out_flag = np.array(spec_out_flag)

#     # -------------------
#     #  SPC RULE TEST 결과 시각화 1
#     #--------------------------------------------
#     df_raw = pd.DataFrame(df_data[column_nm])  #공통 
#     out_len = len(df_raw)
#     print(f"평균은 {df_raw[column_nm].mean()} 이고, 표준편차는 {rbar} 이면 sample size는 {sample_size} 임")

#     # ----------
#     # spc rule  테스트 결과
#     ##---------------------------------------------
#     print(f" out_len : {out_len} : range : {range(out_len)}")
#     print(f"{spec_out_flag}  ")
#     n = df_raw.index.min()
#     outlier = [] 
#     for i in range(out_len):
#         #print(spec_out_flag[i])
#         if 0 != spec_out_flag[i]: outlier += [n]
#         n += 1

#     print(f" >>>> nelson_rules_check outlier : {outlier}  ")
#     spc_chart = spcRuleChart(df_raw, outlier, rbar, rule_no)             # chart 작성 : histgram, scatter, box-plot
#     #spc_chart = spcRuleScatterChart(df_raw, outlier, rbar, rule_no)     # chart 작성 : scatter
#     #spc_chart = spcRuleCheckChart(df_raw, outlier, rbar, rule_no) 
#     outlier_y = [df_raw[colname][i] for i in outlier]       # raw data에서 이상치 값 찾기  
#     # print(f"outlier_y : {outlier_y}")

#     return spc_chart, outlier_y


# Nelson Rules 적용 예제
#------------------------------------
# def nelson_rules_exam(rule_no):
    
#     # -------------------
#     #  샘플 데이터 준비 : Range 용도   n <= 9
#     #--------------------------------------------
#     # Generate normal distributed measures
#     #data = np.round(np.random.normal(loc=50, scale=25, size=100),2)
#     data = np.random.randn(100)
#     #print(data)

#     # Generate sample groups
#     sample_size=5
#     sample_group = np.repeat(range(0,20),sample_size)
#     #print(sample_group)

#     # Define data frame
#     df = pd.DataFrame({'data':data, 'sample_group':sample_group})
#     #print(df)

#     # Group masures by sample group (x_bar)
#     df_grouped = df.groupby('sample_group').mean()

#     # Rename x-bar column
#     df_grouped.columns = ['x_bar']
#     #print(df_grouped)

#     # 관리도 상수값 
#     data_cl = setCLConstants()
#     A2 = getCLConstant(data_cl, sample_size, 'A2')

#     # Add R (range) Column
#     df_max = df.groupby('sample_group').max()
#     df_min = df.groupby('sample_group').min()
#     df_grouped['R'] = df_max['data'] - df_min['data']

#     # unbiased estimate 불편추정량 
#     df_data = pd.DataFrame(df_grouped['x_bar'])              # subgroup 의 평균 
#     rbar = (statistics.mean(df_grouped['R']) * A2) / 3       # r-bar의 불편추정량, sigma 값 
#     xbar = statistics.mean(df_grouped['x_bar'])              # x-bar

#     # -------------------
#     #  SPC RULE TEST 
#     #--------------------------------------------
#     # spc rules test
#     column_nm = 'x_bar'
#     detector = spcRuleAnomalyDetector()
#     if rule_no == 'spc_rule1':
#         spc_out1 = detector.rule1(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out1['Rule1']
#     elif rule_no == 'spc_rule2':
#         spc_out2 = detector.rule2(df_data, xbar, column_nm)  
#         spec_out_flag = spc_out2['Rule2']
#     elif rule_no == 'spc_rule3':    
#         spc_out3 = detector.rule3(df_data, column_nm)
#         spec_out_flag = spc_out3['Rule3']
#     elif rule_no == 'spc_rule4':
#         spc_out4 = detector.rule4(df_data, column_nm)
#         spec_out_flag = spc_out4['Rule4']
#     elif rule_no == 'spc_rule5':
#         spc_out5 = detector.rule5(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out5['Rule5']
#     elif rule_no == 'spc_rule6':
#         spc_out6 = detector.rule6(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out6['Rule6']
#     elif rule_no == 'spc_rule7':
#         spc_out7 = detector.rule7(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out7['Rule7']
#     elif rule_no == 'spc_rule8':
#         spc_out8 = detector.rule8(df_data, xbar, rbar, column_nm)
#         spec_out_flag = spc_out8['Rule8']

#     spec_out_flag = np.array(spec_out_flag)

#     # -------------------
#     #  SPC RULE TEST 결과 시각화 1
#     #--------------------------------------------
#     df_raw = pd.DataFrame(df_data[column_nm])  #공통 
#     out_len = len(df_raw)

#     # ----------
#     # spc rule  테스트 결과
#     ##---------------------------------------------
#     n = 0
#     outlier = []
#     for i in range(out_len):
#         if 0 != spec_out_flag[i]: outlier += [n]
#         n += 1
#     spc_chart = spcRuleChart(df_raw, outlier, rbar, rule_no)             # chart 작성 : histgram, scatter, box-plot
#     #spc_chart = spcRuleScatterChart(df_raw, outlier, rbar, rule_no)     # chart 작성 : scatter
#     outlier_y = [df_raw[i] for i in outlier]                  # raw data에서 이상치 값 찾기  
    
#     return spc_chart, outlier_y
        


