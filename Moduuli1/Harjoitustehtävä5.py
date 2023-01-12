LUOTI_KERROIN = 13.3
NAULA_KERROIN = 32 * LUOTI_KERROIN
LEIVISKÄ_KERROIN = 20 * NAULA_KERROIN

leiviskätGrammoina = float(input("Anna leiviskät: ")) * LEIVISKÄ_KERROIN
naulatGrammoina = float(input("Anna naulat: ")) * NAULA_KERROIN
luoditGrammoina = float(input("Anna luodit: ")) * LUOTI_KERROIN

grammatyhteensä = leiviskätGrammoina + naulatGrammoina + luoditGrammoina
kilogrammat = int(grammatyhteensä / 1000)
grammat = float(grammatyhteensä % 1000)


print(f'Massa nykymittojen mukaan:\n{kilogrammat} kilogrammaa ja {round(grammat,3)} grammaa.')