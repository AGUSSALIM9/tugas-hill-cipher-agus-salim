def encrypt_hill(plaintext, key):
    if len(key) != 2 or any(len(row) != 2 for row in key):
        raise ValueError("Kunci harus berupa matriks 2x2.")

    text = "".join(character for character in plaintext.upper() if not character.isspace())
    if not text or not text.isascii() or not text.isalpha():
        raise ValueError("Plainteks harus berisi huruf A-Z.")

    if len(text) % 2:
        text += "X"

    ciphertext = []
    for index in range(0, len(text), 2):
        first = ord(text[index]) - ord("A")
        second = ord(text[index + 1]) - ord("A")
        encrypted_first = (key[0][0] * first + key[0][1] * second) % 26
        encrypted_second = (key[1][0] * first + key[1][1] * second) % 26
        ciphertext.append(chr(encrypted_first + ord("A")))
        ciphertext.append(chr(encrypted_second + ord("A")))

    return text, "".join(ciphertext)


def main():
    examples = [
        ("HILL CIPHER TIDAK SULIT", [[5, 6], [2, 3]]),
        ("SAYA PUSING", [[5, 8], [17, 3]]),
    ]

    print("=" * 54)
    print("TUGAS 3 - ENKRIPSI HILL CIPHER")
    print("Nama  : AGUS SALIM")
    print("NIM   : 524012001")
    print("Prodi : ILMU KOMPUTER")
    print("=" * 54)
    print("ENKRIPSI HILL CIPHER")
    print("Metode: Hill Cipher 2 x 2")
    print("Modulus: 26")
    print("Pemetaan: A = 0, B = 1, ..., Z = 25")
    print()

    for number, (plaintext, key) in enumerate(examples, start=1):
        prepared_text, ciphertext = encrypt_hill(plaintext, key)
        pairs = [
            prepared_text[index:index + 2]
            for index in range(0, len(prepared_text), 2)
        ]

        print(f"SOAL {number} - {plaintext}")
        print(f"Plainteks : {plaintext}")
        print(f"Matriks kunci: K = {key}")
        print("Rumus: C = K x P (mod 26)")
        print(f"Pembagian pasangan: {' - '.join(pairs)}")
        print("Spasi dihilangkan; setiap blok terdiri dari dua huruf.")
        print()

        for block_number, pair in enumerate(pairs, start=1):
            first = ord(pair[0]) - ord("A")
            second = ord(pair[1]) - ord("A")
            first_product = key[0][0] * first + key[0][1] * second
            second_product = key[1][0] * first + key[1][1] * second
            first_mod = first_product % 26
            second_mod = second_product % 26
            encrypted_pair = (
                chr(first_mod + ord("A")) + chr(second_mod + ord("A"))
            )

            print(f"Blok {block_number} ({pair})")
            print(
                f"Indeks plainteks: {pair[0]} = {first}, "
                f"{pair[1]} = {second}."
            )
            print(
                f"C = K x P (mod 26) = {key} x [[{first}], [{second}]]"
            )
            print(
                f"  = [[({key[0][0]} x {first}) + "
                f"({key[0][1]} x {second})], "
                f"[({key[1][0]} x {first}) + "
                f"({key[1][1]} x {second})]]"
            )
            print(f"  = [[{first_product}], [{second_product}]]")
            print(
                f"Modulo 26: {first_product} mod 26 = {first_mod}; "
                f"{second_product} mod 26 = {second_mod}."
            )
            print(
                f"Hasil huruf: {first_mod} = {encrypted_pair[0]}, "
                f"{second_mod} = {encrypted_pair[1]} -> {encrypted_pair}"
            )
            print()

        print(f"Cipherteks: {ciphertext}")
        print()

    print("KESIMPULAN")
    print(
        "1. HILL CIPHER TIDAK SULIT menghasilkan "
        "FMRDGCNZSHNKPGCWKVYV."
    )
    print("2. SAYA PUSING menghasilkan MUQSBDYSJF.")
    print(
        "Catatan: Determinan kunci soal pertama adalah 3 dan "
        "gcd(3, 26) = 1; determinan kunci soal kedua adalah "
        "-121 ≡ 9 (mod 26) dan gcd(9, 26) = 1. Karena kedua "
        "determinan memiliki invers modulo 26, kedua kunci dapat "
        "digunakan untuk enkripsi maupun dekripsi Hill Cipher."
    )


if __name__ == "__main__":
    main()
