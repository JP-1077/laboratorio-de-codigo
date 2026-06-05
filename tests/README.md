# Testes

## 📖 Visão Geral

A estratégia de testes visa garantir a **qualidade e confiabilidade** das soluções implementadas. Os testes cobrem:

- ✅ **Validação de Saída** — Verifica se o resultado está correto
- 🔍 **Casos Extremos** — Testa entradas mínimas, máximas e inválidas
- ⚡ **Performance** — Valida complexidade de tempo e espaço
- 🐛 **Regressão** — Garante que mudanças não quebrem funcionalidades existentes
- 📋 **Cobertura de Código** — Objetivo: manter > 80% de cobertura

## 🎯 Escopo de Testes

| Categoria | Funcionalidades Testadas | Prioridade |
|-----------|--------------------------|-----------|
| **Lógica Básica** | Cálculos matemáticos, operações aritméticas | 🔴 Alta |
| **Processamento de Dados** | Strings, arrays, estruturas | 🔴 Alta |
| **Algoritmos** | Busca, ordenação, recursão | 🟡 Média |
| **Banco de Dados** | Consultas SQL, integridade | 🟡 Média |
| **API/Backend** | Endpoints, autenticação, validação | 🟡 Média |
| **Dashboard** | Visualização de métricas | 🟢 Baixa |

## 🏗️ Estrutura de Testes

```
tests/
├── README.md                          # Este arquivo
├── conftest.py                        # Configuração global do pytest
├── requirements-dev.txt               # Dependências de teste
├── beecrowd/
│   ├── __init__.py
│   ├── test_logica.py                 # Testes da categoria lógica
│   ├── test_sql.py                    # Testes de SQL
│   └── test_strings.py                # Testes de strings
├── leetcode/
│   ├── __init__.py
│   ├── test_arrays_strings.py         # Testes de arrays/strings
│   ├── test_trees.py                  # Testes de árvores
│   └── test_dp.py                     # Testes de programação dinâmica
├── dashboard/
│   ├── __init__.py
│   ├── test_api.py                    # Testes da API
│   └── test_metricas.py               # Testes de coleta de métricas
└── utils/
    ├── __init__.py
    ├── test_helpers.py                # Testes de funções auxiliares
    └── fixtures.py                    # Dados compartilhados entre testes
```

### Padrão de Nomenclatura

- **Arquivo**: `test_<modulo>.py`
- **Função**: `test_<funcionalidade>_<caso>`
- **Exemplo**: `test_soma_dois_valores_com_numeros_positivos()`

## 🧪 Como Executar

### Pré-requisitos

Instale as dependências de teste:
```bash
pip install -r tests/requirements-dev.txt
```

### Executar Todos os Testes

```bash
# Todos os testes com saída detalhada
pytest tests/ -v

# Com cobertura de código
pytest tests/ --cov --cov-report=html

# Modo watch (reexecuta testes quando arquivo muda)
pytest-watch tests/
```

### Executar Testes de um Módulo

```bash
# Apenas testes de Beecrowd
pytest tests/beecrowd/ -v

# Apenas testes de lógica
pytest tests/beecrowd/test_logica.py -v

# Um teste específico
pytest tests/beecrowd/test_logica.py::test_soma_dois_valores -v
```

### Criar Testes com Coverage

```bash
# Gera relatório HTML de cobertura
pytest tests/ --cov --cov-report=html

# Abre relatório no navegador
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS
```

### Executar com Marcadores

```bash
# Apenas testes rápidos
pytest tests/ -m "fast" -v

# Apenas testes lentos
pytest tests/ -m "slow" -v

# Excluir testes lentos
pytest tests/ -m "not slow" -v
```

## ➕ Como Adicionar Novos Testes

### 1. Criar Arquivo de Teste

Crie um arquivo `test_<nome>.py` na pasta apropriada:

```python
# tests/beecrowd/test_novo_modulo.py
import pytest
from app.beecrowd.logica import funcao_para_testar

class TestNovaFuncionalidade:
    """Suite de testes para nova funcionalidade"""
    
    def test_caso_basico(self):
        """Testa o caso básico esperado"""
        resultado = funcao_para_testar(entrada)
        assert resultado == esperado
    
    def test_caso_extremo_vazio(self):
        """Testa com entrada vazia"""
        resultado = funcao_para_testar([])
        assert resultado is None
    
    def test_caso_extremo_grande(self):
        """Testa com entrada grande"""
        entrada_grande = [1] * 10000
        resultado = funcao_para_testar(entrada_grande)
        assert len(resultado) == 10000
    
    @pytest.mark.parametrize("entrada,esperado", [
        (10, 100),
        (5, 25),
        (0, 0),
    ])
    def test_multiplos_casos(self, entrada, esperado):
        """Testa múltiplos casos com parametrização"""
        resultado = funcao_para_testar(entrada)
        assert resultado == esperado
```

### 2. Padrão AAA (Arrange-Act-Assert)

```python
def test_exemplo_aaa():
    # Arrange - Preparar dados
    entrada = [3, 1, 2]
    esperado = [1, 2, 3]
    
    # Act - Executar função
    resultado = ordenar(entrada)
    
    # Assert - Verificar resultado
    assert resultado == esperado
```

### 3. Usar Fixtures para Dados Compartilhados

```python
# tests/conftest.py
import pytest

@pytest.fixture
def entrada_padrao():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def entrada_vazia():
    return []

# tests/beecrowd/test_exemplo.py
def test_com_fixture(entrada_padrao):
    resultado = processar(entrada_padrao)
    assert len(resultado) == 5
```

### 4. Adicionar Marcadores (Markers)

```python
import pytest

@pytest.mark.fast
def test_rapido():
    assert True

@pytest.mark.slow
def test_lento():
    # Teste que demora mais tempo
    assert True

@pytest.mark.skip(reason="Funcionalidade não implementada")
def test_futuro():
    pass
```

### 5. Checklist para Novo Teste

- [ ] Arquivo criado em pasta correta (`tests/<categoria>/test_*.py`)
- [ ] Teste segue padrão AAA (Arrange-Act-Assert)
- [ ] Inclui pelo menos 3 casos: normal, extremo, erro
- [ ] Nomes descritivos de funções e variáveis
- [ ] Docstring explicando o que testa
- [ ] Executa com sucesso: `pytest tests/beecrowd/test_novo.py -v`
- [ ] Cobertura está acima de 80%

---

## 📚 Recursos Úteis

- 🐍 **Pytest Documentation**: [pytest.org](https://pytest.org/)
- 📖 **Testing Best Practices**: [python.readthedocs.io](https://docs.python-guide.org/writing/tests/)
- 🧪 **Unit Testing Guide**: [realpython.com/python-testing](https://realpython.com/python-testing/)

---

