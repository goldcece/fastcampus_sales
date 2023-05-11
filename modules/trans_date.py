from datetime import datetime, timedelta
import re
def trans_date(str):
    '''
    거래일자를 string에서 datetime으로 바꿔줍니다.

    Parameters :
        str(str) : dataframe['column'].apply(trans_date) 그대로 넣으세요.
    Return :
        ap_dt(datetime) :  datetime으로 바뀐 str이 반환
    '''
    ampm = str.split()[-2] # 오전인지 오후인지 판단
    str = re.sub('[ ㄱ-ㅣ가-힣]+', '', str) # str에서 오전, 오후 둘다 삭제
    
    if ampm == '오전':
        ap_dt = datetime.strptime(str, '%Y.%m.%d.%I:%M:%S')
    else:
        ap_dt = datetime.strptime(str, '%Y.%m.%d.%I:%M:%S') + timedelta(hours=12)
    
    return ap_dt
