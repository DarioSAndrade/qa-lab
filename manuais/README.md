# Manual Completo: Como Realizar Testes de Carga em um Website

Este manual foi criado para orientar equipes de desenvolvimento, infraestrutura e QA na execução de testes de carga em websites. Abaixo serão abordados os principais tipos de testes, suas finalidades, ferramentas recomendadas (gratuitas sempre que possível) e tutoriais passo a passo para execução.

---

## ✅ **1. O que é Teste de Carga?**

Teste de carga é um tipo de teste de desempenho utilizado para verificar como um sistema se comporta sob uma determinada carga de usuários simultâneos, acessos ou requisições. Ele simula o comportamento real do usuário para identificar gargalos e limites da aplicação web.

---

## 🔢 **2. Tipos de Teste de Carga e Suas Finalidades**

| Tipo de Teste        | Finalidade |
|----------------------|------------|
| **Teste de Carga Padrão** | Avalia o comportamento com usuários simultâneos esperados |
| **Teste de Estresse** | Determina o limite máximo suportado pelo sistema |
| **Teste de Pico (Spike)** | Avalia como o sistema reage a aumentos rápidos de carga |
| **Teste de Soak (Endurance)** | Verifica estabilidade sob carga moderada por longos períodos |
| **Teste de Volume (Data Volume)** | Avalia desempenho com grande volume de dados |

---

## 🔧 **3. Ferramentas Gratuitas Recomendadas**

| Ferramenta | Tipo de Teste Suportado | Website |
|------------|--------------------------|---------|
| **Apache JMeter** | Todos | https://jmeter.apache.org |
| **k6 (Grafana Labs)** | Todos | https://k6.io |
| **Locust** | Carga, Estresse, Soak | https://locust.io |
| **Loader.io** | Carga, Pico | https://loader.io |
| **BlazeMeter** | Carga (com JMeter) | https://www.blazemeter.com |

---

## ✍️ **4. Como Executar Cada Tipo de Teste**

### **4.1 Teste de Carga Padrão com Apache JMeter**

**Passo a Passo:**
1. Instale o JMeter (https://jmeter.apache.org/download_jmeter.cgi)
2. Abra o JMeter GUI
3. Crie um novo "Thread Group" e defina número de usuários, tempo de ramp-up e loops
4. Adicione um "HTTP Request" apontando para `https://seuwebsite.com`
5. Adicione "View Results Tree" para visualizar as respostas
6. Execute e analise os tempos de resposta

### **4.2 Teste de Estresse com k6 (CLI)**

**Passo a Passo:**
1. Instale via `brew install k6` (macOS/Linux)
2. Crie um script `stress-test.js`:
```javascript
import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 20 },
    { duration: '2m', target: 100 },
    { duration: '2m', target: 500 },
    { duration: '1m', target: 0 },
  ],
};

export default function () {
  http.get('https://seuwebsite.com');
  sleep(1);
}
```
3. Execute: `k6 run stress-test.js`
4. Verifique resultados no terminal

### **4.3 Teste de Pico com Loader.io**

**Passo a Passo:**
1. Crie conta em https://loader.io
2. Verifique domínio via token (arquivo no servidor)
3. Configure teste com aumento rápido de usuários
4. Execute e acompanhe o gráfico

### **4.4 Teste de Soak com Locust**

**Passo a Passo:**
1. Instale com `pip install locust`
2. Crie `locustfile.py`:
```python
from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")
```
3. Execute com: `locust -f locustfile.py --host=https://seuwebsite.com`
4. Acesse `http://localhost:8089` para iniciar e visualizar

### **4.5 Teste de Volume de Dados com JMeter**

1. Siga passos do 4.1
2. Use "CSV Data Set Config" para simular formulários e pesquisas com dados variados
3. Analise impacto nas respostas

---

## 🎓 **5. Boas Práticas ao Realizar Testes de Carga**

- Sempre testar em ambiente de homologacão ou clonado da produção
- Monitorar recursos do servidor (CPU, RAM, I/O)
- Acompanhar logs de erro
- Limitar acessos simultâneos no início e aumentar gradualmente
- Ter metas definidas: tempo máximo de resposta, número esperado de usuários etc.
- Documentar tudo (cenário, ferramentas, métricas)

---

## ⚙️ **6. Referências e Links úteis**

- [Documentação oficial do Apache JMeter](https://jmeter.apache.org/usermanual/index.html)
- [Guia de Performance com k6](https://k6.io/docs/)
- [Locust Quickstart](https://docs.locust.io/en/stable/quickstart.html)
- [Loader.io Guide](https://support.loader.io/docs)

---

## 📄 **7. Checklist Final**

- [ ] Testes definidos (tipo, cenário)
- [ ] Ambiente preparado
- [ ] Ferramentas instaladas
- [ ] Scripts validados
- [ ] Monitoramento ativo
- [ ] Análise de resultados após execução

---

**Autor:** Dario Andrade

**Propósito:** Garantir que o website esteja preparado para acessos em larga escala com segurança, estabilidade e desempenho.


