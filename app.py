import streamlit as st

from bert import *

st.set_page_config(layout="wide")
st.markdown("""
<style>
.little-font {
    font-size:0.8rem !important;
}
</style>
""", unsafe_allow_html=True)

header = st.beta_container()

text_input, buffer, text_output = st.beta_columns([20,1,20])

with header:
    st.title("Atlas Research Question Answering Tool")

with text_input:
    st.header("Question Input")
    user_input = [st.text_area("Enter your question here:", value="", height=200)]
    print(user_input)

with text_output:
    st.header("Suggested Answer")
    st.markdown('<p class="little-font">Copy your answer here:</p>', unsafe_allow_html=True)
    encode_questions()
    bm = BertAnswer()
    if user_input == ['']:
        pass
    else:
        df = getResults(user_input, getBertAnswer)
        st.write(df.iloc[0]['A'])
        st.write("\n")
        score = df.iloc[0]['Score']
        perc = "{:.0%}".format(score)
        st.markdown("_with confidence_: "+ perc)

more_details = st.beta_container()

if user_input == ['']:
    pass
else:
    with more_details:
        st.write("\n")
        st.write("\n")
        if user_input == ['']:
            pass
        else:
            st.write("More Details")
            st.table(df[['Q', 'Prediction', 'Score']].assign(hack='').set_index('hack'))

about_section = st.beta_container()

with about_section:
    st.header("About")
    st.text("This application utilizes BERT for question answering.")
    st.write("\n")


