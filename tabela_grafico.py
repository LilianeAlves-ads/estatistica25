import pandas as pd
import matplotlib.pyplot as plt


tabela = pd.DataFrame({
    'idade': [15, 32, 45, 54, 73 ],
    'nome': ['Ana', "Sara", 'Sofia', 'Helena', 'Jose']
})

plt.hist(tabela['idade'])
