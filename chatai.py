import g4f


def ask_gpt(prompt:str)->str:
        response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user","content": prompt}],
        )
        return response

while True:
        textuser = input(" ")
#       print(ask_gpt(textuser))
        if textuser=="exit":
                quit()
        else:
                print(ask_gpt(textuser))
