import streamlit as st

st.title("Simple Calculator 🧮")
st.write("Enter two numbers and pick an operation!")

# Input fields (much nicer than text prompts!)
num1 = st.number_input("First number", value=0.0, step=1.0)
num2 = st.number_input("Second number", value=0.0, step=1.0)

# Radio buttons for operation
operation = st.radio(
    "Choose operation:",
    ("+", "-", "×", "÷")
)

# Calculate button
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
        st.success(f"{num1} + {num2} = **{result}**")
    
    elif operation == "-":
        result = num1 - num2
        st.success(f"{num1} - {num2} = **{result}**")
    
    elif operation == "×":
        result = num1 * num2
        st.success(f"{num1} × {num2} = **{result}**")
    
    elif operation == "÷":
        if num2 == 0:
            st.error("Error: Cannot divide by zero! 😅")
        else:
            result = num1 / num2
            st.success(f"{num1} ÷ {num2} = **{result}**")

# Optional: Add a fun footer
st.markdown("---")
st.caption("Built with Python & Streamlit – share with friends!")