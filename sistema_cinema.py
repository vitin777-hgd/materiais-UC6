from datetime import date
import locale

# 1. Configura o idioma para pegar o dia em português (ajustado para aceitar qualquer sistema)
try:
    locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except:
        pass

# 2. Pega o dia atual do sistema (em minúsculo)
dia = date.today().strftime('%A').lower()

# 3. Define o preço do ingresso baseado no dia
if dia in ["segunda-feira", "quarta-feira", "sexta-feira"]:
    valor_ingresso = 32.50
else:
    valor_ingresso = 36.00

# --- ENTRADA DE DADOS ---
print(f"--- CINE SENAC (Hoje é {dia}) ---")

# Escolha do Filme
print("[D039] O Poderoso Chefão\n[B678] Matrix\n[D889] O Senhor dos Anéis\n[M912] Interestelar\n[G007] O Resgate do Soldado Ryan")
filme_codigo = input("Digite o código do filme: ").upper()
qtd_ingressos = int(input("Quantos ingressos deseja? "))

# Escolha do Combo
print("\n--- COMBOS DISPONÍVEIS ---")
print("[COMBO-005] Doritos + Refri Lata (R$ 15,90)")
print("[COMBO-072] Pipoca Salgada + Coca (R$ 17,90)")
print("[COMBO-777] Pipoca Doce + Suco (R$ 14,90)")
print("[COMBO-215] Refil Pipoca + 2 Refris (R$ 25,90)")
print("[0] Não quero combo")

combo_codigo = input("Digite o código do combo: ").upper()

# --- CÁLCULOS ---
total_ingressos = valor_ingresso * qtd_ingressos

valor_combo = 0.0
if combo_codigo == "COMBO-005": valor_combo = 15.90
elif combo_codigo == "COMBO-072": valor_combo = 17.90
elif combo_codigo == "COMBO-777": valor_combo = 14.90
elif combo_codigo == "COMBO-215": valor_combo = 25.90

total_geral = total_ingressos + valor_combo

# --- EXTRATO FINAL ---
print("\n" + "="*40)
print("           RESUMO DO PEDIDO           ")
print("="*40)
print(f" Filme Código:   {filme_codigo}")
print(f" Ingressos:      {qtd_ingressos}x de R$ {valor_ingresso:.2f}")
print(f" Total Combos:   R$ {valor_combo:.2f}")
print("-"*40)
print(f" TOTAL A PAGAR:  R$ {total_geral:.2f}")
print("=" * 40)