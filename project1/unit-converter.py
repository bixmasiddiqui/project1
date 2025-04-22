import streamlit as st

st.title("Unit Converter")

conversion_choice = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_choice == "Weight":
    weight_units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    input_value = st.number_input("Enter Weight Value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit:", list(weight_units.keys()))

    if st.button("Convert", key="weight_convert"):
        result = input_value * (weight_units[from_unit] / weight_units[to_unit])
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

    input_value = st.number_input("Enter Temperature Value:", format="%.2f")
    from_unit = st.selectbox("From Unit:", temperature_units, key="temp_from")
    to_unit = st.selectbox("To Unit:", temperature_units, key="temp_to")

    if st.button("Convert", key="temp_convert"):
        result = None

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (input_value * 9 / 5) + 32
            elif to_unit == "Kelvin":
                result = input_value + 273.15
            else:
                result = input_value

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (input_value - 32) * 5 / 9
            elif to_unit == "Kelvin":
                result = (input_value - 32) * 5 / 9 + 273.15
            else:
                result = input_value

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = input_value - 273.15
            elif to_unit == "Fahrenheit":
                result = (input_value - 273.15) * 9 / 5 + 32
            else:
                result = input_value

        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")
