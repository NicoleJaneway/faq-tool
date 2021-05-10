import streamlit as st
import numpy as np
import pandas as pd
import requests

base_questions = pd.read_csv('data/faqs.csv')

def encode(j_data):
    url = 'http://localhost:8125/encode'
    return requests.post(url, json=j_data)

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

def init():
    questions = base_questions["Question"].values.tolist()
    json_response = encode({ 'id': 456, 'texts': questions }).json()
    results = np.array(json_response.get('result'))
    np.save("questions", results)
    questions_encoder_len = np.sqrt(
        np.sum(results * results, axis=1)
    )
    np.save("questions_len", questions_encoder_len)

init()

def get(q, min_score = 0.9):
    json_response = encode({'id': 567, 'texts': q}).json()
    print(json_response)
    query_vector = np.array(json_response.get('result'))

    score = np.sum((query_vector * np.load("questions.npy")), axis=1) / (
        np.load("questions_len.npy") * (np.sum(query_vector * query_vector) ** 0.5)
    )
    top_id = np.argsort(score)[::-1][0]

    data = pd.read_csv('data/faqs.csv')
    q_data = data["Question"].values.tolist()
    a_data = data["Answer"].values.tolist()

    if float(score[top_id]) > min_score:
        return [q[0], a_data[top_id], score[top_id], q_data[top_id]]
    return [ q[0], "Sorry, I didn't get you.", score[top_id], q_data[top_id] ]

with header:
    st.title("Atlas Research Question Answering Tool")

with text_input:
    st.header("Question Input")
    user_input = [st.text_area("Enter your question here:", value="", height=200)]
    if user_input == ['']:
        pass
    else:
        print(user_input)

with text_output:
    st.header("Suggested Answer")
    st.markdown('<p class="little-font">Copy your answer here:</p>', unsafe_allow_html=True)

    if user_input == ['']:
        pass
    else:
        # st.write(get(user_input))
        # st.write(type(get(user_input)))
        df = pd.DataFrame([get(user_input)], columns=["Q", "A", "Score", "Prediction"])
        # st.write(df)
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