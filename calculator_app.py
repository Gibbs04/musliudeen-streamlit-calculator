import streamlit as st
import random

# App title
st.title("Fun Calculator + Guessing Game 🧮🎲")

# Tabs for the two features
tab1, tab2 = st.tabs(["Calculator", "Guessing Game"])

# ────────────────────────────────────────────────
# TAB 1: Calculator
# ────────────────────────────────────────────────
with tab1:
    st.subheader("Simple Calculator")
    st.write("Enter two numbers and pick an operation!")

    num1 = st.number_input("First number", value=0, step=1)
    num2 = st.number_input("Second number", value=0, step=1)

    operation = st.radio(
        "Choose operation:",
        ("+", "-", "×", "÷")
    )

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
                st.error("Cannot divide by zero! 😅")
            else:
                result = num1 / num2
                # Show as whole number if it's actually whole
                if result.is_integer():
                    st.success(f"{num1} ÷ {num2} = **{int(result)}**")
                else:
                    st.success(f"{num1} ÷ {num2} = **{result:.2f}**")  # keep 2 decimals only if needed

        # Little celebration for any successful calculation
        st.balloons()

# ────────────────────────────────────────────────
# TAB 2: Guessing Game
# ────────────────────────────────────────────────
with tab2:
    st.subheader("Number Guessing Game")

    # Initialize session state variables (so game remembers progress)
    if 'secret' not in st.session_state:
        st.session_state.secret = random.randint(1, 20)
        st.session_state.attempts_left = 5
        st.session_state.game_over = False
        st.session_state.message = ""

    # Show instructions and attempts
    st.write(f"I'm thinking of a number between **1 and 20**.")
    st.write(f"You have **{st.session_state.attempts_left}** guesses left.")

    # Guess input (only show if game not over)
    if not st.session_state.game_over:
        guess = st.number_input("Your guess:", min_value=1, max_value=20, step=1)

        if st.button("Submit Guess"):
            if guess == st.session_state.secret:
                st.success(f"Yes! You got it! The number was {st.session_state.secret} 🎉")
                st.balloons()           # Celebration!
                st.session_state.game_over = True
            elif guess < st.session_state.secret:
                st.warning("Too low! Try higher.")
                st.session_state.attempts_left -= 1
            else:
                st.warning("Too high! Try lower.")
                st.session_state.attempts_left -= 1

            # Check if out of attempts
            if st.session_state.attempts_left == 0 and not st.session_state.game_over:
                st.error(f"Game over! The number was {st.session_state.secret} 😔")
                st.session_state.game_over = True

    # Play again button
    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.secret = random.randint(1, 20)
            st.session_state.attempts_left = 5
            st.session_state.game_over = False
            st.session_state.message = ""
            st.rerun()  # Refresh the page to reset
