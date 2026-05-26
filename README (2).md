# 🔍 Análise de Causa Raiz — Avaria Zero (Case Ferrero)

> Aplicação real de 5 Porquês + Ishikawa + Plano de Ação 5W2H que resultou em **R$0,00 em avarias por 5 meses consecutivos** na operação Ferrero (CDDNPA – ID Logistics).

---

## 🎯 Contexto do case

Produtos Ferrero (chocolates) são **altamente sensíveis** a temperatura e impacto. Uma avaria gera não apenas prejuízo financeiro, mas também risco de perda do contrato — a tolerância era **≤ R$0,10/ton movimentada**.

Ao identificar ocorrências recorrentes de avaria no manuseio, apliquei metodologia estruturada de causa raiz para encontrar e eliminar a causa de origem — não apenas tratar o sintoma.

**Resultado:** R$0,00 em avarias de Janeiro a Maio/2025.

---

## 🔧 Metodologias aplicadas

### Os 5 Porquês

| Nível | Pergunta | Resposta |
|---|---|---|
| Problema | O que foi observado? | Avarias em produtos Ferrero durante manuseio no CDDNPA |
| Por quê 1 | Por que ocorreram? | Produtos empilhados de forma inadequada nas docas |
| Por quê 2 | Por que empilhamento inadequado? | Operadores não seguiam procedimento padrão Ferrero |
| Por quê 3 | Por que não seguiam? | Treinamento insuficiente, regras não visíveis na doca |
| Por quê 4 | Por que não estavam visíveis? | Onboarding não incluía regras específicas por cliente |
| **Causa Raiz** | — | **Ausência de POP documentado e visível para manuseio de produtos sensíveis** |

### Diagrama de Ishikawa

6 categorias de causas mapeadas: Método, Mão de Obra, Material, Ambiente, Medição e Gestão.

---

## 📋 Plano de Ação (5W2H)

| Ação | Responsável | Prazo | Status |
|---|---|---|---|
| Documentar POP de manuseio Ferrero | Analista Administrativo | Semana 1 | ✅ Concluído |
| Treinamento presencial da equipe | Analista + Supervisor | Sem. 1–2 | ✅ Concluído |
| Sinalização visual nas docas | Embaixador MyIdea | Semana 2 | ✅ Concluído |
| Controle diário de temperatura (Sitrad) | Analista Administrativo | Permanente | ✅ Em curso |
| Checklist eletrônico de auditoria de doca | Analista Administrativo | Por transferência | ✅ Em curso |

---

## 📈 Resultado

| Mês | Avaria R$/ton | vs. Meta |
|---|---|---|
| Jan/25 | R$0,00 | ✅ Abaixo do limite |
| Fev/25 | R$0,00 | ✅ |
| Mar/25 | R$0,00 | ✅ |
| Abr/25 | R$0,00 | ✅ |
| Mai/25 | R$0,00 | ✅ |

---

## 💡 Transferibilidade para TI

A lógica aplicada aqui é **idêntica à Gestão de Problemas (ITIL)**:

- Identificar incidente recorrente → mapeamento de causa raiz → tratamento definitivo → monitoramento de reincidência
- A diferença é que aqui eram caixas de chocolate. Em TI, são tickets de suporte ou falhas de disponibilidade.

---

## 🚀 Como executar

```bash
git clone https://github.com/EmanoelInC/analise-causa-raiz-avaria-zero.git
cd analise-causa-raiz-avaria-zero
pip install matplotlib numpy
python causa_raiz_avaria_zero.py
```

---

*Autor: Emanoel Cavalcante · [emanoelinc.github.io](https://emanoelinc.github.io)*
