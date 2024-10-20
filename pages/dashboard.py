import streamlit as st
from helplines import helpline_list

st.title("Patient Strategy Management")

risk_level = st.selectbox("Select Patient Risk Level", ["Low", "Medium", "High"])

strategies = {
    "Low": [
        "Encourage peer-to-peer support meetings",
        "Suggest light physical activities (e.g., walking, yoga)",
        "Promote journaling and mindfulness practices"
    ],
    "Medium": [
        "Schedule regular counseling sessions",
        "Recommend joining online mental health communities",
        "Encourage participation in a mindfulness program"
    ],
    "High": [
        "Connect immediately to crisis helpline (Lifeline 13 11 14)",
        "Recommend post-natal support (PANDA 1300 726 306)",
        "Suggest immediate professional support (Kids Helpline 1800 551 800)"
    ]
}

st.write(f"Recommended Strategies for {risk_level} Risk Level:")
for strategy in strategies[risk_level]:
    st.write(f"- {strategy}")

regions = list(helpline_list.keys())
for i, tab in enumerate(st.tabs(regions)):
    with tab:
        region = regions[i]
        st.header(f"{region}")

for service, info in helpline_list[region].items():
            st.markdown(
                f"""
            **{service}**  
            Main areas: {", ".join(info["purpose"]).title()}  
            Contact: {info['contact_number']}
            """
            )
