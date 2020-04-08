from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
class SimilarityCheckBangla():
    def __init__(self):
        self.bangla_stopwords=""""""
        self.bangla_stopwords =[self.bangla_stopwords.split(",")] 
        
    @staticmethod
    def tokenize_news(news_in_bangla):
        
        news_in_bangla = news_in_bangla.split(".")
        sentences = []
        
        for sentence in news_in_bangla:
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        
         
        
        return sentences
   
    def sentence_similarity(self,sent1, sent2):
        if self.bangla_stopwords is None:
            self.bangla_stopwords = []
 
        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]
 
        all_words = list(set(sent1 + sent2))
 
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)
 
        for w in sent1:
            if w in self.bangla_stopwords:
                continue
            vector1[all_words.index(w)] += 1
 
        for w in sent2:
            if w in self.bangla_stopwords:
                continue
            vector2[all_words.index(w)] += 1
        return 1 - cosine_distance(vector1, vector2)


    def build_similarity_matrix(self,sentences,sentences2):
       
        arr  = []
        for idx1 in range(len(sentences[0])):
            for idx2 in range(len(sentences2[0])):
                max_num = -10
                
                if idx1 == idx2:
                    continue 
            	
                similarity_score = self.sentence_similarity(sentences[0][idx1], sentences2[0][idx2])
         
		
        if similarity_score>max_num:
            max_num = similarity_score
        arr.append(max_num)

        return arr
            
    def get_similarity_check(self,first_document,second_document):


        # Step 1 - Read text anc split it
        sentences =  SimilarityCheckBangla.tokenize_news(first_document)
        sentences2 =  SimilarityCheckBangla.tokenize_news(second_document)
        simmilarity_percentage = np.array(self.build_similarity_matrix(sentences,sentences2))
        return simmilarity_percentage.mean()
                