# [PANDAS] 특정값이 존재하는 행의 인덱스 번호를 가져오기
# index_number = dataframe.index[(dataframe['컬럼명'] == '특정값')]
# 특정행의 데이터 가져오기
# print(dataframe.iloc[index_number])
# 특정행을 리스트로 변경
# data = dataframe.iloc[index_number].to_list()
# 리스트에서 값 추출
# data[0]

# dataframe 만들기
# dates = pd.date_range('20130101', periods=6)
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))


# 컬럼 열번호 가져오기
#df2.columns.get_loc('E')

# 컬럼 행번호 가져오기
#df2.index.get_loc('2013-01-01')


### 선택

# 컬럼 선택 (컬럼명)
# df.A 혹은 df['A']

# 행범위 선택
# df[0:3]
# df['2013-01-02':'2013-01-04']
# ! 행 하나 선택 시 df['2013-01-02':'2013-01-02'] 앞뒤를 동일한 인덱스 기입

### .loc

# 행선택
# df.loc[dates[0]] or df.loc['2013-01-02']

# 열선택
# df.loc[:, ['A']]
# df.loc[:, ['A', 'B']]

# adjustable range : 작동 지점을 설정할 수 있는 범위 (주로 Switch 에서 필요한 항목 같음)









