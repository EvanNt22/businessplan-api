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
    a_pdf = pdf.main()
    #with open ("/Users/evangelosntoumpas/code/Businessplan-AI/DATA/Vorlage.txt","r") as f:
        #b_pdf = f.read()
    #with open ("/Users/evangelosntoumpas/code/Businessplan-AI/DATA/Vorlage.txt","r") as f:
        #c_pdf = f.read()

    with open ("/Users/evangelosntoumpas/code/Businessplan-AI/DATA/Vorlage.txt","r") as f:
        text_pdf = f.read()
    with open ("/Users/evangelosntoumpas/code/Businessplan-AI/DATA/Informationen.txt","r") as f:
        infos_pdf = f.read()
    #messages += [{"role":"user","content":"Hier sind einige Fragen \n"+text_pdf+" und dazugehörige Informationen \n"+infos_pdf+"& \n"+a_pdf+b_pdf+c_pdf+"+die dir helfen sollen den Businessplan zu erstellen. Erstell mir einen optimalen Businessplan. Solltest du noch fragen haben so schreibe mir eine Liste die ich dir beantworten soll."}]
    messages += [{"role":"user","content":"Hier sind einige Fragen \n"+text_pdf+" und dazugehörige Informationen \n"+infos_pdf+"& \n"+a_pdf+"+die dir helfen sollen den Businessplan zu erstellen. Erstell mir einen optimalen Businessplan. Solltest du noch fragen haben so schreibe mir eine Liste die ich dir beantworten soll."}]
    index = 0
    while True:
        temp = askgpt(messages)
        messages += [{"role":"assistant","content":temp}]
        print(temp)
        with open ("result"+str(index)+".txt","w") as f:
            f.write(temp)
            index+=1
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