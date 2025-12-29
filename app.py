import streamlit as st
import random

# إعداد الصفحة
st.set_page_config(page_title="لعبة تخمين الرقم", page_icon="🎲")

# تهيئة session state
if 'true_number' not in st.session_state:
    st.session_state.true_number = random.randint(1, 100)
    st.session_state.attempts = 10
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.history = []

# العنوان الرئيسي
st.title("🎲 لعبة تخمين الرقم الصحيح")
st.markdown("### Guess the Correct Number Game")

# عرض التعليمات
with st.expander("📖 كيفية اللعب / How to Play"):
    st.write("""
    **قواعد اللعبة:**
    - خمن رقم بين 1 و 100
    - لديك 10 محاولات
    - سيخبرك التطبيق إذا كان الرقم أكبر أو أصغر
    - اربح باختيار الرقم الصحيح!
    
    **Game Rules:**
    - Guess a number between 1 and 100
    - You have 10 attempts
    - The app will tell you if the number is higher or lower
    - Win by choosing the correct number!
    """)

# عرض المعلومات الحالية
col1, col2 = st.columns(2)
with col1:
    st.metric("المحاولات المتبقية / Attempts Left", st.session_state.attempts)
with col2:
    st.metric("النطاق / Range", "1 - 100")

# عرض السجل
if st.session_state.history:
    st.write("**محاولاتك السابقة / Your Previous Guesses:**")
    st.write(", ".join([str(x) for x in st.session_state.history]))

st.markdown("---")

# اللعب
if not st.session_state.game_over and not st.session_state.won:
    guess = st.number_input(
        "أدخل تخمينك / Enter Your Guess:",
        min_value=1,
        max_value=100,
        step=1,
        key="guess_input"
    )
    
    if st.button("خمّن! / Guess!", type="primary"):
        if guess in st.session_state.history:
            st.warning("⚠️ لقد جربت هذا الرقم من قبل! / You already tried this number!")
        else:
            st.session_state.history.append(guess)
            st.session_state.attempts -= 1
            
            if guess > st.session_state.true_number:
                st.error(f"❌ لا، اختر رقماً **أصغر**! (-) / No, choose a **smaller** number!")
            elif guess < st.session_state.true_number:
                st.warning(f"❌ لا، اختر رقماً **أكبر**! (+) / No, choose a **larger** number!")
            elif guess == st.session_state.true_number:
                st.session_state.won = True
                st.balloons()
                st.success(f"🎉 **مبروك! فزت!** / **Congratulations! You Won!**")
                st.success(f"الرقم الصحيح كان: {st.session_state.true_number}")
                st.info(f"استخدمت {10 - st.session_state.attempts} محاولة / You used {10 - st.session_state.attempts} attempts")
            
            if st.session_state.attempts == 0 and not st.session_state.won:
                st.session_state.game_over = True

# Game Over
if st.session_state.game_over:
    st.error("💔 **انتهت اللعبة! / Game Over!**")
    st.info(f"الرقم الصحيح كان: {st.session_state.true_number}")
    st.write("المحاولات انتهت! / Attempts Finished!")

# زر إعادة اللعب
if st.session_state.game_over or st.session_state.won:
    st.markdown("---")
    if st.button("🔄 العب مرة أخرى / Play Again", type="primary"):
        st.session_state.true_number = random.randint(1, 100)
        st.session_state.attempts = 10
        st.session_state.game_over = False
        st.session_state.won = False
        st.session_state.history = []
        st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
    <p>صنع بواسطة Python و Streamlit 💻</p>
    </div>
    """,
    unsafe_allow_html=True
)
