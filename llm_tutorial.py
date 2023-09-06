from secret_key import secret_key
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

os.environ["OPENAI_API_KEY"] = secret_key

llm = OpenAI(temperature=0.6)


def generate_controls(risk, num_controls):
    prompt_teamplate_name = PromptTemplate(
        input_variables=["risk", "num_controls"],
        template="Imagine you are an Operational Risk Officer. Suggest me {num_controls} controls for {risk} risk. Please present the data in an html table format with control title in first column and their description in second column. Please take some time to think and then provide complete output.",
    )
    # print(prompt_teamplate_name.format(risk="Mexican"))
    name_chain = LLMChain(llm=llm, prompt=prompt_teamplate_name, output_key="controls")

    # prompt_template_information = PromptTemplate(
    #     input_variables=["controls"],
    #     template="Provide me a list of 5 policies that {controls} must follow. Please provide 2 lines worth of information about them as well. Please make each point is separated by @ symbol.",
    # )

    # item_chain = LLMChain(
    #     llm=llm, prompt=prompt_template_information, output_key="policies"
    # )

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=["risk", "num_controls"],
        output_variables=["controls"],
    )

    response = chain({"risk": risk, "num_controls": num_controls})

    return response


if __name__ == "__main__":
    print(generate_controls(risk="Whistleblowing", num_controls="2"))
