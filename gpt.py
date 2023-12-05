import pdf
from openai import OpenAI

def askgpt (messages):
    client = OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages
    )
    summary = response.choices[0].message.content.strip()
    return summary

if __name__ == "__main__":
    messages = [{"role":"system","content":"Du bist ein Businessplanersteller."}]
    text_pdf = pdf.main()
    messages += [{"role":"user","content":"Hier ist die Vorlage die du befüllen sollst: \n"+text_pdf+ "\n Stelle mir soviele Fragen wie du benötigst um den bestmöglichen Businessplan für mein Unternehmen zu erstellen."}]
    while True:
        temp = askgpt(messages)
        messages += [{"role":"assistant","content":temp}]
        print(temp)
        i = input("Eingabe: \n") 
        messages += [{"role":"user","content":i}]
"""
evangelosntoumpas@AirvonEvangelos ~ % cd code
evangelosntoumpas@AirvonEvangelos code % cd Businessplan-AI
evangelosntoumpas@AirvonEvangelos Businessplan-AI % source env/bin/activate
(env) evangelosntoumpas@AirvonEvangelos Businessplan-AI % python gpt.py 
Please enter the path for the pdf: 
/Users/evangelosntoumpas/Desktop/Businessplan-Vorlage-Textteil.pdf
"""