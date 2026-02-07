import inspect
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent
DEFAULT_PAGE_ICON = "👨🏻‍💻"

PAGE_REGISTRY = [
    {"path": "Introduction.py", "title": "Introduction", "icon": ":material/home:"},
    {"path": "pages/headings.py", "title": "Headings", "icon": ":material/title:"},
    {"path": "pages/text_and_messaging.py", "title": "Text and Messaging", "icon": ":material/chat:"},
    {"path": "pages/structure_and_layout.py", "title": "Structure and Layout", "icon": ":material/dashboard:"},
    {"path": "pages/input_widgets.py", "title": "Input Widgets", "icon": ":material/tune:"},
    {"path": "pages/forms.py", "title": "Forms", "icon": ":material/edit_square:"},
    {"path": "pages/data_display.py", "title": "Data Display", "icon": ":material/bar_chart:"},
]


def build_navigation_pages():
    return [
        st.Page(page["path"], title=page["title"], icon=page["icon"])
        for page in PAGE_REGISTRY
    ]


def set_page_config(page_title: str, page_icon: str | None = None):
    icon = page_icon
    if icon is None:
        current_path = _infer_current_page_path()
        if current_path:
            page_index = _find_page_index(current_path)
            if page_index is not None:
                icon = PAGE_REGISTRY[page_index]["icon"]
    st.set_page_config(
        page_title=page_title,
        page_icon=icon or DEFAULT_PAGE_ICON,
        layout="wide",
    )


def _normalize_page_path(path: str) -> str:
    path_obj = Path(path)
    if path_obj.is_absolute():
        try:
            return path_obj.resolve().relative_to(ROOT_DIR).as_posix()
        except ValueError:
            return path_obj.name
    return path_obj.as_posix()


def _infer_current_page_path() -> str | None:
    frame = inspect.currentframe()
    if frame is None or frame.f_back is None or frame.f_back.f_back is None:
        return None
    return frame.f_back.f_back.f_code.co_filename


def _find_page_index(page_path: str) -> int | None:
    normalized_path = _normalize_page_path(page_path)
    for index, page in enumerate(PAGE_REGISTRY):
        if page["path"] == normalized_path:
            return index
    return None

def attach_custom_css():
    return st.sidebar.markdown(
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
            h1, h2, h3, h4, h5, h6 {
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
                h1, h2, h3, h4, h5, h6 {
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

def add_navigation(current_page: str | None = None):
    st.divider()

    page_path = current_page or _infer_current_page_path()
    if not page_path:
        return

    current_index = _find_page_index(page_path)
    if current_index is None:
        return

    previous_page = PAGE_REGISTRY[current_index - 1] if current_index > 0 else None
    next_page = PAGE_REGISTRY[current_index + 1] if current_index < len(PAGE_REGISTRY) - 1 else None

    if previous_page and next_page:
        previous_col, next_col = st.columns(2)
        with previous_col:
            if st.button(f"<- Previous : {previous_page['title']}"):
                st.switch_page(previous_page["path"])
        with next_col:
            if st.button(f"Next : {next_page['title']} ->"):
                st.switch_page(next_page["path"])
    else:
        if previous_page:
            if st.button(f"<- Previous : {previous_page['title']}"):
                st.switch_page(previous_page["path"])
        if next_page:
            if st.button(f"Next : {next_page['title']} ->"):
                st.switch_page(next_page["path"])
