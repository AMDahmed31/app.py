import streamlit as st

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

# واجهة التطبيق
st.title("🔢 مولد الأرقام - Number Generator")
st.write("تطبيق بسيط لتوليد مجموعة من الأرقام")

# زرار لتشغيل الـ generator
if st.button("اضغط لتوليد الأرقام / Generate Numbers"):
    st.subheader("النتائج:")
    
    # عرض الأرقام بشكل جميل
    cols = st.columns(4)
    for idx, value in enumerate(myGenerator()):
        with cols[idx]:
            st.metric(label=f"رقم {idx + 1}", value=value)
    
    st.success("✅ تم توليد الأرقام بنجاح!")
    
    # عرض الأرقام كقائمة أيضاً
    numbers = list(myGenerator())
    st.write(f"**القائمة الكاملة:** {numbers}")

# معلومات إضافية
with st.expander("ℹ️ معلومات عن التطبيق"):
    st.write("""
    هذا التطبيق يستخدم Python Generator لتوليد أرقام من 1 إلى 4.
    
    **كيفية الاستخدام:**
    - اضغط على الزر لتوليد الأرقام
    - ستظهر لك الأرقام بشكل تفاعلي
    """)
