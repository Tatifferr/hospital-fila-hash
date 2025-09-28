# 🏥 Sistema de Fila Hospitalar + Tabela Hash (Python)

![Python](https://img.shields.io/badge/python-3.11-blue.svg)

Este projeto implementa duas estruturas de dados em **Python** como atividade prática da disciplina **Estrutura de Dados / Programação III (2025)**:

1. **Fila Hospitalar com Lista Encadeada**  
   - Simula o atendimento em um hospital com base na prioridade de triagem.  
   - Cartões **Amarelos (A)** têm prioridade sobre **Verdes (V)**.  
   - Dentro da mesma cor, pacientes com menor número são atendidos primeiro.  
   - Funções: adicionar paciente, imprimir fila de espera, chamar próximo paciente.

2. **Tabela Hash de Estados**  
   - Estrutura que organiza os 26 estados brasileiros + Distrito Federal.  
   - Implementada com **tabela hash com encadeamento** (listas ligadas).  
   - Caso especial: **DF** sempre ocupa a posição 7.  
   - Inclui inserção de um estado fictício.

---

## 🚀 Tecnologias
- Python 3.11+  
- Estruturas de Dados: Lista Encadeada e Hashing  



## 📂 Estrutura do Projeto

hospital-fila-hash/
├─ src/
│  ├─ fila_hospitalar.py
│  ├─ tabela_hash_estados.py
├─ tests/
│  ├─ test_fila.py
│  └─ test_hash.py
├─ README.md
├─ LICENSE
├─ requirements.txt
└─ .gitignore



## Como Executar

Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/hospital-fila-hash.git
cd hospital-fila-hash

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows PowerShell
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python src/fila_hospitalar.py
python src/tabela_hash_estados.py

