# Infra - Infraestrutura como Código

Pasta destinada para arquivos de configuração de infraestrutura, containers, orquestração e deployment.

## 📖 Visão Geral

O módulo **Infra** define toda a infraestrutura do projeto através de **Infraestrutura como Código (IaC)**. Isso significa que toda a configuração de ambientes, serviços, redes e recursos é versionada e reproducível.

### Benefícios da Abordagem IaC

- ✅ **Reproducibilidade** — Ambientes idênticos em qualquer lugar
- 📚 **Documentação Viva** — Configuração é a documentação
- 🔄 **Versionamento** — Histórico completo de mudanças
- 🚀 **Automatização** — Deploy com um comando
- 🔐 **Consistência** — Evita configurações manuais inconsistentes
- 📈 **Escalabilidade** — Fácil aumentar recursos
- 💰 **Otimização de Custos** — Provisionar exatamente o necessário

### Arquitetura Geral

```
┌─────────────────────────────────────────────────────┐
│           Ambiente de Desenvolvimento                │
│  Local com Docker Compose para testes                │
└──────────────┬──────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────┐
│          Ambiente de Staging (Opcional)              │
│  Servidor cloud para testes antes de produção        │
└──────────────┬──────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────┐
│        Ambiente de Produção                          │
│  Cloud provider (AWS, GCP, Azure, DigitalOcean)      │
└─────────────────────────────────────────────────────┘
```

## 🏗️ Componentes de Infraestrutura

### Estrutura de Pastas

```
infra/
├── README.md                              # Este arquivo
├── docker/
│   ├── Dockerfile                         # Imagem do aplicativo
│   ├── docker-compose.yml                 # Orquestração local
│   └── .dockerignore                      # Arquivos a ignorar
├── terraform/
│   ├── main.tf                            # Configuração principal
│   ├── variables.tf                       # Variáveis do Terraform
│   ├── outputs.tf                         # Saídas
│   ├── terraform.tfvars                   # Valores de variáveis
│   └── backend.tf                         # Configuração de estado
├── kubernetes/
│   ├── deployment.yml                     # Deployments K8s
│   ├── service.yml                        # Serviços
│   ├── ingress.yml                        # Ingress
│   └── configmap.yml                      # Configurações
├── ci-cd/
│   ├── .github/
│   │   └── workflows/
│   │       ├── test.yml                   # Pipeline de testes
│   │       └── deploy.yml                 # Pipeline de deploy
│   └── gitlab-ci.yml                      # Para GitLab CI
├── monitoring/
│   ├── prometheus.yml                     # Configuração Prometheus
│   ├── grafana-dashboards/                # Dashboards Grafana
│   └── alertas.yml                        # Regras de alerta
├── scripts/
│   ├── setup.sh                           # Setup inicial
│   ├── deploy.sh                          # Deploy script
│   └── backup.sh                          # Backup script
└── docs/
    ├── SETUP.md                           # Guia de setup
    └── DEPLOY.md                          # Guia de deploy
```

### Componentes Disponíveis

| Componente | Tecnologia | Status | Descrição |
|-----------|-----------|--------|-----------|
| **Containerização** | Docker | 🔄 Planejado | Imagens container para aplicação |
| **Orquestração Local** | Docker Compose | 🔄 Planejado | Setup local de desenvolvimento |
| **IaC Cloud** | Terraform | 🔄 Planejado | Provisionamento de recursos cloud |
| **Orquestração Avançada** | Kubernetes | 🔲 Futuro | Orquestração em produção |
| **CI/CD** | GitHub Actions/GitLab CI | 🔲 Futuro | Pipelines de teste e deploy |
| **Monitoring** | Prometheus + Grafana | 🔲 Futuro | Monitoramento e alertas |
| **Logging** | ELK Stack | 🔲 Futuro | Centralização de logs |
| **Backup** | Scripts + Cloud Storage | 🔲 Futuro | Backup automático |

### Detalhamento por Componente

#### 🐳 Docker

**Propósito**: Containerizar a aplicação para execução consistente.

```dockerfile
# Exemplo de Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "app/main.py"]
```

**Recursos**:
- Multi-stage builds para otimizar tamanho
- Health checks configurados
- Variáveis de ambiente seguras
- Volumes para dados persistentes

