from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from TextSummarization import TextSummarization
from nltk.tokenize import sent_tokenize
from check_similarity_bangla import SimilarityCheckBangla
from similarity_check import SimilarityCheck
from flask import request
app = Flask(__name__)
api = Api(app)

similarity = SimilarityCheckBangla()
english_similaity = SimilarityCheck()
english_similaity.load_file_of_vectors()

parser = reqparse.RequestParser()
parser.add_argument('article_one', type=str,required=True)
parser.add_argument('lan', type=str)
parser.add_argument('article_two', type=str,required=True)
class SimilarityCheckAPI(Resource):
    
    def get(self):   
        if(request.args.get('lan')[1:-1]=="eng"):
            df=english_similaity.get_similarity(request.args.get('article_one'),request.args.get('article_two'))
         
            return jsonify({'similariy_score':df})
        elif(request.args.get('lan')[1:-1]=="ban"):
            
            df=similarity.get_similarity_check(request.args.get('article_one'),request.args.get('article_two'))
         
            return jsonify({'similariy_score':df})
        
        return jsonify({'error':'invalid parameters parameters'})

    
    def post(self):
        similarity_argument = parser.parse_args()
            
        if(similarity_argument['lan']=='eng'):
            df=english_similaity.get_similarity(similarity_argument['article_one'],similarity_argument['article_two'])
            return jsonify({'summarized_text':df})
        
        elif(similarity_argument['lan']=='ban'):
            df=similarity.get_similarity_check(similarity_argument['article_one'],similarity_argument['article_two'])
            return jsonify({'similariy_score':df})

        return {"noting":"nothing"}
    
api.add_resource(SimilarityCheckAPI,'/')

if __name__ == "__main__":
    app.run()