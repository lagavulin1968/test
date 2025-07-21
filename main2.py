import streamlit as st
import streamlit.components.v1 as components
import base64
import pandas as pd

# app.py
st.set_page_config(page_title="main", page_icon="📊")


st.write('Hello World!')
st.write('Hello :blue[World!]')
st.title('Hello World! 	:coffee:')

st.link_button('Google', 'https://www.google.com/')
st.link_button('click here', 'https://developer.x.com/en/portal/dashboard')


# 2つのカラムに分けて表示
col1, col2 = st.columns(2)

with col1:
    st.link_button('Google', 'https://www.google.com/')

with col2:
    st.link_button('click here', 'https://x.com/i/status/1907776820205990341')


code = """
# 数値型の列だけを抽出
df1 = df['時間']
st.line_chart(df1)

# df.info()の情報を取得し、DataFrame化する関数を作成
def dataframe_info(df):
    info_df = pd.DataFrame({
        "Column": df.columns,
        "Non-Null Count": df.notnull().sum().values,
        "Dtype": df.dtypes.values
    })
    return info_df
"""
st.code(code, language='python')




if st.button('動画1を表示'):
    st.video('sample1.mp4') 

if st.button('動画2を表示'):
    st.video('sample2.mp4') 

if st.button('動画3を表示'):
    st.video('sample3.mp4')




st.title("🤖 AI Agent Sample Videos")
tab1, tab2, tab3, tab4 = st.tabs(["🎥 動画編集", "💡 画像検索＆送信", "✈️🏨 旅行手配", "📝 Samples_Code"])

with tab1:
    # st.markdown(
    #     '<p style="font-size:14px; color:blue;">AI Agentがマウスとキーボードを自動かつ高速に操作し、カットや結合などの動画編集タスクを効率的に実行しています。</p>',
    #     unsafe_allow_html=True
    # )
    st.markdown(
    '<p style="font-size:16px; color:#2b6cb0;">AI Agentがマウスとキーボードを自動かつ高速に操作し、カットや結合などの動画編集タスクを効率的に実行しています。</p>',
    unsafe_allow_html=True
)
    st.video("sample1.mp4")

with tab2:
    st.video("sample2.mp4")

with tab3:
    st.video("sample3.mp4")

with tab4:
    st.write("### コードサンプル")
    st.code(code, language='python')



tab = st.radio(
    "メニューを選んでください",
    ["🎥 動画編集", "🔍 画像検索", "✈️ 旅行手配", "💻 コード"],
    horizontal=True
)

if tab == "🎥 動画編集":
    # st.write("AI Agentがマウスとキーボードを自動かつ高速に操作し、カットや結合などの動画編集タスクを効率的に実行しています。")
    st.markdown(
    '<p style="font-size:16px; color:#2b6cb0;">AI Agentがマウスとキーボードを自動かつ高速に操作し、カットや結合などの動画編集タスクを効率的に実行しています。</p>',
    unsafe_allow_html=True
    )
    st.video("sample1.mp4")  # ← この時だけ読み込まれる！

elif tab == "🔍 画像検索":
    st.write("画像処理関連の機能です。")
    st.video("sample2.mp4")

elif tab == "✈️ 旅行手配":
    st.write("旅行プランを表示中...")
    st.video("sample3.mp4")

elif tab == "💻 コード":
    st.write("コードスニペットを表示します。")
    st.code("print('Hello, Streamlit!')", language="python")


st.image("Deep Serach.jpeg", caption="Deep Serach", use_container_width=True)


# 外部のHTMLファイルを読み込んで表示する場合
with open("BPO_AI活用図.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# components.html(html_data, height=12000)

components.html(html_data, height=12000, width=700, scrolling=True)




# HTMLファイルのパス
file_path = "BPO_AI活用図.html"
file_name = "BPO_AI活用図.html"

# ファイル読み込み
with open(file_path, "r", encoding="utf-8") as f:
    html_data = f.read()

# base64にエンコード（ブラウザで開くため）
b64 = base64.b64encode(html_data.encode()).decode()

# 新しいタブで開くためのHTMLリンク（download属性なし）
href = f'<a href="data:text/html;base64,{b64}" target="_blank">▶ HTMLを新しいタブで開く</a>'
st.markdown(href, unsafe_allow_html=True)


video_url = "https://x.com/i/status/1945904743148323285"

# リンクを表示（新しいタブで開く）
st.markdown(f'<a href="{video_url}" target="_blank">▶ 動画を開く（Xの投稿）</a>', unsafe_allow_html=True)



video_path = "downloaded_video.mp4"
st.video(video_path)