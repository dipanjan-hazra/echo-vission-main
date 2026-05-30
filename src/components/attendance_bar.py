import streamlit as st


def attendance_bar(percentage):

    percentage = max(0, min(float(percentage), 100))

    if percentage >= 75:
        bar_color = "#22c55e"
        status = "🟢 Safe Attendance"

    elif percentage >= 50:
        bar_color = "#f59e0b"
        status = "🟠 Attendance Needs Improvement"

    else:
        bar_color = "#ef4444"
        status = "🔴 Attendance Shortage"

    st.markdown(
        f"""
        <div style="
            margin-top:-10px;
            margin-bottom:20px;
            padding:12px;
            border-radius:12px;
            background:#fafafa;
            border:1px solid #e5e7eb;
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                margin-bottom:6px;
            ">
                <span><b>Attendance</b></span>
                <span><b>{percentage:.1f}%</b></span>
            </div>

            <div style="
                width:100%;
                height:12px;
                background:#e5e7eb;
                border-radius:20px;
                overflow:hidden;
            ">
                <div style="
                    width:{percentage}%;
                    height:100%;
                    background:{bar_color};
                    border-radius:20px;
                ">
                </div>
            </div>

            <div style="
                margin-top:8px;
                font-size:0.85rem;
                font-weight:600;
            ">
                {status}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )