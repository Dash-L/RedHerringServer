import numpy as np

class Markov:
    """An abstract data type to make markov chains"""

    def __init__(self, headlines):
        self.avg_len = sum([len(headline.split(' ')) for headline in headlines]) / len(headlines)
        self.headlines = headlines
        self.keys = self._populate_keys()

    def _populate_keys(self):
        """Each word to the words that come after it"""

        keys = {}
        headlines = self.headlines.copy() 
        for headline in headlines: 
            headline = headline.split(" ")
            
            # collecting words that start and end sentences
            try: keys["ending_words"].append(headline[-1]) 
            except KeyError: keys["ending_words"] = [headline[-1]]
            try: keys["starting_words"].append(headline[0])
            except KeyError: keys["starting_words"] = [headline[0]]

            for idx, word in enumerate(headline):
                if (idx+2 > len(headline)): break

                next_word = headline[idx+1]
                try: keys[word].append(next_word)
                except KeyError: keys[word] = [next_word]
        return keys

    def get_fake_headline(self):
        """Generating random strings from the keys"""

        markov = [np.random.choice(self.keys["starting_words"])]

        sentence_enders = self.keys["ending_words"]

        while not ((len(markov) > self.avg_len-2) and (markov[-1] in sentence_enders)):
            try: markov.append(np.random.choice(self.keys[markov[-1]]))
            except KeyError: break
        
        markov = " ".join(markov)

        return (markov if markov not in self.headlines 
        else self.get_fake_headline())

    def add_fakes(self, json):
        for _ in range(len(json['headlines'])):
            json['headlines'].append({ 'content': self.get_fake_headline(), 'real': False })
        return json