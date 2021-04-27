mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml



wget https://storage.googleapis.com/bert_models/2018_10_18/cased_L-24_H-1024_A-16.zip
unzip ./cased_L-24_H-1024_A-16.zip
ls

pip install --upgrade pip --user

pip install bert-serving-server==1.10.0 --user
pip install bert-serving-client==1.10.0 --user
pip install tensorflow-cpu==1.15.0

bert-serving-start -model_dir=./cased_L-24_H-1024_A-16 -port=8080