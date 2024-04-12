''' 
Author: Cole Barbes
Last edited: 03/27/2024
Analyze abstracts to determine a set of categories
'''
import openai
import random
import os
import json
#mport arxiv
#from nltk.corpus import wordnet

API_KEY = os.getenv('OPENAI_API_KEY')

# Here we define the various prompts we will need within this framework of analysis functions

format = """{ "Top-Level-Category" : { "mid-level-category": "low-level-category", "..."} }"""

format2 = """{
    'Computer Science': {
        'Machine Learning': 'Supervised Learning, Unsupervised Learning', 
        'Natural Language Processing': 'Named Entity Recognition, Sentiment Analysis', 
        'Computer Vision': 'Object Detection, Image Segmentation', 
        'Algorithms': 'Sorting Algorithms, Graph Algorithms'
    }, 
    'Health and Medicine': {
        'Public Health': 'Epidemiology, Health Policy', 
        'Medical Research': 'Clinical Trials, Genetics', 
        'Mental Health': 'Depression, Anxiety Disorders'
    }, 
    'Physics': {
        'Quantum Mechanics': 'Quantum Entanglement, Wave-Particle Duality', 
        'Astrophysics': 'Black Holes, Dark Matter', 
        'Condensed Matter Physics': 'Superconductivity, Semiconductors'
    }
}"""

class ResearchTaxonomy:
    def __init__(self, abstracts = [], prompt_num=0):
        self.prompt = [f"""
        You are an expert constructing a category taxonomy from an abstract to output JSON. \
        The output should be as follows: {format}
        Given a list of predefined categories and topics \
        Please find a hierarchy of topics 
        Output the taxonomy in JSON\
        <Parent Category> : <Child Category>, <Child Category> \
        This should be a concise category like Computer Science
        Only give about 5 or 6 categories, they should be categories from this site https://arxiv.org/category_taxonomy\
        The caregories should not be sentences
        Here is an example taxonomy:
        machine learning 1st level
        learning paradigms 2nd level
        cross validation 2nd level -> supervised learning 3rd level, unsupervised learning 3rd level
        heres how it should look
        {format2}
        """] 
        self.AbstractList = abstracts if len(abstracts) != 0 else ["Taxonomies represent hierarchical relations between entities, frequently applied in various software modeling and natural language processing (NLP) activities. They are typically subject to a set of structural constraints restricting their content. However, manual taxonomy construction can be time-consuming, incomplete, and costly to maintain. Recent studies of large language models (LLMs) have demonstrated that appropriate user inputs (called prompting)can effectively guide LLMs, such as GPT-3, in diverse NLP tasks without explicit (re-)training. However, existing approaches for automated taxonomy construc-tion typically involve fine-tuning a language model by adjusting model parameters.\In this paper, we present a general framework for taxonomy construction that takes into account structural constraints. We subsequently conduct a systematic comparison between the prompting and fine-tuning approaches performed on a hypernym taxonomy and a novel computer science taxonomy dataset. Our result reveals the following: (1) Even without explicit training on the dataset, the prompting approach outperforms fine-tuning-based approaches.Moreover, the performance gap between prompting and fine-tuning widens when the training dataset is small. However, (2) taxonomies generated by the fine-tuning approach can be easily post-processed to satisfy all the constraints, whereas handling violations of the taxonomies produced by the prompting approach can be challenging. These evaluation findings provide guidance on selecting the appropri-ate method for taxonomy construction and highlight potential enhancements for both approaches."]
        self.prompt_num = prompt_num if prompt_num <= len(self.prompt) else 0
    
    """
    This function prompts the openai api and returns the output
    Parameters: The message in open ai format, the model, the temperature, and the maximum token size
    Return: The output content in human readable format
    """
    def get_response(self, messages, model='gpt-3.5-turbo', temperature=0.5, max_tokens=500):
        response = openai.chat.completions.create(
            model=model,
            messages = messages, 
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    
    """
    This function creates a taxonomy of a random list of abstracts and outputs to json
    parameters: The abstract list, the prompt and the number of abstracts
    print to json file
    """
    def get_taxonomy_abstracts(self, num_iter=1):
        file_name = "Taxonomy.json"
        rand_index = random.randint(0, len(self.AbstractList))
        Abstract_range = self.AbstractList[rand_index:rand_index+num_iter]
        with open(file_name, 'w') as file:
            json_output = {}
            for abstract in Abstract_range:
                #print(abstract)
                messages = [
                    {'role':'system', 'content':self.prompt[self.prompt_num]},
                    {'role':'user', 'content': abstract},
                ]
                output_taxonomy = self.get_response(messages=messages)
                json_output[abstract] = json.loads(output_taxonomy)
            json.dump(json_output, file, indent=4)
        print("Taxonomy of abstracts Complete")
        return json_output
    
    """
    Function to reduce category taxonomy 

    """
    def get_reduced_taxonomy(self, Data):
        print(Data)




if __name__ == "__main__":
    with open('abstracts_to_categories.json', 'r') as file:
        data = json.load(file)
    abstract_list = [key for key, __ in data.items()]
    #print(abstract_list)
    category_list = [value for __, value in data.items()]
    Tester = ResearchTaxonomy()
    Taxonomy_Dict = Tester.get_taxonomy_abstracts()
    #print(Taxonomy_Dict)
    #Tester.get_reduced_taxonomy(Taxonomy_Dict)
    #print(Taxonomy_Dict)