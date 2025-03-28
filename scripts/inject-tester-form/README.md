# 🛡️ inject-tester-form

**inject-tester-form** é um script de segurança desenvolvido para testar formulários de contato em aplicações web contra ataques de injeção, como **SQL Injection**, **Cross-Site Scripting (XSS)** e outras formas de entradas maliciosas.

Este projeto tem como foco ajudar desenvolvedores e equipes de QA a validarem a robustez dos seus formulários, garantindo que dados submetidos sejam corretamente tratados e sanitizados, prevenindo assim vulnerabilidades comuns em aplicações web.

> ⚠️ Esta ferramenta é destinada apenas para ambientes de testes e auditoria autorizada. Nunca utilize em sistemas sem permissão explícita.

# Teste de Injeção em Formulário de Contato

Este script em Python permite testar a segurança de formulários de contato contra injeções de código, como SQL Injection, XSS (Cross-site scripting), HTML e JavaScript Injection.

## Objetivo

Identificar possíveis falhas de segurança em formulários públicos que possam comprometer a aplicação, expondo dados ou permitindo execução de código malicioso.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `requests`

## Payloads Testados

- `' OR '1'='1` — SQL Injection
- `<script>alert('XSS')</script>` — XSS
- `<h1>Test</h1>` — HTML Injection
- `<a href='javascript:alert(1)'>Click</a>` — JavaScript Injection
- `' UNION SELECT NULL--` — SQL Injection avançado

## Como Usar

1. Instale as dependências:
    ```bash
    pip install requests
    ```

2. Edite o script e ajuste a URL do formulário (`form_url`) e os nomes dos campos.

3. Execute:
    ```bash
    python test_form_injection.py
    ```

## Observações

- **Use apenas com autorização do cliente.**
- Este teste simula ataques de forma ética com objetivo de prevenir vulnerabilidades reais.

## Autor

Desenvolvido por Dario S. Andrade
