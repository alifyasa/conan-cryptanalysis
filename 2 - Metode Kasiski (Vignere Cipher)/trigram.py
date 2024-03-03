def get_all_repeated_trigram(ciphertext):
    trigram_pos = {}
    for i, y in enumerate(ciphertext):
        next_trigram = ciphertext[i:i+3]
        if(next_trigram in trigram_pos.keys()):
            trigram_pos[next_trigram] += [i+1]
        else:
            trigram_pos[next_trigram] = [i+1]
    repeated_list = list(filter(lambda x: len(trigram_pos[x]) > 1, trigram_pos))
    ret_trigram_pos = [(trigram, trigram_pos[trigram]) for trigram in repeated_list]
    return ret_trigram_pos

def get_all_each_distance(repeated_trigrams):
    distances_dict = {}
    for item in repeated_trigrams:
        key = item[0]
        array = item[1]
        distances = []
        for i in range(len(array) - 1):
            distance = array[i + 1] - array[i]
            distances.append(distance)
        distances_dict[key] = distances
    distances_list = [(key, value) for key, value in distances_dict.items()]
    return distances_list

def load_ciphertext(ciphertext_file = "ciphertext.txt"):
    with open(ciphertext_file, "r") as f:
        return ''.join(f.read().split())

def save_list_to_txt(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("Data saved successfully to", file_path)
    except Exception as e:
        print("Error occurred while saving data:", e)

if __name__ == "__main__":
    text = load_ciphertext()
    temp_all_repeated_trigram = get_all_repeated_trigram(text)
    sorted_data = sorted(temp_all_repeated_trigram, key=lambda x: len(x[1]), reverse=True)
    temp_trigram_distance = get_all_each_distance(sorted_data)
    save_list_to_txt("repeated_trigram.txt", sorted_data)
    save_list_to_txt("each_trigram_distance.txt", temp_trigram_distance)