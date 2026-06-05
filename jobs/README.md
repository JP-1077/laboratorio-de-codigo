# Jobs - Scripts de Execução Agendada

Pasta destinada para alojar scripts de jobs que executam tarefas agendadas ou em background.

## 📖 Visão Geral

O módulo **Jobs** contém scripts autônomos que executam tarefas periódicas ou agendadas de forma independente. Esses scripts são projetados para rodar em background, coletar dados, processar informações ou sincronizar sistemas.

### Scripts Disponíveis

| Script | Descrição | Status |
|--------|-----------|--------|
| `captura_metricas.py` | Coleta e processa métricas do projeto | 🔄 Em desenvolvimento |
| `sincronizar_dados.py` | Sincroniza dados entre sistemas | 🔲 Planejado |
| `limpeza_cache.py` | Remove arquivos temporários | 🔲 Planejado |
| `notificacao_alertas.py` | Envia alertas e notificações | 🔲 Planejado |

## 🎯 Objetivo dos Jobs

### 📊 captura_metricas.py

**Objetivo**: Coletar, processar e armazenar métricas do projeto em intervalos regulares.

**Responsabilidades**:
- ✅ Escaneia estrutura de diretórios do projeto
- 📈 Conta exercícios resolvidos por categoria
- 🔍 Coleta informações de commits e alterações
- 💾 Armazena dados em banco de dados ou arquivo
- 📊 Calcula estatísticas agregadas
- 🎯 Fornece dados para o dashboard visualizar

**Métricas Capturadas**:
- Quantidade total de exercícios resolvidos
- Distribuição por plataforma (Beecrowd, LeetCode)
- Distribuição por categoria (lógica, estruturas, etc)
- Última atualização por categoria
- Progresso geral do projeto
- Histórico temporal de métricas

### 🔄 sincronizar_dados.py (Futuro)

**Objetivo**: Sincronizar dados entre diferentes fontes e manter consistência.

**Responsabilidades**:
- Sincronizar com repositório remoto
- Atualizar banco de dados
- Manter cache atualizado

### 🧹 limpeza_cache.py (Futuro)

**Objetivo**: Manter o projeto limpo removendo arquivos temporários.

**Responsabilidades**:
- Remover cache do Python
- Limpar arquivos temporários
- Otimizar espaço em disco

## 🚀 Como Executar

### Pré-requisitos

Instale as dependências necessárias:

```bash
# Dependências gerais do projeto
pip install -r requirements.txt

# Para jobs específicos (se houver)
pip install schedule  # Para agendamento
pip install python-dotenv  # Para variáveis de ambiente
```

### Executar Job Manualmente

#### captura_metricas.py

```bash
# Execução simples
python jobs/captura_metricas.py

# Com output detalhado
python jobs/captura_metricas.py --verbose

# Forçar atualização completa
python jobs/captura_metricas.py --force

# Modo dry-run (simula sem salvar)
python jobs/captura_metricas.py --dry-run
```

### Executar Todos os Jobs

```bash
# Executa todos os jobs uma vez
python -m jobs.runner

# Executa em modo scheduler (contínuo)
python jobs/scheduler.py
```

### Agendar Jobs com Cron (Linux/macOS)

```bash
# Editar crontab
crontab -e

# Executar captura_metricas a cada hora
0 * * * * cd /path/to/projeto && python jobs/captura_metricas.py

# Executar a cada 30 minutos
*/30 * * * * cd /path/to/projeto && python jobs/captura_metricas.py

# Executar diariamente às 00:00
0 0 * * * cd /path/to/projeto && python jobs/captura_metricas.py
```

### Agendar Jobs com Task Scheduler (Windows)

```batch
# Criar tarefa agendada
schtasks /create /tn "CapturaMétricas" /tr "python C:\caminho\jobs\captura_metricas.py" /sc hourly

# Executar a cada 30 minutos
schtasks /create /tn "CapturaMétricas" /tr "python C:\caminho\jobs\captura_metricas.py" /sc minute /mo 30
```

### Agendar com APScheduler (Python)

```python
# jobs/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from captura_metricas import main

scheduler = BackgroundScheduler()

# Executar a cada hora
scheduler.add_job(main, 'interval', hours=1)

# Executar diariamente às 00:00
scheduler.add_job(main, 'cron', hour=0, minute=0)

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    scheduler.shutdown()
```

## 📊 Saída dos Jobs

### captura_metricas.py

#### Arquivos Gerados

```
projeto/
├── data/
│   ├── metricas.json          # Última snapshot de métricas
│   ├── metricas_historico.csv # Histórico temporal
│   └── relatorio.txt          # Relatório textual
└── logs/
    └── captura_metricas.log   # Log de execução
```

#### Formato da Saída JSON

