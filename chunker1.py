import nltk

def message_chunker(command):
    words = nltk.word_tokenize(command)
    tagged_tokens = nltk.pos_tag(words)
    output_command = ''
    regular_expression = r"""
                NP: {<NN|NNP|NNS>?<DT|PP\$>?<JJ>*<NN|NNS><IN>?<NN|NNP|NNS>+}
                {<VB>?<JJ>*<NNP|NN|NNS>+}
                """
    chunk = nltk.RegexpParser(regular_expression)
    sentence_tree = chunk.parse(tagged_tokens)
    sentence_tree.draw()
    for outer_subtree in sentence_tree.subtrees():
        if outer_subtree.label() == 'NP':
            for inner_subtree in outer_subtree:
                if inner_subtree[1] == 'NNP':
                    output_command += ' ' + inner_subtree[0]
                elif inner_subtree[1] == 'NNS':
                    output_command += ' ' + inner_subtree[0]
                elif inner_subtree[1] == 'NN':
                    output_command += ' ' + inner_subtree[0]
    output_command = output_command.strip()
    print(output_command)

#message_chunker('what is the location of delhi')
#message_chunker('define perception for me')
message_chunker('he accepted the position of vice chairman of Carlise group, a merchant banking concern')
