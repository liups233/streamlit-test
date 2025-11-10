import streamlit as st
import cloudflare_ai as ai


st.set_page_config(page_title="语言检测")
st.title("语言检测与修正")
cf_account_id = st.text_area("输入 Cloudflare 账户 ID：", height=70)
cf_workers_api = st.text_area("输入 Workers AI API：", height=70)
user_input = st.text_area("请输入句子：", height=100)
if st.button("分析"):
    if user_input.strip() == "":
        st.warning("请输入句子再点击按钮")
    else:
        with st.spinner("正在分析中……", show_time=True):
            score = ai.judge_offense(user_input, cf_account_id, cf_workers_api)
            st.success(f"歧视分析结果得分：**{score}**")
            if score in ["4", "5"]:
                result = ai.improve_sentence(user_input, cf_account_id, cf_workers_api)
                st.success(f"调整后的句子为：\n{result}")
