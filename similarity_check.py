import gensim
# upgrade gensim if you can't import softcossim
from gensim.matutils import softcossim 
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess
import gensim
from gensim.matutils import softcossim 
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess

class SimilarityCheck:
    def __init__(self):
        self.__fasttext_model = 0
    def load_file_of_vectors(self):
        self.__fasttext_model = api.load('fasttext-wiki-news-subwords-300')
    
    def get_similarity(self,first_document,second_document):
        documents = [ first_document, second_document]
        dictionary = corpora.Dictionary([simple_preprocess(doc) for doc in documents])
        similarity_matrix = self.__fasttext_model.similarity_matrix(dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)
        
        sentences_of_first_document = dictionary.doc2bow(simple_preprocess(first_document))
        sentences_of_second_document = dictionary.doc2bow(simple_preprocess(second_document))

        sentences = [sentences_of_first_document, sentences_of_second_document]
        return softcossim(sentences_of_first_document, sentences_of_second_document, similarity_matrix)
        
    
