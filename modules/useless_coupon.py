import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from matplotlib import font_manager, rc
import platform

def useless_coupon(df):
    '''
    Make and Drop Useless Coupon list from DF
    
    Parameters:
    DataFrame
    
    Returns:
    DataFrame with useless coupons data which to be deleted
    '''
    coupon_df = pd.DataFrame()
    
    coupon_count = df['쿠폰이름'].value_counts()
    coupon_name = df['쿠폰이름'].unique()

    cnt = []
    for i in range (len(coupon_count)):
        cnt.append(coupon_count[i])
    coupon_df['counts'] = cnt
    coupon_df['coupon_name'] = df['쿠폰이름'].unique()
    
    coupon_award_list=[]
    year_coupon = list(coupon_df[coupon_df['coupon_name'].str.contains('자기계발 어워즈 무료수강권')].index)
    year_coupon = year_coupon[1:] # 0번째만 정상 쿠폰
    for i in year_coupon:
        coupon_award_list.append(coupon_df.iloc[i]['coupon_name'][:4])
    
    stopword = ['^테스트$', '결제테스트', '검수용', '미리보기', '업무용', '참고용', '미리보기', 'test', '검토용', '신해동', '내부', '직원', '지인', '강의검수', '조교', '제공용', '예외처리', 'cx', 'CX', '^쿠폰$', '^3$', '발행', '예외발급', 'TEST', '인턴']
    stopword = stopword + coupon_award_list

    # # 'coupon_name' 컬럼에서 stopword 리스트 안에 있는 단어가 포함된 행만 선택
    filtered_df = coupon_df[coupon_df['coupon_name'].str.contains('|'.join(stopword), na=False)
                            & (~coupon_df['coupon_name'].str.contains('A/B 테스트'))]
    
    return filtered_df