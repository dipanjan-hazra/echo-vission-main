import streamlit as st
from src.database.db import delete_subject

@st.dialog("Delete Subject")
def delete_subject_warning_dialog(
    subject_id,
    subject_name
):

    st.error(
        f"Are you sure you want to permanently delete "
        f"'{subject_name}'?"
    )

    st.warning(
        "This action cannot be undone."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "No",
            width="stretch"
        ):
            st.rerun()

    with col2:
        if st.button(
            "Yes, Delete",
            type="primary",
            width="stretch"
        ):
            try:
                success = delete_subject(subject_id)

                if success:
                    st.success(
                        "Subject deleted successfully."
                    )

                    st.rerun()

            except Exception as e:

                print("Delete Error:", e)

                return False