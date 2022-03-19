import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 50, 20, 30]
})
st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```
"""

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['a', 'b', 'c']  
)

st.dataframe(df)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

if st.checkbox('Show Map'):
    df = pd.DataFrame(
        np.random.rand(100, 2)/[50, 50] + [36.3228, 139.0127],
        columns=['lat', 'lon']  
    )
    st.map(df)

if st.checkbox('Show Image'):
    st.write('Display Image')
    img = Image.open('sample.jpg')
    st.image(img, caption='Rika taiken', use_column_width=True)
st.write('selectbox')
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は ', option, 'です。'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

st.write('Interctive widgets')
text = st.sidebar.text_input('あなたの趣味をを教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0 , 100, 50)

'あなたの趣味:', text
'コンディション：', condition

expander = st.expander('問合せ')
expander.write('問合せ内容を書く')

st.write('プログレスバーの表示')
'Start!!'

lateset_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    lateset_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

