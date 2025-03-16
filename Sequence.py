import streamlit as st

st.title('HELLO')

# Get values from user
a1 = st.number_input(label='A1', step=1)
a2 = st.number_input(label='A2', step=1)
a3 = st.number_input(label='A3', step=1)
n = st.number_input(label='Enter the term number (n)', min_value=1, value=1)

# Add a button to trigger calculations
if st.button('Calculate'):
    def check_sequence(a1, a2, a3):
        """
        This function checks if the sequence is an Arithmetic Progression (AP) or Geometric Progression (GP).
        Returns 'AP' if it's an arithmetic progression, 'GP' if it's a geometric progression, or None otherwise.
        """
        d1 = a2 - a1
        d2 = a3 - a2
        
        if d1 == d2:
            return 'AP'
        
        q1 = a2 / a1
        q2 = a3 / a2
        
        if q1 == q2:
            return 'GP'
        
        return None

    def arithmetic_progression(a1, a2, n):
        """
        Calculate the nth term of an arithmetic progression.
        Formula: a_n = a1 + (n - 1) * d
        """
        d = a2 - a1
        return a1 + (n - 1) * d

    def geometric_progression(a1, a2, n):
        """
        Calculate the nth term of a geometric progression.
        Formula: a_n = a1 * q^(n - 1)
        """
        q = a2 / a1
        return a1 * q ** (n - 1)

    sequence_type = check_sequence(a1, a2, a3)

    if sequence_type == 'AP':
        result = arithmetic_progression(a1, a2, n)
        st.latex(f"Arithmetic\ Progression:\ a_n = {result}")
    elif sequence_type == 'GP':
        result = geometric_progression(a1, a2, n)
        st.latex(f"Geometric\ Progression:\ a_n = {result}")
    else:
        st.write("The sequence is neither an Arithmetic Progression nor a Geometric Progression.")