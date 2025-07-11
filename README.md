# WhatsApp-Chat-Analyzer
📊 WhatsApp Chat Analyzer: Interactive Visualization Edition
Analyze and visualize your WhatsApp chat history like never before — with rich, dynamic charts, emoji usage, word clouds, and daily/monthly activity timelines in a clean 12-hour AM/PM format.

🚀 Project Highlights

✅ Built with Streamlit for a smooth and interactive user experience

✅ Uses matplotlib, seaborn, pandas, WordCloud, and emoji libraries

✅ Presents visually appealing stats and charts on WhatsApp chats

✅ Supports 12-hour AM/PM format for easy interpretation

✅ Great for group chats or individual conversations

📦 Features at a Glance

Feature	Description

📁 Upload Chat	Upload .txt exported WhatsApp chat file (without media)

🧮 Basic Stats	Message count, word count, media, and links shared

📆 Timelines	Monthly and daily chat activity trends

📈 Activity Heatmap	Weekly heatmap by time of day (in 12-hour AM/PM format)

🧑‍🤝‍🧑 Most Active Users	Ranking of most talkative users in the group

🌥️ Word Cloud	Visual of most used words excluding stopwords

🔤 Common Words	Horizontal bar chart of top 20 frequent words

😀 Emoji Stats	Table and pie chart of emoji usage

🛠 Tech Stack
 Python
 Streamlit
 Pandas
 Matplotlib
 Seaborn
 WordCloud
 Emoji
 URLExtract
 
📂 Folder Structure

📁 whatsapp-chat-analyzer/
├── app.py                 # Streamlit frontend
├── helper.py              # Logic for stats, wordcloud, emoji, heatmap etc.
├── preprocessor.py        # Parses WhatsApp txt data to structured DataFrame
├── stop_hinglish.txt      # Custom stopwords file (Hindi + English)
├── README.md              # You're reading this!
📥 How to Run Locally

Run the app

streamlit run app.py

📝 Export WhatsApp Chat

Open WhatsApp chat or group

Tap on ⋮ > More > Export chat

Select Without Media
Upload the .txt file into the app

📊 Example Visuals
(You can add screenshots here later)

📅 Monthly timeline of messages

🕒 Activity heatmap (12-hour format)

🌥 Word cloud
🔢 Emoji frequency
🔠 Most common words

💡 Future Ideas
Sentiment analysis of messages
Support Telegram/Instagram chats
Compare chats between users

👨‍💻 Author
Muhammad Ghous
🧠 AI Engineer | 📊 Data Analyst | 🗣️ NLP Enthusiast

📄 License
This project is licensed under the MIT License.
