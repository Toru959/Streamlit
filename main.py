import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門') #タイトルを表示

st.write('Hello World!') #文字を表示

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})

st.write(df) #　dfの表を表示する
# st.datafream(df()) # dfの表を表示する（引数を取れる）
# st.table(df.style.highlight_max(axis=0)) # dfの表を静的に表示する

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