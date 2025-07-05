

from flask import Flask, jsonify 
import random
index=Flask(_name_)

q=["Success is not in what you have, but who you are. - Bo Bennett","Live out of your imagination, not your history. -Stephen Covey","Be the change that you wish to see in the world. —Mahatma Ghandi","Never bend your head. Always hold it high. Look the world straight in the eye. —Helen Keller","All our dreams can come true — if we have the courage to pursue them. —Walt Disney"]
@index.route('/q', methods=['GET'])
def get_quote():
    return jsonify({"quote": random.choice(q)})

if _name_ == "__main__":
    index.run(debug=True)