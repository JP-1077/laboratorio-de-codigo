# Dashboard de Métricas

## 📖 Visão Geral

O **Dashboard de Métricas** é uma aplicação full-stack desenvolvida para monitorar e visualizar dados de progresso e performance. Ele coleta, processa e apresenta informações em tempo real sobre atividades, com uma arquitetura moderna separando backend, frontend e coleta de dados.

**Objetivo Principal**: Fornecer insights visuais sobre progresso, desempenho e padrões de uso através de gráficos interativos e métricas em tempo real.

## 🎯 Funcionalidades

- 📈 **Visualização de Métricas** — Gráficos e estatísticas em tempo real
- 🔄 **Coleta Automática de Dados** — Jobs agendados para capturar dados
- 💾 **Armazenamento de Dados** — Persistência e histórico de métricas
- 🎨 **Interface Intuitiva** — Frontend responsivo e amigável
- 🔌 **API REST** — Endpoints para acesso aos dados
- 📊 **Análises Agregadas** — Resumos e tendências de dados
- ⏱️ **Monitoramento Contínuo** — Acompanhamento em tempo real

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────┐
│            Frontend (React/Vue)                      │
│  - Componentes visuais                              │
│  - Gráficos e dashboards                            │
│  - Chamadas para API                                │
└──────────────────┬──────────────────────────────────┘
                   │
                   ↓ (HTTP/REST)
┌─────────────────────────────────────────────────────┐
│      Backend (Python/FastAPI)                       │
│  - API REST para gerenciar dados                    │
│  - Processamento de métricas                        │
│  - Autenticação e autorização                       │
│  - Endpoints em /api/metricas                       │
└──────────────────┬──────────────────────────────────┘
                   │
                   ↓ (Banco de Dados)
┌─────────────────────────────────────────────────────┐
│         Camada de Dados                             │
│  - Banco de dados (SQLite/PostgreSQL)               │
│  - Persistência de métricas                         │
│  - Histórico e agregações                           │
└─────────────────────────────────────────────────────┘
                   ↑
                   │ (Jobs de Captura)
┌─────────────────────────────────────────────────────┐
│    Jobs de Coleta de Dados                          │
│  - captura_metricas.py (Job agendado)               │
│  - Coleta de dados periódica                        │
│  - Processamento e normalização                     │
└─────────────────────────────────────────────────────┘
```

### Componentes

| Componente | Localização | Descrição |
|-----------|------------|-----------|
| **Frontend** | `frontend/` | Interface visual, gráficos e interação com usuário |
| **Backend** | `backend/app/` | API REST, lógica de negócio, processamento |
| **API Métricas** | `backend/app/api/metricas.py` | Endpoints específicos para dados de métricas |
| **Jobs** | `../jobs/captura_metricas.py` | Script de coleta automática de dados |
| **Banco de Dados** | (configurável) | Persistência de dados históricos |

## 📊 Métricas Coletadas

### Tipos de Métricas

| Métrica | Descrição | Frequência | Status |
|---------|-----------|-----------|--------|
| **Atividade de Código** | Commits, PRs, alterações | Por commit | 🔄 Em desenvolvimento |
| **Exercícios Resolvidos** | Quantidade e categoria | Diária | 🔄 Em desenvolvimento |
| **Performance** | Tempo de execução | Em tempo real | 🔄 Em desenvolvimento |
| **Progresso Plataforma** | Beecrowd, LeetCode, etc | Semanal | 🔄 Em desenvolvimento |
| **Tempo de Trabalho** | Horas dedicadas | Diária | 🔄 Em desenvolvimento |

### Fluxo de Coleta de Dados

```
1. Job (captura_metricas.py) executa periodicamente
   ↓
2. Coleta dados de múltiplas fontes
   ↓
3. Processa e normaliza informações
   ↓
4. Armazena no banco de dados
   ↓
5. Frontend consome via API REST
   ↓
6. Usuário visualiza gráficos e estatísticas
```

### Endpoints da API

- `GET /api/metricas/resumo` — Resumo geral de métricas
- `GET /api/metricas/detalhes` — Dados detalhados
- `GET /api/metricas/periodo` — Métricas em período específico
- `POST /api/metricas/capturar` — Força coleta manual

---
