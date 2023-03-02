import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from time import sleep

st.title('streamlit 入門')

# st.write('DataFrame')
st.write('プログレスバーの表示')
# st.sidebar.write('Inreractive Widgets')
'Start!!'

latest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問合せ1')
expander1.write('問合せ1への回答')
expander2 = st.expander('問合せ2')
expander2.write('問合せ2への回答')
expander3 = st.expander('問合せ3')
expander3.write('問合せ3への回答')

# option = st.text_input('貴方の趣味を教えてください') 
# option = st.sidebar.text_input('貴方の趣味を教えてください') 
# '貴方の趣味は',option,'です。'

# condition = st.slider('貴方の今の調子は？',0,100,70)
# condition = st.sidebar.slider('貴方の今の調子は？',0,100,70)
# 'コンディション：',condition
# option = st.selectbox(
#     'あなたが好きな数字を入れてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'

# if st.checkbox('Show Image'):
#     img = Image.open(r'C:\Users\ysio7\OneDrive\画像\画像6.png') 
#     st.image(img,caption='graph',use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.dataframe(df, width =300  ,height =800)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

# st.dataframe(df.style.highlight_max(axis=0), width =300  ,height =200)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

