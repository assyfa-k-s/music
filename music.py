import sys
from time import sleep

def print_lyrics():
    # judul lagu
    print("=" * 40)
    print("<<< Pemuja Rahasia >>>".center(40))
    print("by : Sheila on 7".center(40))
    print("=" * 40)
    print() # baris kosong sebelum lirik

    lines = [
        ("akulah orang yang selalu menaruh bunga", 0.07),
        ("dan menuliskan cinta di atas meja kerjamu", 0.07),
        ("akulah orang yang kan selalu mengawasimu", 0.06),
        ("menikmati indahmu dari sisi gelapku", 0.09),
        ("dan biarkan aku jadi pemujamu", 0.06),
        ("jangan pernah hiraukan perasaan hatiku", 0.10),
        ("tenanglah, tenang, pujaan hatiku, sayang", 0.06),
        ("aku takkan sampai hati bila menyentuhmu", 0.07),
    ]

    delays = [0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char,end="")
            sys.stdout.flush()
            sleep(char_delay)

        print()
        sleep(delays[i])

print_lyrics()