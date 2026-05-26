"""
Análise de Causa Raiz — Case Avaria Zero (Ferrero)
===================================================
Autor: Emanoel Cavalcante
Contexto: Operação CDDNPA – ID Logistics – Ferrero

Case real: Identificação e eliminação de avarias em produtos
Ferrero (chocolate sensível a temperatura e impacto), resultando
em R$0,00 em avarias por 5 meses consecutivos (Jan–Mai 2025).

Ferramentas aplicadas:
 - Diagrama de Ishikawa (Causa e Efeito)
 - 5 Porquês
 - Plano de Ação (5W2H)
 - Monitoramento de resultado
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np

BG      = '#0a0d14'
SURFACE = '#111520'
BORDER  = '#1e2740'
VERDE   = '#00d4a4'
AZUL    = '#4f7fff'
AMARELO = '#fbbf24'
VERMELHO = '#ff6b6b'
ROXO    = '#a78bfa'
TEXTO   = '#e8ecf5'
MUTED   = '#8290aa'

# ──────────────────────────────────────────────
# 1. OS 5 PORQUÊS — Case Avaria Ferrero
# ──────────────────────────────────────────────

cinco_porques = [
    {
        'nivel': 'PROBLEMA',
        'pergunta': 'Qual o problema observado?',
        'resposta': 'Avarias em produtos Ferrero durante manuseio no CDDNPA',
        'cor': VERMELHO,
    },
    {
        'nivel': 'POR QUÊ 1',
        'pergunta': 'Por que ocorreram as avarias?',
        'resposta': 'Produtos empilhados de forma inadequada nas docas de recebimento',
        'cor': '#ff9f43',
    },
    {
        'nivel': 'POR QUÊ 2',
        'pergunta': 'Por que o empilhamento estava inadequado?',
        'resposta': 'Operadores não seguiam procedimento padrão de manuseio Ferrero',
        'cor': AMARELO,
    },
    {
        'nivel': 'POR QUÊ 3',
        'pergunta': 'Por que o procedimento não era seguido?',
        'resposta': 'Treinamento insuficiente e regras não documentadas visivelmente na doca',
        'cor': '#a3e635',
    },
    {
        'nivel': 'POR QUÊ 4',
        'pergunta': 'Por que as regras não estavam documentadas na doca?',
        'resposta': 'Processo de onboarding de operadores não incluía regras específicas por cliente',
        'cor': VERDE,
    },
    {
        'nivel': 'CAUSA RAIZ',
        'pergunta': 'Causa raiz identificada',
        'resposta': 'Ausência de procedimento operacional documentado e visível para manuseio de produtos sensíveis (Ferrero)',
        'cor': AZUL,
    },
]

plano_acao = [
    {
        'what': 'Documentar procedimento de manuseio Ferrero',
        'who': 'Analista Administrativo (Emanoel)',
        'when': 'Semana 1',
        'where': 'Doca CDDNPA + sistema',
        'why': 'Formalizar regras e torná-las auditáveis',
        'how': 'Criar POP com fotos e fluxograma',
        'status': 'Concluído ✓',
        'cor': VERDE,
    },
    {
        'what': 'Treinamento presencial da equipe operacional',
        'who': 'Analista + Supervisor de Operações',
        'when': 'Semana 1–2',
        'where': 'CDDNPA',
        'why': 'Garantir que todos conheçam o procedimento',
        'how': 'Treinamento em doca com checklist de confirmação',
        'status': 'Concluído ✓',
        'cor': VERDE,
    },
    {
        'what': 'Fixar sinalização visual nas docas Ferrero',
        'who': 'Embaixador MyIdea (Emanoel)',
        'when': 'Semana 2',
        'where': 'Docas designadas Ferrero',
        'why': 'Reforço visual contínuo evita reincidência',
        'how': 'Painéis plastificados com regras de empilhamento e temperatura',
        'status': 'Concluído ✓',
        'cor': VERDE,
    },
    {
        'what': 'Controle diário de temperatura via Sitrad',
        'who': 'Analista Administrativo',
        'when': 'Diário – permanente',
        'where': 'Câmara e planilha de controle',
        'why': 'Prevenir avaria por variação de temperatura (chocolate)',
        'how': 'Registro automático + alerta manual se fora do range',
        'status': 'Em curso ✓',
        'cor': AZUL,
    },
    {
        'what': 'Checklist eletrônico de auditoria de doca',
        'who': 'Analista Administrativo',
        'when': 'A cada transferência',
        'where': 'TMWS + planilha controle',
        'why': 'Rastrear conformidade 100% das cargas',
        'how': 'Campo de inspeção integrado à rotina de expedição',
        'status': 'Em curso ✓',
        'cor': AZUL,
    },
]

resultados = {
    'Mês': ['Ago/24', 'Set/24', 'Out/24', 'Nov/24', 'Dez/24', 'Jan/25', 'Fev/25', 'Mar/25', 'Abr/25', 'Mai/25'],
    'Avaria_R': [0.08, 0.05, 0.03, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00],
    'Meta': [0.10] * 10,
    'Fase': ['Antes'] * 5 + ['Após Ação'] * 5,
}

# ──────────────────────────────────────────────
# 2. VISUALIZAÇÕES
# ──────────────────────────────────────────────

fig = plt.figure(figsize=(22, 28), facecolor=BG)

fig.text(0.5, 0.975, 'ANÁLISE DE CAUSA RAIZ — AVARIA ZERO', fontsize=20,
         color=TEXTO, ha='center', fontweight='bold', fontfamily='monospace')
fig.text(0.5, 0.966,
         'Case Ferrero · CDDNPA · 5 Porquês + Plano de Ação 5W2H · Resultado: R$0,00 em 5 meses',
         fontsize=10, color=MUTED, ha='center', fontfamily='monospace')

# ── 2.1  5 Porquês ──
ax1 = fig.add_axes([0.04, 0.72, 0.92, 0.23])
ax1.set_facecolor(SURFACE)
ax1.set_xlim(0, 10); ax1.set_ylim(0, 1)
ax1.axis('off')
ax1.set_title('OS 5 PORQUÊS — METODOLOGIA DE CAUSA RAIZ', color=TEXTO,
              fontsize=11, fontfamily='monospace', pad=10, loc='left')

n = len(cinco_porques)
for i, item in enumerate(cinco_porques):
    x = i * (10 / n) + 0.3
    w, h = 1.3, 0.65
    rect = mpatches.FancyBboxPatch((x, 0.18), w, h, boxstyle='round,pad=0.02',
                                    facecolor=item['cor'] + '22',
                                    edgecolor=item['cor'], linewidth=1.5)
    ax1.add_patch(rect)
    ax1.text(x + w/2, 0.78, item['nivel'], ha='center', va='center',
             color=item['cor'], fontsize=8, fontweight='bold', fontfamily='monospace')
    ax1.text(x + w/2, 0.58, item['pergunta'], ha='center', va='center',
             color=MUTED, fontsize=6.5, fontfamily='monospace',
             wrap=True)
    ax1.text(x + w/2, 0.36, item['resposta'], ha='center', va='center',
             color=TEXTO, fontsize=6.8, fontfamily='monospace',
             wrap=True)
    if i < n - 1:
        ax1.annotate('', xy=(x + w + 0.05, 0.5), xytext=(x + w - 0.02, 0.5),
                     arrowprops=dict(arrowstyle='->', color=MUTED, lw=1.5))

# ── 2.2  Resultado: evolução das avarias ──
ax2 = fig.add_axes([0.04, 0.50, 0.55, 0.18])
ax2.set_facecolor(SURFACE)
meses_r = resultados['Mês']
avarias = resultados['Avaria_R']
meta = resultados['Meta']
cores = [VERMELHO if f == 'Antes' else VERDE for f in resultados['Fase']]
bars = ax2.bar(meses_r, avarias, color=cores, width=0.6, zorder=3)
ax2.plot(meses_r, meta, color=AMARELO, linewidth=1.5, linestyle='--',
         label='Meta ≤ R$0,10/ton', zorder=4)
ax2.axvline(x=4.5, color=AZUL, linewidth=1.5, linestyle=':', alpha=0.7)
ax2.text(4.6, 0.09, 'Plano de\nação ativado', color=AZUL,
         fontsize=8, fontfamily='monospace', va='top')
ax2.set_facecolor(SURFACE)
ax2.tick_params(colors=MUTED, labelsize=8, rotation=30)
ax2.spines[:].set_color(BORDER)
ax2.set_title('EVOLUÇÃO DAS AVARIAS — ANTES E APÓS AÇÃO (R$/ton)',
              color=TEXTO, fontsize=10, fontfamily='monospace', pad=8)
ax2.legend(fontsize=8, facecolor=SURFACE, edgecolor=BORDER, labelcolor=MUTED)
p1 = mpatches.Patch(color=VERMELHO, label='Antes da ação')
p2 = mpatches.Patch(color=VERDE, label='Após ação (R$0,00)')
ax2.legend(handles=[p1, p2], fontsize=8, facecolor=SURFACE, edgecolor=BORDER, labelcolor=MUTED)

# ── 2.3  Ishikawa simplificado ──
ax3 = fig.add_axes([0.62, 0.50, 0.36, 0.18])
ax3.set_facecolor(SURFACE)
ax3.set_xlim(0, 10); ax3.set_ylim(0, 6)
ax3.axis('off')
ax3.set_title('DIAGRAMA DE ISHIKAWA (RESUMO)', color=TEXTO,
              fontsize=10, fontfamily='monospace', pad=8)

ax3.annotate('', xy=(9.2, 3), xytext=(1, 3),
             arrowprops=dict(arrowstyle='->', color=MUTED, lw=2))
efeito_box = mpatches.FancyBboxPatch((8.8, 2.3), 1.1, 1.4,
    boxstyle='round,pad=0.05', facecolor=VERMELHO+'33', edgecolor=VERMELHO, lw=1.5)
ax3.add_patch(efeito_box)
ax3.text(9.35, 3, 'AVARIA\nFerrero', ha='center', va='center',
         color=VERMELHO, fontsize=7.5, fontweight='bold', fontfamily='monospace')

causas = [
    (2.5, 5.2, 'Método:\nEmpilhamento\ninadequado', 2.5, 4.2),
    (2.5, 0.8, 'Mão de Obra:\nSem treinamento\nespecífico', 2.5, 1.8),
    (5.0, 5.2, 'Material:\nEmbalagem\nsensível', 5.0, 4.2),
    (5.0, 0.8, 'Ambiente:\nVariação de\ntemperatura', 5.0, 1.8),
    (7.2, 5.0, 'Medição:\nSem checklist\nde conformidade', 7.0, 4.2),
    (7.2, 1.0, 'Gestão:\nPOP não\ndocumentado', 7.0, 1.8),
]
cors_ish = [AZUL, AMARELO, ROXO, VERDE, '#ff9f43', VERMELHO]
for i, (xt, yt, txt, x2, y2) in enumerate(causas):
    ax3.text(xt, yt, txt, ha='center', va='center',
             color=cors_ish[i], fontsize=6.5, fontfamily='monospace')
    ax3.plot([x2, (x2+8.8)/2], [y2, 3], color=MUTED, lw=0.8, alpha=0.5)

# ── 2.4  Plano de Ação 5W2H ──
ax4 = fig.add_axes([0.04, 0.07, 0.92, 0.40])
ax4.set_facecolor(SURFACE)
ax4.axis('off')
ax4.set_title('PLANO DE AÇÃO — 5W2H · CASE AVARIA ZERO FERRERO',
              color=TEXTO, fontsize=11, fontfamily='monospace', pad=10, loc='left')

colunas = ['O QUÊ (What)', 'QUEM (Who)', 'QUANDO (When)', 'ONDE (Where)', 'POR QUÊ (Why)', 'COMO (How)', 'STATUS']
col_x = [0.01, 0.22, 0.34, 0.44, 0.57, 0.73, 0.90]
col_w = [0.20, 0.11, 0.09, 0.12, 0.15, 0.16, 0.09]

for j, col in enumerate(colunas):
    ax4.text(col_x[j], 0.93, col, transform=ax4.transAxes,
             fontsize=7.5, color=MUTED, fontweight='bold', fontfamily='monospace')

for i, acao in enumerate(plano_acao):
    y = 0.78 - i * 0.17
    rect = mpatches.FancyBboxPatch((0.005, y - 0.06), 0.99, 0.14,
        transform=ax4.transAxes, boxstyle='round,pad=0.005',
        facecolor=acao['cor'] + '10', edgecolor=acao['cor'] + '40', lw=0.8)
    ax4.add_patch(rect)
    vals = [acao['what'], acao['who'], acao['when'], acao['where'],
            acao['why'], acao['how'], acao['status']]
    for j, val in enumerate(vals):
        cor = acao['cor'] if j == 6 else TEXTO
        ax4.text(col_x[j] + 0.005, y, val, transform=ax4.transAxes,
                 fontsize=7, color=cor, va='center', fontfamily='monospace',
                 wrap=True)

fig.text(0.5, 0.022,
         'Fonte: Dados reais operação CDDNPA  |  Autor: Emanoel Cavalcante  |  github.com/EmanoelInC',
         ha='center', color=MUTED, fontsize=8, fontfamily='monospace')

plt.savefig('causa_raiz_avaria_zero.png', dpi=150, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
print("✅ Gráfico salvo: causa_raiz_avaria_zero.png")
plt.show()
