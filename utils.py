import streamlit as st

def get_custom_css():
    return st.sidebar.markdown(
        """
        <style>
        /* Sidebar link styling */
        div[data-testid="stSidebarUserContent"] a {
            color: var(--text-color);
            opacity: 0.75;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.875rem;
            padding: 0.25rem 0;
            display: inline-block;
            border-left: 3px solid transparent;
            padding-left: 0.5rem;
            transition: all 0.15s ease-in-out;
            border-radius: 0.5rem;
            width: 100%;

        }

        /* Hover state */
        div[data-testid="stSidebarUserContent"] a:hover {
            color: var(--primary-color);
            border-left-color: var(--primary-color);
            background-color: rgba(0, 0, 0, 0.03);
        }

        /* Dark mode hover fix */
        @media (prefers-color-scheme: dark) {
            div[data-testid="stSidebarUserContent"] a:hover {
                background-color: rgba(255, 255, 255, 0.05);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

