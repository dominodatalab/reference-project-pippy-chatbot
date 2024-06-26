import random
import streamlit as st

def build_sidebar():
    popular_questions = [
        "Conda Virtual Environments in Compute Environments in Domino",
        "How to get workspace Logs And Support Bundle for 5.1 and Above",
        "Exotic IDE/VNC or Compute Environment Support - why is it not supported?",
        "How to set up Domino Model Monitoring (DMM) using the Domino API",
        "How to capture a HAR file from your Chrome web browser",
        "How to work with data in Domino",
        "How to sync files with MPI clusters in Domino",
        "How to exclude Project files from sync in Domino",
        "How can Domino help me build generative AI?",
        "How can I set a default Environment in Domino?",
        "Generate code for a custom metric to monitor Model toxicity",
        "What are the new features in Domino 5.10?",
    ]

    def insert_as_users_prompt(**kwargs):
        if prompt := kwargs.get("prompt"):
            st.session_state.messages.append({"role": "user", "content": prompt})

    def clear_chat_history():
        st.session_state.messages = [
            {"role": "assistant", "content": "How can I help you today?"}
        ]

    # App sidebar
    st.image("/mnt/code/assets/pippy.png", width=50)
    st.write(
        "<h1>Hi, I'm <font color='#ffcdc2'>Pippy</font> - your personal Domino Data Lab expert</h1>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("---")

    domino_docs_version = st.selectbox(
        "Domino Docs Version",
        (
            "Latest (5.9)", "5.8", "5.7", "5.6", "5.5", "5.4", "5.3", "5.2", "5.1", "5.0",
            "4.6", "4.5", "4.4", "4.3", "4.2", "4.1", 
            "3.6"
        ),
    )

    doc_category = st.selectbox(
        "Doc Category",
        ("All", "User Guide", "Admin Guide", "API Guide", "Release Notes"),
    )
    st.sidebar.markdown("---")

    st.write(
        "<h2>Ask me anything</h2>",
        unsafe_allow_html=True,
    )

    # Pick any 4 questions randomly from popular_questions
    selected_questions = random.sample(popular_questions, 4)

    for question in selected_questions:
        st.sidebar.button(
            question,
            on_click=insert_as_users_prompt,
            kwargs={"prompt": question},
            use_container_width=True,
        )
    st.sidebar.markdown("---")
    st.sidebar.button("Clear Chat History", on_click=clear_chat_history, type="primary")

    return domino_docs_version, doc_category
