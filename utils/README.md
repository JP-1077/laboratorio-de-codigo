# Utils - Funções e Utilitários Reutilizáveis

Pasta destinada para alojar funções, classes e utilitários reutilizáveis em todo o projeto.

## 📖 Visão Geral

O módulo **Utils** centraliza código comum e reutilizável que é compartilhado entre diferentes partes do projeto. Isso inclui:

- ✅ **Funções auxiliares** — Lógica comum para manipulação de dados
- 🔄 **Conversores** — Transformação entre formatos e tipos
- 📊 **Processadores** — Tratamento e normalização de dados
- 🎨 **Formatadores** — Apresentação e saída de dados
- 🔍 **Validadores** — Verificação de entrada e integridade
- 📐 **Helpers Matemáticos** — Cálculos frequentes
- 📝 **Parsers** — Leitura e interpretação de dados
- 🔐 **Segurança** — Funções de criptografia e hash

**Objetivo**: Evitar duplicação de código e centralizar lógica reutilizável.

## 🔧 Módulos Disponíveis

### Estrutura Sugerida

```
utils/
├── README.md                    # Este arquivo
├── __init__.py                  # Exportações principais
├── helpers.py                   # Funções auxiliares gerais
├── validators.py                # Validadores de entrada
├── formatters.py                # Formatadores de saída
├── converters.py                # Conversões entre tipos
├── math_utils.py                # Utilitários matemáticos
├── string_utils.py              # Manipulação de strings
├── file_utils.py                # Operações com arquivos
├── decorators.py                # Decoradores úteis
└── constants.py                 # Constantes do projeto
```

### Módulos e Funções Propostos

#### `helpers.py` — Funções Auxiliares Gerais

| Função | Descrição | Assinatura |
|--------|-----------|-----------|
| `chunk_list()` | Divide lista em chunks | `chunk_list(lista, tamanho)` |
| `flatten()` | Achata listas aninhadas | `flatten(lista_aninhada)` |
| `remove_duplicates()` | Remove duplicatas preservando ordem | `remove_duplicates(lista)` |
| `merge_dicts()` | Mescla múltiplos dicionários | `merge_dicts(*dicts)` |
| `get_nested()` | Acessa valor aninhado com segurança | `get_nested(dict, chave.subchave)` |

#### `validators.py` — Validadores

| Função | Descrição |
|--------|-----------|
| `is_valid_email()` | Valida formato de email |
| `is_valid_cpf()` | Valida CPF brasileiro |
| `is_valid_number()` | Valida se é número |
| `is_empty()` | Verifica se está vazio |
| `has_min_length()` | Valida comprimento mínimo |

#### `formatters.py` — Formatadores de Saída

| Função | Descrição |
|--------|-----------|
| `format_currency()` | Formata como moeda |
| `format_date()` | Formata data |
| `format_number()` | Formata número com separadores |
| `truncate_text()` | Trunca texto com ellipsis |
| `highlight_text()` | Destaca partes de texto |

#### `converters.py` — Conversores

| Função | Descrição |
|--------|-----------|
| `string_to_int()` | Converte string para inteiro |
| `string_to_float()` | Converte string para float |
| `list_to_dict()` | Converte lista em dicionário |
| `dict_to_list()` | Converte dicionário em lista |
| `seconds_to_time()` | Converte segundos em HH:MM:SS |

#### `math_utils.py` — Utilitários Matemáticos

| Função | Descrição |
|--------|-----------|
| `factorial()` | Calcula fatorial |
| `fibonacci()` | Gera série Fibonacci |
| `gcd()` | Máximo divisor comum |
| `lcm()` | Mínimo múltiplo comum |
| `distance()` | Calcula distância entre pontos |

#### `string_utils.py` — Manipulação de Strings

| Função | Descrição |
|--------|-----------|
| `capitalize_words()` | Capitaliza cada palavra |
| `remove_special_chars()` | Remove caracteres especiais |
| `reverse_string()` | Inverte string |
| `count_words()` | Conta palavras |
| `extract_numbers()` | Extrai números de string |

#### `decorators.py` — Decoradores

| Decorador | Descrição |
|-----------|-----------|
| `@timer` | Mede tempo de execução |
| `@retry` | Tenta executar N vezes em caso de erro |
| `@cache` | Cacheia resultado de função |
| `@validate_types` | Valida tipos de argumentos |
| `@deprecated` | Marca função como descontinuada |

## 📚 Exemplos de Uso

### 1. Usando Helpers

