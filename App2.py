import streamlit as st

# --- 1. 設定網頁標題與版面 ---
st.set_page_config(page_title="申請研究所自傳生成系統 v4.1", page_icon="🎓", layout="centered")

st.title("🎓 申請研究所自傳生成系統")
st.markdown("""
### 專業版自傳生成器
本系統依照學術界標準的 **五大核心項目** 設計。請依序填寫資料，系統將自動組織段落邏輯，生成一篇結構嚴謹的自傳。
""")

with st.sidebar:
    st.header("💡 填寫指南")
    st.info("""輸入框內的灰色文字僅為範例，請直接輸入您的真實資料。""")
    st.success("""✨ v4.1 更新：現在可以自訂「座右銘」了！""")

# --- 2. 建立輸入表單 ---

with st.form("autobiography_form"):

    # 📌 第一類：基本身分資料
    st.header("1. 個人基本資料 (Personal Profile)")
    col1, col2 = st.columns(2)
    
    name = col1.text_input("姓名 (必填)", placeholder="例如：陳瑋承")
    status = col1.selectbox("目前身分", ["應屆畢業生", "已畢業", "在職中"])
    
    highest_school = col2.text_input("最高學歷學校 (必填)", placeholder="例如：國立臺北大學")
    highest_dept = col2.text_input("最高學歷系所 (必填)", placeholder="例如：中國文學系碩士")
    
    col3, col4 = st.columns(2)
    phone = col3.text_input("聯絡電話", placeholder="0912-345-678")
    email = col4.text_input("電子郵件", placeholder="example@email.com")

    st.markdown("---")

    # 🎯 第二類：申請目標客製化
    st.header("2. 申請動機 (Motivation)")
    st.caption("""此部分將決定自傳的開頭與結尾，請務必針對目標校系填寫。""")
    
    target_school = st.text_input("目標學校全稱 (必填)", placeholder="例如：國立臺灣大學")
    
    col_t1, col_t2 = st.columns(2)
    target_dept = col_t1.text_input("目標系所全稱 (必填)", placeholder="例如：中國文學系博士班")
    target_group = col_t2.text_input("欲申請組別 (若無可留空)", placeholder="例如：古文字學組")
    
    dept_feature = st.text_area(
        "吸引您的系所特色 (必填)", 
        height=100,
        placeholder="例如：貴所在「出土文獻與古典學」領域具備頂尖的研究資源，且擁有豐富的古文字數位資料庫。"
    )
    
    target_professor = st.text_input("目標指導教授 (選填)", placeholder="例如：曾昱夫 教授")

    st.markdown("---")

    # 📚 第三類：學術背景與表現
    st.header("3. 學術背景 (Academic Background)")
    st.caption("""證明您的學術基礎足以勝任研究所課業。""")
    
    research_interests = st.text_input("核心研究領域/關鍵字 (必填)", placeholder="例如：文字學、漢字教學、數位人文")
    
    col_a1, col_a2 = st.columns(2)
    academic_highlight = col_a1.text_input("學業量化表現", placeholder="例如：系排前 5%、曾獲書卷獎")
    thesis_topic = col_a2.text_input("過去專題/論文主題", placeholder="例如：部件與圖像結合之漢字教學研究")
    
    other_academic_skill = st.text_input("其他學術技能/修課亮點 (選填)", placeholder="例如：修習「古籍數位化」課程，熟悉資料庫建置")

    st.markdown("---")

    # ✨ 第四類：個人特質與經歷
    st.header("4. 個人特質與經歷 (Traits & Experience)")
    st.caption("""請輸入您的核心特質與座右銘，這能展現您的人格高度。""")
    
    st.markdown("👉 **個人特質關鍵字**")
    col_p1, col_p2, col_p3 = st.columns(3)
    trait_1 = col_p1.text_input("特質 1", placeholder="例如：積極主動")
    trait_2 = col_p2.text_input("特質 2", placeholder="例如：樂於溝通")
    trait_3 = col_p3.text_input("特質 3", placeholder="例如：抗壓性強")
    
    # 修改重點：新增座右銘欄位
    motto = st.text_input("個人座右銘/處事態度 (選填)", placeholder="例如：魔鬼藏在細節裡 / 不做不會怎樣，做了很不一樣")
    
    st.markdown("👉 **展現特質的小故事**")
    story = st.text_area("一句話描述特質實例", placeholder="例如：半工半讀完成學業，並曾與母親合開早餐店，這段經歷培養了我解決問題的行動力。")

    st.markdown("👉 **關鍵成就 (建議列出 3 項)**")
    exp_1 = st.text_input("經歷/成就 1", placeholder="例如：發表兩篇數位人文相關論文於研究生研討會")
    exp_2 = st.text_input("經歷/成就 2", placeholder="例如：擔任學報編輯助理三年，熟悉學術行政")
    exp_3 = st.text_input("經歷/成就 3", placeholder="例如：兩度擔任國際研討會總召")

    st.markdown("---")

    # 🔭 第五類：未來規劃
    st.header("5. 未來展望 (Future Goals)")
    short_term = st.text_area("短期目標 (入學後)", height=80, placeholder="例如：深入探討漢字構形類化，並結合數位工具研究降低錯字率的方法。")
    long_term = st.text_input("長期目標 (畢業後)", placeholder="例如：將研究成果應用於對外華語教學，成為該領域的跨域學者。")

    # 送出按鈕
    submitted = st.form_submit_button("✨ 生成自傳")

# --- 3. 生成邏輯與模板 ---

if submitted:
    # 檢查必填欄位
    if not name or not highest_school or not target_school or not target_dept:
        st.error("⚠️ 請至少填寫「姓名」、「學歷」、「目標學校」與「目標系所」才能生成喔！")
    else:
        # 邏輯處理：準備變數
        group_str = f"【{target_group}】" if target_group else ""
        prof_str = f"我尤其仰慕貴所 **{target_professor}** 在該領域的卓越研究，渴望能受其指導。" if target_professor else ""
        skill_str = f"此外，我曾{other_academic_skill}，為進階研究打下基礎。" if other_academic_skill else ""
        
        # 特質字串處理
        traits_list = [t for t in [trait_1, trait_2, trait_3] if t]
        if traits_list:
            traits_desc = "、".join(traits_list)
            traits_sentence = f"我具備 **{traits_desc}** 的個人特質。"
        else:
            traits_sentence = "我具備積極進取且樂於挑戰的個人特質。"

        # 座右銘處理 (修改重點)
        if motto:
            motto_sentence = f"我的處事觀念是「{motto}」，並以此作為自我要求的準則。"
        else:
            motto_sentence = "我始終秉持著腳踏實地、勇於任事的態度。"

        # 經歷列表格式化
        exp_list = [exp_1, exp_2, exp_3]
        valid_exp = [item for item in exp
