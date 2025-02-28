import random
from faker import Faker
from fpdf import FPDF
import zipfile
import os

fake = Faker()

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Nota de Entrega', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_delivery_note(self, process_number, seller_address, delivery_address, product_quantity):
        self.add_page()
        self.set_font('Arial', '', 12)
        
        self.cell(0, 10, f'Número do Processo: {process_number}', 0, 1)
        self.cell(0, 10, f'Endereço da Empresa Vendedora: {seller_address}', 0, 1)
        self.cell(0, 10, f'Endereço de Entrega: {delivery_address}', 0, 1)
        self.cell(0, 10, f'Quantidade de Produtos: {product_quantity}', 0, 1)

def create_pdf(file_name, process_number, seller_address, delivery_address, product_quantity):
    pdf = PDF()
    pdf.add_delivery_note(process_number, seller_address, delivery_address, product_quantity)
    pdf.output(file_name)

def create_zip_with_pdf(vehicle_id):
    process_number = str(random.randint(100000, 999999))
    seller_address = fake.address().replace("\n", ", ")
    delivery_address = fake.address().replace("\n", ", ")
    product_quantity = random.randint(1, 100)
    
    pdf_file_name = f"{vehicle_id}_delivery_note_{process_number}.pdf"
    create_pdf(pdf_file_name, process_number, seller_address, delivery_address, product_quantity)
    
    zip_file_name = f"{vehicle_id}.zip"
    
    # Verificar se o arquivo ZIP já existe
    if os.path.exists(zip_file_name):
        with zipfile.ZipFile(zip_file_name, 'a') as zipf:
            zipf.write(pdf_file_name)
    else:
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            zipf.write(pdf_file_name)
    
    os.remove(pdf_file_name)
    
    return zip_file_name

# Exemplo de uso com dados aleatórios
vehicle_id = random.randint(100, 110)

zip_file_name = create_zip_with_pdf(vehicle_id)
print(f"Arquivo ZIP criado: {zip_file_name}")