```python
from utils.helpers import chunk_list, flatten, remove_duplicates

# Dividir lista em chunks
lista = [1, 2, 3, 4, 5, 6, 7, 8]
chunks = chunk_list(lista, 3)
# Resultado: [[1, 2, 3], [4, 5, 6], [7, 8]]

# Achatar lista aninhada
aninhada = [[1, 2], [3, [4, 5]], [6]]
flat = flatten(aninhada)
# Resultado: [1, 2, 3, 4, 5, 6]

# Remover duplicatas
lista_dup = [1, 2, 2, 3, 1, 4]
sem_dup = remove_duplicates(lista_dup)
# Resultado: [1, 2, 3, 4]
```

### 2. Usando Validadores

```python
from utils.validators import is_valid_email, is_valid_cpf, has_min_length

# Validar email
if is_valid_email("usuario@example.com"):
    print("Email válido!")

# Validar CPF
if is_valid_cpf("12345678901"):
    print("CPF válido!")

# Validar comprimento
if has_min_length("senha123", min_len=8):
    print("Senha atende requisitos!")
```

### 3. Usando Formatadores

```python
from utils.formatters import format_currency, format_date, truncate_text

# Formatar moeda
preco = 1234.50
print(format_currency(preco))  # R$ 1.234,50

# Formatar data
from datetime import datetime
data = datetime.now()
print(format_date(data, "%d/%m/%Y"))  # 05/06/2026

# Truncar texto
texto_longo = "Lorem ipsum dolor sit amet..."
print(truncate_text(texto_longo, 20))  # "Lorem ipsum dolor..."
```

### 4. Usando Conversores

```python
from utils.converters import seconds_to_time, string_to_int, list_to_dict

# Converter segundos para tempo
segundos = 3661
print(seconds_to_time(segundos))  # "01:01:01"

# Converter string para inteiro
numero = string_to_int("123")
print(numero)  # 123 (tipo int)

# Converter lista em dicionário
lista = [("a", 1), ("b", 2)]
dict_result = list_to_dict(lista)
# Resultado: {"a": 1, "b": 2}
```

### 5. Usando Decoradores

```python
from utils.decorators import timer, retry, cache

# Medir tempo de execução
@timer
def processar_dados(n):
    return sum(range(n))

processar_dados(1000000)
# Output: Tempo de execução: 0.045s

# Tentar 3 vezes em caso de erro
@retry(max_attempts=3, delay=1)
def conectar_api():
    # Tenta conectar até 3 vezes
    return requests.get("https://api.example.com")

# Cachear resultado
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(100)  # Muito mais rápido com cache!
```

### 6. Usando Math Utils

```python
from utils.math_utils import factorial, fibonacci, gcd, distance

# Calcular fatorial
print(factorial(5))  # 120

# Gerar Fibonacci
fib = fibonacci(10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# MDC
print(gcd(48, 18))  # 6

# Distância entre pontos
d = distance((0, 0), (3, 4))  # 5.0
```

## 🎯 Boas Práticas

1. **Funções Puras** — Evite side-effects, retorne valores sempre
2. **Type Hints** — Use type annotations para documentar tipos
3. **Documentação** — Adicione docstrings em todas as funções
4. **Testes** — Mantenha testes em `tests/utils/test_*.py`
5. **Nomes Descritivos** — Use nomes claros e autoexplicativos
6. **DRY** — Don't Repeat Yourself - reutilize funções

### Exemplo de Função Bem Estruturada

```python
def chunk_list(items: list, chunk_size: int) -> list:
    """
    Divide uma lista em chunks de tamanho especificado.
    
    Args:
        items: Lista a ser dividida
        chunk_size: Tamanho de cada chunk
    
    Returns:
        Lista de listas (chunks)
    
    Raises:
        ValueError: Se chunk_size for <= 0
    
    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size deve ser positivo")
    
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
```

## 📦 Como Importar

```python
# Importação específica
from utils.helpers import chunk_list
from utils.validators import is_valid_email

# Importação do módulo
from utils import helpers, validators

# Importação com alias
from utils.formatters import format_currency as fmt_money
```

---

## 📚 Recursos Úteis

- 📖 **Python Best Practices**: [peps.python.org](https://www.python.org/dev/peps/)
- 🧪 **Testing Utils**: [pytest.org](https://pytest.org/)
- 📝 **Type Hints Guide**: [mypy.readthedocs.io](https://mypy.readthedocs.io/)

---

**Última atualização**: Junho 2026
