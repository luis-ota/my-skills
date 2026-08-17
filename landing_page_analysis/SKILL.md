---
name: landing-page-analysis
description: "Skill for analyzing landing pages focusing on conversion factors before design. Helps evaluate if a page has conditions to sell before investing in visual design."
---

# Landing Page Analysis

Use this skill whenever you need to evaluate a landing page for conversion potential before making any design changes. It forces you to check the fundamentals first — traffic source, ICP alignment, value proposition clarity, objection handling, and friction — instead of blindly redesigning a page that was never going to convert.

## When to use

- A founder or PM says "the page looks ugly, redesign it" — use this skill to prove the problem is not visual.
- You're auditing a landing page and need a structured checklist.
- You're about to start a redesign and want to validate the strategy first.
- You're creating a new LP from scratch and want to get the structure right before touching design.

## The Checklist

### 1. Traffic & Source

- **De onde esse usuário veio?** (ad, organic, email, referral?)
- **O que ele esperava encontrar quando clicou?** (does the page deliver?)
- **A promessa do anúncio bate com o conteúdo da página?** (message match)

### 2. ICP & Targeting

- **Qual o ICP (Ideal Customer Profile)?** (who is this for?)
- **Qual dor/desejo/objetivo trouxe essa pessoa aqui?** (pain, desire, goal)

### 3. Value Proposition

- **O que exatamente tá sendo vendido?** (product, service, outcome?)
- **Dá pra entender isso em menos de 5s?** (above the fold clarity)
- **A copy conversa com o ICP?** (tone, language, specificity)
- **As principais objeções são abordadas?** (price, trust, risk, timing)

### 4. User Experience

- **A página consegue segurar a atenção?** (scroll depth, engagement)
- **Existe fricção desnecessária para comprar/assinar?** (CTAs, forms, steps)

## Design Comes Second

A LP pode estar linda, consistente, bem espaçada, com uma puta direção de arte e mesmo assim ser uma máquina de jogar dinheiro fora.

Se o usuário não entende o que você vende, não percebe valor, não confia ou não sabe por que deveria comprar agora — não é seu pixel perfect que vai salvar.

Esse é um erro comum em SaaS: tentam melhorar a conversão redesenhando a página com um videozinho na hero sem antes entender por que ela não está convertendo.

## Output

The skill returns a structured analysis with:

- **Status:** `ready-for-design` | `needs-fix` | `rebuild-needed`
- **Priority issues** identified per checklist section
- **Recommendations** for copy, structure, or design

## Decision tree

```
User wants to redesign / improve LP
    |
    +-- Has the checklist been run?
    |       +-- No  -> Run the checklist first
    |       +-- Yes -> Proceed to design review
    |
    +-- Any critical issues?
    |       +-- Yes -> Fix copy/structure before design
    |       +-- No  -> Design review is safe to proceed
    |
    +-- Status: ready-for-design | needs-fix | rebuild-needed
```

## Best practices

- Always run the checklist before touching any design tool.
- If the page fails 3+ checklist items, redesign is a waste — fix fundamentals first.
- Use the checklist as a shared framework with founders, PMs, and designers.
- Re-run the checklist after changes to verify improvement.

## Reference files

- `README.md` - Skill overview and setup instructions.