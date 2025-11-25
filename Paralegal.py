import streamlit as st
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Zimbabwe Paralegal Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f3d7a;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2c5aa0;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .argument-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #2c5aa0;
    }
    .loophole-alert {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header">⚖️ Zimbabwe Paralegal Assistant</div>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a service:", 
    ["Motion Writer", "Contract Analyzer", "Case Strategy Advisor"])

# Sample data for demonstration
judges = ["Justice Chidyausiku", "Justice Malaba", "Justice Garwe", "Justice Gwaunza", "Justice Patel"]
case_types = ["Contract Dispute", "Land Dispute", "Employment", "Family Law", "Commercial"]
motion_templates = {
    "Contract Dispute": "application_for_summary_judgment",
    "Land Dispute": "urgent_application",
    "Employment": "reinstatement_application", 
    "Family Law": "maintenance_variation",
    "Commercial": "interdict_application"
}

if app_mode == "Motion Writer":
    st.markdown('<div class="section-header">📝 Motion Drafting Assistant</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        case_type = st.selectbox("Case Type", case_types)
        party_names = st.text_input("Party Names (e.g., Applicant vs Respondent)")
        case_number = st.text_input("Case Number")
        relief_sought = st.text_area("Relief Sought", placeholder="What are you asking the court to do?")
        
    with col2:
        facts_of_case = st.text_area("Facts of the Case", height=150)
        legal_basis = st.text_area("Legal Basis", placeholder="Constitutional provisions, statutes, case law...")
    
    if st.button("Generate Motion"):
        if party_names and relief_sought:
            st.success("✅ Motion Generated Successfully!")
            
            st.markdown("### 📄 Generated Motion Document")
            st.markdown(f"""
**IN THE HIGH COURT OF ZIMBABWE**
**HELD AT ZVISHAVANE MAGISTRATE COURT**

**CASE NO: {case_number if case_number else 'HC 1234/23'}**

**BETWEEN:**

**{party_names.split('vs')[0].strip() if 'vs' in party_names else party_names}** - APPLICANT

**AND**

**{party_names.split('vs')[1].strip() if 'vs' in party_names else 'RESPONDENT'}** - RESPONDENT

**APPLICATION IN TERMS OF {motion_templates.get(case_type, 'THE HIGH COURT RULES')}**

**BACKGROUND**
1. This is an application for {relief_sought.lower() if relief_sought else 'the relief set out below'}.
2. The material facts are as follows: {facts_of_case if facts_of_case else 'The applicant has a clear right to the relief sought.'}

**LEGAL BASIS**
3. The application is founded on {legal_basis if legal_basis else 'the common law and the High Court Act [Chapter 7:06]'}.

**PRAYER**
WHEREFORE the Applicant prays for an order that:
1. {relief_sought if relief_sought else 'The Respondent pay the sum claimed.'}
2. Costs of suit.
3. Further and/or alternative relief.

DATED at Harare this {datetime.now().strftime('%d')} day of {datetime.now().strftime('%B %Y')}.
            """)
            
            st.markdown("### 🎯 Three Possible Counter-Arguments")
            counter_arguments = [
                f"The respondent will likely argue that {party_names.split('vs')[0].strip() if 'vs' in party_names else 'the applicant'} has failed to establish a clear right.",
                f"A potential defense could be that the matter is not urgent and should follow normal court procedures.",
                f"The opposing party may contend that there are material disputes of fact that cannot be resolved on motion."
            ]
            
            for i, arg in enumerate(counter_arguments, 1):
                st.markdown(f'<div class="argument-box"><strong>Argument {i}:</strong> {arg}</div>', unsafe_allow_html=True)

elif app_mode == "Contract Analyzer":
    st.markdown('<div class="section-header">🔍 Contract Loophole Analyzer</div>', unsafe_allow_html=True)
    
    contract_text = st.text_area("Paste Contract Text Here:", height=200, 
        placeholder="Paste the contract text you want analyzed for loopholes and issues...")
    
    if st.button("Analyze Contract"):
        if contract_text:
            st.success("🔍 Analysis Complete!")
            
            # Simulated analysis based on common legal issues in Zimbabwe
            potential_issues = [
                "Ambiguous termination clauses that may not comply with the Labour Act",
                "Unclear dispute resolution mechanism - consider specifying Zimbabwean courts",
                "Potential violation of Consumer Contracts Act provisions",
                "Vague payment terms that could lead to contractual disputes",
                "Insufficient force majeure clause for Zimbabwean context"
            ]
            
            st.markdown("### ⚠️ Potential Loopholes & Issues")
            for issue in potential_issues:
                st.markdown(f'<div class="loophole-alert">{issue}</div>', unsafe_allow_html=True)
            
            st.markdown("### 💡 Recommended Fixes")
            fixes = [
                "Include specific timelines and notice periods for termination",
                "Specify that disputes will be resolved in Zimbabwean courts under Zimbabwean law",
                "Ensure all terms are fair and reasonable under the Consumer Contracts Act",
                "Define clear payment deadlines and consequences for late payment",
                "Expand force majeure to include load-shedding and forex unavailability"
            ]
            
            for fix in fixes:
                st.markdown(f"• {fix}")
        else:
            st.warning("Please paste contract text to analyze.")

elif app_mode == "Case Strategy Advisor":
    st.markdown('<div class="section-header">🎯 Case Strategy Advisor</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        presiding_judge = st.selectbox("Presiding Judge", judges)
        case_category = st.selectbox("Case Category", case_types)
        opponent_previous_motions = st.text_area("Opponent's Previous Motion Types", 
            placeholder="e.g., Exception applications, Summary judgment applications...")
    
    with col2:
        case_strengths = st.text_area("Your Case Strengths")
        case_weaknesses = st.text_area("Your Case Weaknesses")
        key_legal_issues = st.text_area("Key Legal Issues")
    
    if st.button("Generate Strategy"):
        st.success("🎯 Strategy Generated!")
        
        # Judge-specific advice (simulated)
        judge_approaches = {
            "Justice Chidyausiku": "Focus on constitutional arguments and fundamental rights",
            "Justice Malaba": "Emphasize precedent and established legal principles", 
            "Justice Garwe": "Prepare detailed factual analysis and evidence",
            "Justice Gwaunza": "Highlight gender and social justice aspects where applicable",
            "Justice Patel": "Focus on commercial practicality and business context"
        }
        
        st.markdown("### 👨‍⚖️ Judge-Specific Approach")
        st.info(judge_approaches.get(presiding_judge, "Focus on clear legal principles and evidence"))
        
        st.markdown("### 📊 Recommended Arguments")
        recommended_args = [
            f"Lead with your strongest point: {case_strengths.split('.')[0] if case_strengths else 'your factual evidence'}",
            "Anticipate and pre-emptively address the opponent's likely procedural challenges",
            f"Focus on the core legal issue: {key_legal_issues if key_legal_issues else 'the interpretation of relevant statutes'}"
        ]
        
        for i, arg in enumerate(recommended_args, 1):
            st.markdown(f"**{i}.** {arg}")
        
        st.markdown("### 🛡️ Defense Strategy")
        st.warning(f"Prepare to counter: {opponent_previous_motions if opponent_previous_motions else 'typical procedural objections in this case type'}")

# Footer
st.markdown("---")
st.markdown("*Disclaimer: This is a demonstration tool. Always consult with a qualified legal practitioner for actual legal advice.*")
