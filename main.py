import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像表示

st.title('Streamlit 超入門') #タイトルを表示

st.write('Hello World!') #文字を表示

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})

df = pd.DataFrame(
    np.random.rand(20, 3), #タテ20行横3列
    columns=['a', 'b', 'c']
)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.write('Display Image')

img = Image.open('logo.jpg') #画像表示
st.image(img, caption="python", use_column_width=True)#画像表示
#st.write(df) #　dfの表を表示する
# st.datafream(df()) # dfの表を表示する（引数を取れる）
# st.table(df.style.highlight_max(axis=0)) # dfの表を静的に表示する

#st.line_chart(df) #折線グラフ
#st.area_chart(df) #折れ線グラフに似たやつ
#st.bar_chart(df) #棒グラフ
#st.map(df) #map


#-----
#"""
# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```


#"""
#------

