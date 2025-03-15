import streamlit as st
import requests

def get_random_jokes():
    """Fetch random jokes from an Api"""
    try:
        res = requests.get("https://official-joke-api.appspot.com/random_joke")

        if res.status_code == 200:
            data  = res.json()
            return f"Joke: \t{data["setup"]}  \n \n PunchLine: \t{data["punchline"]}" 
        else:
            return "Failed to fetch data"
        
    except:
        return "Why did programer qit his job programmer \n because he did'nt get an array"
    

def main():
    st.title("Random jokes generator😂🎉")
    st.write("Click the below button to generate a joke")

    if st.button("Generate joke"):
        joke = get_random_jokes()
        st.success(joke)
    st.divider()
    


if __name__ == '__main__':
    main()