```json
{
  "timestamp": "2026-06-05T14:30:00Z",
  "total_exercicios": 24,
  "por_plataforma": {
    "beecrowd": {
      "total": 24,
      "por_categoria": {
        "logica": 19,
        "sql": 5
      }
    },
    "leetcode": {
      "total": 0,
      "por_categoria": {}
    }
  },
  "ultima_atualizacao": {
    "beecrowd": "2026-06-05T12:00:00Z",
    "leetcode": null
  },
  "progresso": {
    "completo": 24,
    "em_progresso": 0,
    "planejado": 0,
    "percentual": 100.0
  }
}
```

#### Formato do CSV Histórico

```csv
timestamp,plataforma,total_exercicios,categoria,quantidade,percentual
2026-06-05 14:30:00,beecrowd,24,logica,19,79.17
2026-06-05 14:30:00,beecrowd,24,sql,5,20.83
2026-06-05 14:00:00,beecrowd,24,logica,19,79.17
2026-06-05 14:00:00,beecrowd,24,sql,5,20.83
```

#### Relatório em Texto

```
═══════════════════════════════════════════════════════
          RELATÓRIO DE MÉTRICAS DO PROJETO
═══════════════════════════════════════════════════════

📊 RESUMO GERAL
  Total de Exercícios: 24
  Última Atualização: 2026-06-05 14:30:00

🎯 DISTRIBUIÇÃO POR PLATAFORMA
  ├─ Beecrowd: 24 exercícios (100%)
  │  ├─ Lógica: 19 (79.17%)
  │  └─ SQL: 5 (20.83%)
  └─ LeetCode: 0 exercícios (0%)

📈 PROGRESSO TOTAL: 100%

═══════════════════════════════════════════════════════
```

#### Log de Execução

```log
2026-06-05 14:30:00 INFO  - Iniciando captura de métricas
2026-06-05 14:30:01 INFO  - Escaneando diretório: app/beecrownd/logica/
2026-06-05 14:30:01 INFO  - Encontrados 19 arquivos Python
2026-06-05 14:30:02 INFO  - Escaneando diretório: app/beecrownd/sql/
2026-06-05 14:30:02 INFO  - Encontrados 5 arquivos SQL
2026-06-05 14:30:03 INFO  - Processando dados...
2026-06-05 14:30:04 INFO  - Salvando em data/metricas.json
2026-06-05 14:30:05 INFO  - Atualizando histórico CSV
2026-06-05 14:30:06 INFO  - ✅ Captura concluída com sucesso (6s)
```

### Banco de Dados (se aplicável)

#### Tabela de Métricas

```sql
CREATE TABLE metricas (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    plataforma VARCHAR(50),
    categoria VARCHAR(50),
    total_exercicios INTEGER,
    exercicios_resolvidos INTEGER,
    percentual DECIMAL(5,2),
    INDEX idx_timestamp (timestamp),
    INDEX idx_plataforma (plataforma)
);
```

## 🔧 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Configuração de Jobs
JOB_SCHEDULE_INTERVAL=3600  # Em segundos (1 hora)
JOB_LOG_LEVEL=INFO
JOB_OUTPUT_FORMAT=json      # json, csv, txt

# Banco de dados
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=senha
DB_NAME=metricas

# Notificações (opcional)
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
EMAIL_RECIPIENT=usuario@example.com
```

## 📝 Estrutura de um Job

### Template de Novo Job

```python
# jobs/seu_novo_job.py
import logging
from datetime import datetime
from typing import Any, Dict

logger = logging.getLogger(__name__)

def configurar_logging():
    """Configura logging para o job"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/seu_job.log'),
            logging.StreamHandler()
        ]
    )

def main(verbose=False, dry_run=False) -> Dict[str, Any]:
    """
    Função principal do job.
    
    Args:
        verbose: Saída detalhada
        dry_run: Simula sem fazer mudanças
    
    Returns:
        Dicionário com resultado da execução
    """
    configurar_logging()
    
    logger.info("Iniciando seu_novo_job")
    
    try:
        # Sua lógica aqui
        resultado = {
            "status": "sucesso",
            "timestamp": datetime.now().isoformat(),
            "dados": {}
        }
        
        logger.info(f"✅ Job concluído com sucesso")
        return resultado
        
    except Exception as e:
        logger.error(f"❌ Erro ao executar job: {e}")
        return {"status": "erro", "mensagem": str(e)}

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Seu novo job")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    
    args = parser.parse_args()
    main(verbose=args.verbose, dry_run=args.dry_run)
```

---

## 📚 Recursos Úteis

- 📖 **APScheduler**: [apscheduler.readthedocs.io](https://apscheduler.readthedocs.io/)
- 🐧 **Cron Syntax**: [crontab.guru](https://crontab.guru/)
- 🪟 **Task Scheduler**: [docs.microsoft.com](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)
- 📝 **Python Logging**: [docs.python.org/logging](https://docs.python.org/3/library/logging.html)

---

**Última atualização**: Junho 2026
