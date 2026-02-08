import streamlit as st

def set_page_config(page_title:str, layout:str="wide"):
    st.set_page_config(page_title=page_title, layout=layout, page_icon="assets/app_logo.png")

def attach_custom_css():
    st.logo(
        icon_image="assets/app_logo.png",
        image="assets/app_title.png",
        link="https://technotes.devdanish.in"
    )
    st.sidebar.markdown(
        """
        <style>
        
            /* Sidebar link styling */
            div[data-testid="stSidebarUserContent"] ul {
                width: 100%;
                color: var(--text-color) !important;
            }
            div[data-testid="stSidebarUserContent"] a {
                color: var(--text-color);
                opacity: 0.75;
                text-decoration: none;
                font-weight: 500;
                font-size: 0.875rem;
                padding: 0.25rem 0;
                display: inline-block;
                border-left: 0.3rem solid transparent;
                padding-left: 0.5rem;
                transition: all 0.15s ease-in-out;
                border-radius: 0.5rem;
                width: 100%;            
            }
    
            /* Hover state */
            div[data-testid="stSidebarUserContent"] a:hover {
                color: var(--primary-color);
                border-left-color: teal;
                padding-left: 1rem;
                background-color: rgba(0, 0, 0, 0.03);
            }
            h1, h2, h3, h4 {
                color: teal !important;
            }
            
            button p {
                    color: teal !important;
                    font-weight: 600;
            }
        
            /* Dark mode hover fix */
            @media (prefers-color-scheme: dark) {
                div[data-testid="stSidebarUserContent"] a:hover {
                    border-left-color: MediumAquaMarine;
                    background-color: rgba(255, 255, 255, 0.05);
                }
                h1, h2, h3, h4{
                    color: MediumAquaMarine !important;
                }
                p, .stText>span, ul {
                    color: #cfcdca !important;
                }
                button p {
                    color: MediumAquaMarine !important;
                    font-weight: 600;
                }            
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def add_navigation(previous_page_title:str = None,
                   previous_page:str = None,
                   next_page_title:str = None,
                   next_page:str = None):

    st.divider()

    if previous_page and next_page:
        previous_col, x, next_col = st.columns(3)

        if previous_page:
            with previous_col:
                if st.button(f":material/arrow_back_ios: Previous : {previous_page_title}"):
                    prev_page_path = f"pages/{previous_page}" if previous_page[0].isdigit() else previous_page
                    st.switch_page(prev_page_path)

        if next_page:
            with next_col:
                if st.button(f"Next : {next_page_title} :material/arrow_forward_ios:"):
                    next_page_path = f"pages/{next_page}" if next_page[0].isdigit() else next_page
                    st.switch_page(next_page_path)
    else:
        if previous_page:
            if st.button(f":material/arrow_back_ios: Previous : {previous_page_title}"):
                prev_page_path = f"pages/{previous_page}" if previous_page[0].isdigit() else previous_page
                st.switch_page(prev_page_path)
        if next_page:
            if st.button(f"Next : {next_page_title} :material/arrow_forward_ios:"):
                next_page_path = f"pages/{next_page}" if next_page[0].isdigit() else next_page
                st.switch_page(next_page_path)