#### 🎼 Docker Compose

**Propósito**: Orquestração de múltiplos containers em ambiente local.

```yaml
# Exemplo de docker-compose.yml
version: '3.9'

services:
  backend:
    build: ./dashboard/backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/metricas
    depends_on:
      - db
  
  frontend:
    build: ./dashboard/frontend
    ports:
      - "3000:3000"
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=metricas
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Configurações**:
- Redes customizadas para comunicação
- Volumes para dados persistentes
- Variáveis de ambiente
- Health checks

#### 🏗️ Terraform

**Propósito**: Provisionar recursos cloud de forma declarativa.

```hcl
# Exemplo de main.tf
provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  
  tags = {
    Name = "app-server"
  }
}

resource "aws_rds_instance" "db" {
  allocated_storage = 20
  engine            = "postgres"
  engine_version    = "15.1"
  instance_class    = "db.t3.micro"
  
  db_name  = "metricas"
  username = var.db_username
  password = var.db_password
}
```

**Recursos Gerenciados**:
- Instâncias de computação (EC2, Compute Engine)
- Bancos de dados (RDS, Cloud SQL)
- Redes e segurança
- Storage (S3, Cloud Storage)
- Load balancers

#### ☸️ Kubernetes

**Propósito**: Orquestração avançada e auto-scaling em produção.

```yaml
# Exemplo de deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: myregistry/backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db-url
```

**Funcionalidades**:
- Auto-scaling horizontal
- Self-healing
- Rolling updates
- Service discovery
- Persistent volumes

#### 🔄 CI/CD

**Propósito**: Automatizar testes e deploy.

```yaml
# Exemplo de .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest tests/

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        run: |
          docker build -t myapp:${{ github.sha }} .
          docker push myapp:${{ github.sha }}
```

**Pipelines**:
- Testes automatizados
- Build de containers
- Deploy automático
- Notificações de status

#### 📊 Monitoring

**Propósito**: Monitorar saúde e performance da aplicação.

```yaml
# Exemplo de prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'backend'
    static_configs:
      - targets: ['localhost:8000']
  
  - job_name: 'database'
    static_configs:
      - targets: ['localhost:5432']
```

**Componentes**:
- Prometheus para coleta de métricas
- Grafana para visualização
- AlertManager para alertas
- Node exporter para sistema

## 🚀 Quick Start

### Usar Docker Compose Localmente

```bash
# Clonar repositório
git clone <repo-url>
cd laboratorio-de-codigo

# Iniciar containers
docker-compose -f infra/docker/docker-compose.yml up -d

# Ver logs
docker-compose logs -f

# Parar containers
docker-compose down
```

### Deploy com Terraform

```bash
# Inicializar Terraform
cd infra/terraform
terraform init

# Visualizar plano
terraform plan

# Aplicar configuração
terraform apply

# Destruir recursos (cuidado!)
terraform destroy
```

## 🔒 Segurança

### Boas Práticas

- 🔐 Usar secrets para senhas e tokens
- 🚫 Nunca commitar credenciais
- 🔑 Usar `.env` para variáveis locais
- 📝 Audit logging ativado
- 🛡️ Network policies configuradas
- ✅ HTTPS obrigatório

### Arquivo .env (Exemplo)

```env
# Database
DB_HOST=db
DB_PORT=5432
DB_NAME=metricas
DB_USER=user
DB_PASSWORD=senha_segura_123

# API
API_KEY=sua_api_key_aqui
SECRET_KEY=sua_secret_key_aqui

# Cloud
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
```

## 📚 Recursos Úteis

- 🐳 **Docker Docs**: [docker.com/docs](https://docs.docker.com/)
- 🏗️ **Terraform Docs**: [terraform.io/docs](https://www.terraform.io/docs)
- ☸️ **Kubernetes Docs**: [kubernetes.io/docs](https://kubernetes.io/docs/)
- 🔄 **GitHub Actions**: [github.com/actions](https://github.com/features/actions)
- 📊 **Prometheus**: [prometheus.io](https://prometheus.io/)
- 🎨 **Grafana**: [grafana.com](https://grafana.com/)

---

**Última atualização**: Junho 2026
