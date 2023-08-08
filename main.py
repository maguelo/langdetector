from langtoolkit.config import BASE_PATH
from langtoolkit.lang import load_data

if __name__ == "__main__":
    # print(ROOT_PATH)
    print(BASE_PATH)
    print(load_data().keys())
    print(load_data()['es'][:10])
    print(load_data()['en'][:10])
