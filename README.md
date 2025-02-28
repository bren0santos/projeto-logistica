# 📦 Análise de Entregas Logísticas

## Descrição do Projeto
Este projeto consiste em um script Python que analisa um arquivo Excel e uma pasta `.zip` contendo arquivos `.pdf`. O objetivo é verificar se a coluna "Entregas Realizadas" existe no arquivo Excel e, caso contrário, criá-la. Em seguida, compara-se a quantidade de arquivos `.pdf` em cada pasta `.zip` com os valores registrados na coluna "Total Entregas".

O estudo de caso foi realizado em um ambiente fictício de logística, onde foram criados 11 veículos com IDs de **100 a 110**, simulando entregas de produtos.

## 📌 Funcionalidades
- Verifica se a planilha **"Logística"** existe no arquivo Excel.
- Confirma a existência das colunas **"Total Entregas"** e **"ID_Veículo"**.
- Adiciona a coluna **"Entregas Realizadas"** caso não esteja presente.
- Lê os arquivos `.zip` contendo os PDFs das notas de entrega.
- Compara a quantidade de arquivos `.pdf` com o número registrado no Excel.
- Ordena os resultados de forma decrescente com base nas entregas realizadas.
- Exibe os resultados em uma interface gráfica interativa com **Tkinter**.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Tkinter** (Interface Gráfica)
- **Pandas** (Manipulação de Dados)
- **OpenPyXL** (Leitura e Escrita de Planilhas Excel)
- **Zipfile** (Manipulação de Arquivos ZIP)
- **FPDF** (Geração de PDFs)
- **Faker** (Geração de Dados Fictícios)

## 📂 Estrutura do Projeto
```
📁 projeto-logistica
│-- 📄 preenchimentoTabela_logistica.py  # Script para processar os dados do Excel e arquivos ZIP
│-- 📄 gerador_pdf.py           # Script para gerar PDFs fictícios das notas de entrega
│-- 📂 data                    # Pasta para armazenar os arquivos Excel e ZIPs
│-- 📄 README.md                # Documentação do projeto
```

## 🚀 Como Executar o Projeto
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/bren0santos/projeto-logistica.git
cd projeto-logistica
```

### 2️⃣ Instalar as Dependências
Antes de rodar os scripts, certifique-se de instalar as bibliotecas necessárias:
```bash
pip install pandas openpyxl fpdf faker
```

### 3️⃣ Executar o Gerador de PDFs (Opcional)
Caso queira gerar arquivos `.pdf` fictícios para testes:
```bash
python gerador_pdf.py
```
Isso criará um arquivo `.zip` com notas de entrega simuladas.

### 4️⃣ Executar o Script Principal
Para analisar os arquivos Excel e `.zip`:
```bash
python preenchimentoTabela_logistica.py
```
Isso abrirá a interface gráfica onde você pode selecionar os arquivos para análise.

## 📝 Formato dos Arquivos Gerados
Os arquivos `.pdf` seguem este padrão de nome:
```
ID_VEICULO_delivery_note_NUMEROPROCESSO.pdf
```
Exemplo:
```
105_delivery_note_123456.pdf
```

## 📊 Exemplo de Saída no Excel
| ID_Veículo | Total Entregas | Entregas Realizadas | Observação |
|------------|---------------|---------------------|------------|
| 100        | 15            | 15                  | OK         |
| 101        | 10            | 9                   | Faltando   |
| 102        | 12            | 12                  | OK         |

## 📌 Contribuição
Sinta-se à vontade para contribuir com melhorias no projeto! Para isso:
1. Faça um **fork** do repositório.
2. Crie um branch com a sua feature (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adicionando nova feature'`).
4. Envie para o repositório (`git push origin minha-feature`).
5. Abra um **Pull Request**.

## 📌 Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
Desenvolvido com 💡 por [Breno Santos](https://github.com/bren0santos) 🚀

