import pandas as pd

pizza = {'Nama': ['Agung Priyono', 'facturohman', 'Juan Fahrul Ambiyah', 'Kharisma Bima Sakti', 'Wahyu Purnomo Adi' ],
'Tinggi Badan': [164, 180, 170, 169, 181 ],
'Berat Badan' : [55, 60, 55, 59, 50]
}

pizza_df = pd.DataFrame(pizza)
pizza_df
print (pizza_df)