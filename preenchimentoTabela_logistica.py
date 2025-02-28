import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
import zipfile
import os

def select_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        process_files(file_path)

def process_files(excel_file):
    # Ler todas as planilhas do arquivo Excel
    df_dict = pd.read_excel(excel_file, engine='openpyxl', sheet_name=None)
    
    # Selecionar a planilha "Logística"
    if 'Logística' not in df_dict:
        messagebox.showerror("Erro", "A planilha 'Logística' não foi encontrada no arquivo Excel.")
        return
    
    df = df_dict['Logística']
    
    # Exibir os nomes das colunas para depuração
    print("Colunas na planilha 'Logística':", df.columns)
    
    # Verificar se as colunas 'Total Entregas' e 'ID_Veículo' existem
    if 'Total Entregas' not in df.columns or 'ID_Veículo' not in df.columns:
        messagebox.showerror("Erro", "As colunas 'Total Entregas' e/ou 'ID_Veículo' não foram encontradas na planilha 'Logística'.")
        return
    
    # Adicionar a coluna 'Entregas Realizadas' se não existir
    if 'Entregas Realizadas' not in df.columns:
        df['Entregas Realizadas'] = 0
    
    # Pedir ao usuário para selecionar os arquivos zip
    zip_file_paths = filedialog.askopenfilenames(filetypes=[("Zip files", "*.zip")])
    if not zip_file_paths:
        return
    
    results = []
    
    for zip_file_path in zip_file_paths:
        # Obter o nome da pasta (número) a partir do caminho do arquivo zip
        folder_name = os.path.basename(zip_file_path).split('.')[0]
        
        try:
            folder_name_int = int(folder_name)
        except ValueError:
            results.append((folder_name, "N/A", "N/A", "não é um número válido."))
            continue
        
        # Verificar se o nome da pasta corresponde a algum valor na coluna 'ID_Veículo'
        if folder_name_int not in df['ID_Veículo'].values:
            results.append((folder_name, "N/A", "N/A", "não corresponde a nenhum valor na coluna 'ID_Veículo'."))
            continue
        
        # Obter o valor da coluna 'Total Entregas' correspondente ao ID do veículo
        total_entregas = df.loc[df['ID_Veículo'] == folder_name_int, 'Total Entregas'].iloc[0]
        
        # Contar o número de arquivos PDF no arquivo zip
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            pdf_files = [f for f in zip_ref.namelist() if f.endswith('.pdf')]
            total_pdfs = len(pdf_files)
        
        # Atualizar a coluna 'Entregas Realizadas'
        df.loc[df['ID_Veículo'] == folder_name_int, 'Entregas Realizadas'] = total_pdfs
        
        # Adicionar o resultado à lista de resultados
        results.append((folder_name, total_entregas, total_pdfs, ""))
    
    # Ordenar os resultados de maneira decrescente com base na coluna 'Entregas Realizadas'
    results.sort(key=lambda x: int(x[2]) if isinstance(x[2], int) else 0, reverse=True)
    
    # Exibir os resultados no display com rolagem
    for row in results:
        tree.insert("", tk.END, values=row)
    
    # Salvar apenas a planilha 'Logística' de volta ao arquivo Excel, mantendo todas as planilhas e formatações
    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        for sheet_name, sheet_df in df_dict.items():
            if sheet_name == 'Logística':
                sheet_df.update(df)
            sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

def sort_column(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

# Criar a janela principal
root = tk.Tk()
root.title("Analisador de Arquivos Logísticos")
root.geometry("800x600")

# Criar um rótulo e botão para selecionar o arquivo Excel
label = tk.Label(root, text="Selecione o arquivo Excel:")
label.pack(pady=10)

button = tk.Button(root, text="Selecionar Arquivo", command=select_excel_file)
button.pack(pady=10)

# Criar um frame para o display com rolagem
frame = ttk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Criar um Treeview para exibir os resultados em colunas
columns = ("ID_Veículo", "Total Entregas", "Entregas Realizadas", "Observação")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("ID_Veículo", text="ID_Veículo", command=lambda: sort_column(tree, "ID_Veículo", False))
tree.heading("Total Entregas", text="Total Entregas")
tree.heading("Entregas Realizadas", text="Entregas Realizadas")
tree.heading("Observação", text="Observação")

# Adicionar uma barra de rolagem ao Treeview
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Executar a aplicação
root.mainloop()