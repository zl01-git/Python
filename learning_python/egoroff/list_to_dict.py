def get_word_indices(strings: list[str]) -> dict[str: list[int]]:
    strings_list = " ".join(strings)
    
    print(strings_list.split())

    pass

    # print(strings_list)



strings = ['Look at my horse', 'my horse', 'is amazing']
get_word_indices(strings)




# assert get_word_indices(['This is a string',
#                          'test String',
#                          'test',
#                          'string']) == {'this': [0], 'is': [0], 'a': [0],
#                                         'string': [0, 1, 3], 'test': [1, 2]}

# assert get_word_indices(['Look at my horse', 'my horse', 'is amazing']) == {
#     'look': [0], 
#     'at': [0], 
#     'my': [0, 1],
#     'horse': [0, 1], 
#     'is': [2], 
#     'amazing': [2]}

# assert get_word_indices([]) == {}

# assert get_word_indices(['Avada Kedavra',
#                          'avada kedavra',
#                          'AVADA KEDAVRA']) == {'avada': [0, 1, 2],
#                                                'kedavra': [0, 1, 2]}