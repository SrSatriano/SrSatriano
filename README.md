<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050816,35:0f172a,70:134e4a,100:0891b2&height=190&section=header&text=Matheus%20Rodrigues%20Satriano&fontSize=38&fontColor=ffffff&animation=twinkling" width="100%" alt="Matheus Rodrigues Satriano" />

<div align="center">

<h3>Back-end, sistemas quant, IA local e infraestrutura soberana</h3>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=18&pause=1200&color=38BDF8&center=true&width=780&lines=LHN+Sovereign+V90+%C2%B7+terminal+quant+local;C%2B%2B+%C2%B7+Rust+%C2%B7+Python+%C2%B7+TypeScript;Low+latency+%C2%B7+RAG+offline+%C2%B7+Fiscal+BR+%C2%B7+Web3" alt="LHN Sovereign V90, C++, Rust, Python, TypeScript, low latency, RAG offline, Fiscal BR, Web3" />

<br/>

<a href="https://srsatriano.github.io/portfolio-matheus-satriano/">
  <img src="https://img.shields.io/badge/Portf%C3%B3lio-online-0891b2?style=for-the-badge" alt="Portfólio online" />
</a>
<a href="https://github.com/SrSatriano?tab=repositories">
  <img src="https://img.shields.io/badge/Reposit%C3%B3rios-GitHub-181717?style=for-the-badge&logo=github" alt="Repositórios no GitHub" />
</a>
<a href="https://www.linkedin.com/in/matheus-rodrigues-satriano">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="mailto:matheussatriano@hotmail.com">
  <img src="https://img.shields.io/badge/E--mail-contato-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Perfil-p%C3%BAblico-0ea5e9?style=flat-square" alt="Perfil público" />
<img src="https://img.shields.io/badge/37%20repos-GitHub-22c55e?style=flat-square" alt="37 repositórios GitHub" />
<img src="https://img.shields.io/badge/30%20m%C3%B3dulos-OSS-1d4ed8?style=flat-square" alt="30 módulos open source" />
<img src="https://img.shields.io/badge/docs-pt--BR-64748b?style=flat-square" alt="Documentação em português brasileiro" />
<img src="https://img.shields.io/badge/foco-local--first-f59e0b?style=flat-square" alt="Foco local-first" />

</div>

---

## Navegação rápida

| | Seção |
|:---:|---|
| 01 | [Quem sou](#quem-sou) |
| 02 | [Tese de engenharia](#tese-de-engenharia) |
| 03 | [LHN Sovereign V90](#lhn-sovereign-v90) |
| 04 | [Projetos principais](#projetos-principais) |
| 05 | [Stack](#stack) |
| 06 | [Mapa dos repositórios](#mapa-dos-repositórios) |
| 07 | [Atividade e contato](#atividade-e-contato) |

---

<a id="quem-sou"></a>

## Quem sou

Sou **Matheus Rodrigues Satriano**, graduando em **Ciência da Computação** e desenvolvedor focado em sistemas que exigem **controle, desempenho e clareza operacional**.

Meu centro de gravidade é back-end, mas eu gosto de atravessar a stack quando isso melhora o produto: APIs, painéis, motores de execução, infraestrutura local, automação, telemetria e modelos de IA rodando perto dos dados.

O que aparece com frequência nos meus projetos:

| Direção | Como isso vira código |
|---|---|
| **Baixa latência** | C++, Rust, SIMD, estruturas de dados, benchmarks e simulações de mercado |
| **IA local** | RAG offline, Ollama, pipelines self-hosted, avaliação de respostas e automação de mídia |
| **Mercado financeiro** | order book, pricing, risco, liquidez, tax-loss harvesting e dashboards operacionais |
| **Infra soberana** | Docker, Ansible, eBPF, GitOps, logs comprimidos e serviços que rodam fora da dependência de nuvem |
| **Produto real** | README forte, arquitetura documentada, testes, rotas claras e fluxo de uso reproduzível |

**Princípio pessoal:** se o problema não precisa sair da máquina, ele deve conseguir rodar local. A nuvem entra por necessidade técnica, não por reflexo.

---

<a id="tese-de-engenharia"></a>

## Tese de engenharia

Eu construo como quem quer operar o sistema depois. Por isso meus repositórios costumam combinar:

| Camada | Preferência técnica |
|---|---|
| **Core** | código mensurável, explícito e testável |
| **API** | contratos simples, FastAPI, OpenAPI, validação com Pydantic |
| **Interface** | Next.js, TUI em Rust ou dashboards objetivos para tomada de decisão |
| **Dados** | SQLite/PostgreSQL quando basta, Redis quando latência pede, arquivos locais quando são a solução mais honesta |
| **IA** | modelos open source, RAG offline, avaliação e isolamento do fluxo sensível |
| **Operação** | logs úteis, health checks, scripts reproduzíveis e documentação em português brasileiro |

Essa combinação aparece no meu projeto principal, o **LHN Sovereign V90**, e nos módulos independentes que orbitam o mesmo universo técnico.

---

<a id="lhn-sovereign-v90"></a>

## LHN Sovereign V90

<table>
<tr>
<td width="55%" valign="top">

<p><strong>LHN Sovereign V90</strong> é meu terminal quantitativo local para pesquisa, automação controlada e operação assistida em cripto.</p>

<p>Ele combina <strong>FastAPI</strong>, <strong>Next.js</strong>, integração com <strong>Bybit V5</strong>, camadas de risco, workspace local e módulos de IA. A ideia central é simples: manter o operador no controle, reduzir dependências externas e deixar o sistema observável.</p>

<ul>
  <li><strong>Painel:</strong> interface web para leitura de estado, parâmetros e operação.</li>
  <li><strong>API:</strong> orquestração, configuração, risco, execução e integração externa.</li>
  <li><strong>Core:</strong> tomada de decisão, replay, backfill, radar, labeler e ciclo de treino.</li>
  <li><strong>IA local:</strong> inferência e análise próxima dos dados.</li>
  <li><strong>Workspace:</strong> persistência, auditoria, logs e artefatos operacionais.</li>
</ul>

<p><strong>Licença:</strong> PolyForm Noncommercial. O projeto é público, mas não é licenciado como MIT.</p>

</td>
<td width="45%" valign="top" align="center">

<a href="https://github.com/SrSatriano/LHN-V90-IA">
  <img src="https://gh-card.dev/repos/SrSatriano/LHN-V90-IA.svg?fullname=&lang=Python" alt="LHN-V90-IA" width="100%" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/FastAPI-9002-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI 9002" />
<img src="https://img.shields.io/badge/Next.js-9090-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js 9090" />
<img src="https://img.shields.io/badge/Bybit-V5-f7a600?style=flat-square" alt="Bybit V5" />
<img src="https://img.shields.io/badge/IA-local-22c55e?style=flat-square" alt="IA local" />

</td>
</tr>
</table>

```mermaid
flowchart LR
    UI["Next.js dashboard :9090"] --> API["FastAPI core :9002"]
    API --> EX["Bybit V5"]
    API --> RISK["Risk engine"]
    API --> AI["IA local"]
    API --> WS["Workspace local"]
    WS --> OBS["Logs, replay e auditoria"]
```

---

<a id="projetos-principais"></a>

## Projetos principais

<div align="center">

<a href="https://github.com/SrSatriano/ultra-low-latency-order-book-engine">
  <img src="https://gh-card.dev/repos/SrSatriano/ultra-low-latency-order-book-engine.svg?lang=C%2B%2B" alt="Ultra-low latency order book engine" width="32%" />
</a>
<a href="https://github.com/SrSatriano/avx512-options-pricing-engine">
  <img src="https://gh-card.dev/repos/SrSatriano/avx512-options-pricing-engine.svg?lang=C%2B%2B" alt="AVX-512 options pricing engine" width="32%" />
</a>
<a href="https://github.com/SrSatriano/local-rag-second-mind-vault">
  <img src="https://gh-card.dev/repos/SrSatriano/local-rag-second-mind-vault.svg?lang=Python" alt="Local RAG Second Mind Vault" width="32%" />
</a>

<br/>

<a href="https://github.com/SrSatriano/multi-channel-analytics-dashboard">
  <img src="https://gh-card.dev/repos/SrSatriano/multi-channel-analytics-dashboard.svg?lang=TypeScript" alt="Multi-channel analytics dashboard" width="32%" />
</a>
<a href="https://github.com/SrSatriano/unified-trading-super-terminal">
  <img src="https://gh-card.dev/repos/SrSatriano/unified-trading-super-terminal.svg?lang=Rust" alt="Unified trading super terminal" width="32%" />
</a>
<a href="https://github.com/SrSatriano/high-compression-log-router">
  <img src="https://gh-card.dev/repos/SrSatriano/high-compression-log-router.svg?lang=Rust" alt="High compression log router" width="32%" />
</a>

</div>

| Projeto | Por que ele existe | Stack dominante |
|---|---|---|
| [ultra-low-latency-order-book-engine](https://github.com/SrSatriano/ultra-low-latency-order-book-engine) | motor de order book e matching para estudar microestrutura, filas, execução e performance | C++, CMake, testes, benchmark |
| [avx512-options-pricing-engine](https://github.com/SrSatriano/avx512-options-pricing-engine) | pricing de opções com comparação entre caminho escalar e vetorização SIMD | C++, AVX-512, Monte Carlo, Black-Scholes |
| [local-rag-second-mind-vault](https://github.com/SrSatriano/local-rag-second-mind-vault) | cofre de conhecimento privado com perguntas e respostas 100% offline | Python, FastAPI, Ollama, embeddings |
| [multi-channel-analytics-dashboard](https://github.com/SrSatriano/multi-channel-analytics-dashboard) | painel para métricas, retenção, conversão e leitura executiva de canais | Next.js, TypeScript, Recharts |
| [unified-trading-super-terminal](https://github.com/SrSatriano/unified-trading-super-terminal) | terminal TUI para monitoramento de risco, posições e sinais | Rust, Ratatui |
| [high-compression-log-router](https://github.com/SrSatriano/high-compression-log-router) | ingestão e roteamento de logs com compressão eficiente | Rust, Zstd, LZ4 |
| [fiscal-data-ocr-engine](https://github.com/SrSatriano/fiscal-data-ocr-engine) | OCR e extração estruturada para documentos fiscais brasileiros | Python, OCR, validação |
| [tax-loss-harvesting-engine](https://github.com/SrSatriano/tax-loss-harvesting-engine) | simulação e regras fiscais para compensação de perdas | Node.js, TypeScript, regras BR |

---

<a id="stack"></a>

## Stack

### Linguagens e core

<p>
  <img src="https://skillicons.dev/icons?i=python,rust,cpp,typescript,go,java,javascript,solidity,bash&perline=9" alt="Python, Rust, C++, TypeScript, Go, Java, JavaScript, Solidity e Bash" />
</p>

<p>
  <img src="https://img.shields.io/badge/MQL5-0ea5e9?style=flat-square" alt="MQL5" />
  <img src="https://img.shields.io/badge/SIMD-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="SIMD" />
  <img src="https://img.shields.io/badge/AVX--512-512BD4?style=flat-square&logo=intel&logoColor=white" alt="AVX-512" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA" />
</p>

### Web, APIs e produto

<p>
  <img src="https://skillicons.dev/icons?i=fastapi,nextjs,react,tailwind,nodejs,postgres,redis&perline=8" alt="FastAPI, Next.js, React, Tailwind, Node.js, PostgreSQL e Redis" />
</p>

<p>
  <img src="https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white" alt="OpenAPI" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic" />
  <img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square" alt="WebSocket" />
  <img src="https://img.shields.io/badge/Recharts-22c55e?style=flat-square" alt="Recharts" />
  <img src="https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white" alt="Framer Motion" />
</p>

### IA, dados e automação

<p>
  <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square" alt="Ollama" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square" alt="LangChain" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white" alt="Keras" />
  <img src="https://img.shields.io/badge/RAG-offline-22c55e?style=flat-square" alt="RAG offline" />
  <img src="https://img.shields.io/badge/OCR-fiscal_BR-f59e0b?style=flat-square" alt="OCR fiscal brasileiro" />
</p>

### Infra, DevOps e sistemas

<p>
  <img src="https://skillicons.dev/icons?i=docker,ansible,linux,git,github,nginx,kubernetes&perline=8" alt="Docker, Ansible, Linux, Git, GitHub, Nginx e Kubernetes" />
</p>

<p>
  <img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose" />
  <img src="https://img.shields.io/badge/GitOps-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="GitOps" />
  <img src="https://img.shields.io/badge/eBPF-000000?style=flat-square" alt="eBPF" />
  <img src="https://img.shields.io/badge/Zstd-5A5A5A?style=flat-square" alt="Zstd" />
  <img src="https://img.shields.io/badge/libp2p-000000?style=flat-square" alt="libp2p" />
  <img src="https://img.shields.io/badge/Hyperledger_Fabric-2F2F72?style=flat-square" alt="Hyperledger Fabric" />
</p>

### Mercado e Web3

<p>
  <img src="https://img.shields.io/badge/Bybit_V5-F7A600?style=flat-square" alt="Bybit V5" />
  <img src="https://img.shields.io/badge/MetaTrader_5-0B6BB4?style=flat-square" alt="MetaTrader 5" />
  <img src="https://img.shields.io/badge/Order_Book-0f172a?style=flat-square" alt="Order book" />
  <img src="https://img.shields.io/badge/Risk_Engine-b91c1c?style=flat-square" alt="Risk engine" />
  <img src="https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white" alt="Solidity" />
  <img src="https://img.shields.io/badge/Hardhat-FFF100?style=flat-square" alt="Hardhat" />
  <img src="https://img.shields.io/badge/Foundry-000000?style=flat-square" alt="Foundry" />
  <img src="https://img.shields.io/badge/MEV-educacional-64748b?style=flat-square" alt="MEV educacional" />
</p>

---

<a id="mapa-dos-repositórios"></a>

## Mapa dos repositórios

<div align="center">
  <img src="assets/repos-breakdown-profile.svg" alt="Distribuição dos repositórios por categoria" width="96%" />
</div>

<details open>
<summary><b>Trading, quant e mercado</b></summary>

| Repo | Foco |
|---|---|
| [LHN-V90-IA](https://github.com/SrSatriano/LHN-V90-IA) | terminal quant principal com IA local, risco e integração Bybit |
| [ultra-low-latency-order-book-engine](https://github.com/SrSatriano/ultra-low-latency-order-book-engine) | matching engine em C++ para order book e simulação de execução |
| [smc-liquidity-scanner](https://github.com/SrSatriano/smc-liquidity-scanner) | scanner de liquidez, FVG, BOS/CHOCH e conceitos SMC |
| [unified-trading-super-terminal](https://github.com/SrSatriano/unified-trading-super-terminal) | TUI em Rust para acompanhar risco, sinais e posições |
| [avx512-options-pricing-engine](https://github.com/SrSatriano/avx512-options-pricing-engine) | precificação de opções otimizada com SIMD |
| [mempool-arbitrage-mev-bot](https://github.com/SrSatriano/mempool-arbitrage-mev-bot) | bot educacional de MEV e arbitragem em ambiente controlado |
| [chaos-engineering-trading-toolkit](https://github.com/SrSatriano/chaos-engineering-trading-toolkit) | chaos engineering aplicado a bots e ambientes de trading |
| [dark-pool-market-impact-simulator](https://github.com/SrSatriano/dark-pool-market-impact-simulator) | simulação de impacto de mercado e liquidez oculta |
| [tax-loss-harvesting-engine](https://github.com/SrSatriano/tax-loss-harvesting-engine) | regras fiscais e compensação de perdas para contexto brasileiro |

</details>

<details>
<summary><b>IA local, mídia e avaliação</b></summary>

| Repo | Foco |
|---|---|
| [local-rag-second-mind-vault](https://github.com/SrSatriano/local-rag-second-mind-vault) | RAG offline para conhecimento pessoal e privado |
| [distributed-ai-inference-cluster](https://github.com/SrSatriano/distributed-ai-inference-cluster) | gateway para distribuir inferência entre workers |
| [voice-cloning-tts-api-gateway](https://github.com/SrSatriano/voice-cloning-tts-api-gateway) | API de TTS e clonagem de voz self-hosted |
| [autonomous-short-form-video-pipeline](https://github.com/SrSatriano/autonomous-short-form-video-pipeline) | pipeline de vídeos curtos com roteiro, áudio e render |
| [viral-trend-sentiment-predictor](https://github.com/SrSatriano/viral-trend-sentiment-predictor) | predição de tendências e sentimento em séries temporais |
| [realtime-deepfake-streaming-bridge](https://github.com/SrSatriano/realtime-deepfake-streaming-bridge) | ponte CUDA para processamento de vídeo em tempo real |
| [cognitive-bias-hallucination-trap](https://github.com/SrSatriano/cognitive-bias-hallucination-trap) | testes adversariais e QA para respostas de LLMs |
| [algorithmic-lofi-audio-generator](https://github.com/SrSatriano/algorithmic-lofi-audio-generator) | geração procedural de trilhas lo-fi para vídeos |

</details>

<details>
<summary><b>Produto, SaaS, fiscal BR e analytics</b></summary>

| Repo | Foco |
|---|---|
| [multi-channel-analytics-dashboard](https://github.com/SrSatriano/multi-channel-analytics-dashboard) | dashboard full-stack para métricas e inteligência de canais |
| [fiscal-data-ocr-engine](https://github.com/SrSatriano/fiscal-data-ocr-engine) | OCR, extração e validação de documentos fiscais |
| [enterprise-b2b-saas-boilerplate](https://github.com/SrSatriano/enterprise-b2b-saas-boilerplate) | base SaaS B2B com autenticação, RBAC e multi-tenancy |
| [family-treasury-dao-tracker](https://github.com/SrSatriano/family-treasury-dao-tracker) | tesouraria, metas e projeções financeiras |

</details>

<details>
<summary><b>Web3, identidade e segurança on-chain</b></summary>

| Repo | Foco |
|---|---|
| [tokenomics-staking-protocol](https://github.com/SrSatriano/tokenomics-staking-protocol) | token ERC-20, staking e testes de contrato |
| [identity-vault-zk-proofs](https://github.com/SrSatriano/identity-vault-zk-proofs) | identidade com provas de conhecimento zero |
| [p2p-orderbook-gossip](https://github.com/SrSatriano/p2p-orderbook-gossip) | order book descentralizado com protocolo gossip |
| [honeypot-rugpull-analyzer](https://github.com/SrSatriano/honeypot-rugpull-analyzer) | análise estática de contratos e risco de honeypot |
| [cross-border-ledger-fabric](https://github.com/SrSatriano/cross-border-ledger-fabric) | ledger permissionado com Hyperledger Fabric |

</details>

<details>
<summary><b>Infraestrutura, sistemas e operação</b></summary>

| Repo | Foco |
|---|---|
| [zero-to-hero-workstation-provisioner](https://github.com/SrSatriano/zero-to-hero-workstation-provisioner) | provisionamento de workstation com Ansible |
| [ebpf-latency-tracer-financial](https://github.com/SrSatriano/ebpf-latency-tracer-financial) | tracer eBPF para latência de rede em contexto financeiro |
| [hypervisor-ai-isolation](https://github.com/SrSatriano/hypervisor-ai-isolation) | isolamento de workloads de IA em camada de virtualização |
| [gitops-infra-state-reconciler](https://github.com/SrSatriano/gitops-infra-state-reconciler) | reconciliação de estado entre Git e infraestrutura |
| [high-compression-log-router](https://github.com/SrSatriano/high-compression-log-router) | roteamento de logs com alta compressão e throughput |

</details>

<details>
<summary><b>Arquivo, estudo e primeiros projetos</b></summary>

| Repo | Foco |
|---|---|
| [IA-Financeira](https://github.com/SrSatriano/IA-Financeira) | primeiras explorações de IA aplicada a finanças |
| [PersonalAI](https://github.com/SrSatriano/PersonalAI) | assistente pessoal e estudos de automação |
| [calculadora-de-notas](https://github.com/SrSatriano/calculadora-de-notas) | ferramenta acadêmica utilitária |
| [Python_Senac_RIo_On](https://github.com/SrSatriano/Python_Senac_RIo_On) | exercícios e códigos de curso |
| [portfolio-matheus-satriano](https://github.com/SrSatriano/portfolio-matheus-satriano) | site público com filtros, vitrine e navegação visual |

</details>

---

## Como navegar pelo meu GitHub

| Se você quer ver | Comece por |
|---|---|
| **Sistemas de mercado e performance** | [Order Book](https://github.com/SrSatriano/ultra-low-latency-order-book-engine), [AVX-512 Pricing](https://github.com/SrSatriano/avx512-options-pricing-engine), [LHN](https://github.com/SrSatriano/LHN-V90-IA) |
| **IA local e privacidade** | [Second Mind Vault](https://github.com/SrSatriano/local-rag-second-mind-vault), [Distributed AI Inference](https://github.com/SrSatriano/distributed-ai-inference-cluster) |
| **Produto full-stack** | [Analytics Dashboard](https://github.com/SrSatriano/multi-channel-analytics-dashboard), [SaaS Boilerplate](https://github.com/SrSatriano/enterprise-b2b-saas-boilerplate) |
| **Brasil e fiscal** | [Fiscal OCR](https://github.com/SrSatriano/fiscal-data-ocr-engine), [Tax-Loss Harvesting](https://github.com/SrSatriano/tax-loss-harvesting-engine) |
| **Infra e operação** | [Log Router](https://github.com/SrSatriano/high-compression-log-router), [GitOps Reconciler](https://github.com/SrSatriano/gitops-infra-state-reconciler), [eBPF Tracer](https://github.com/SrSatriano/ebpf-latency-tracer-financial) |

---

<a id="atividade-e-contato"></a>

## Atividade e contato

<div align="center">

<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=SrSatriano&theme=github_dark" alt="Estatísticas detalhadas do perfil GitHub" />
<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=SrSatriano&theme=github_dark" alt="Linguagens por repositório" />
<img height="180" src="https://streak-stats.demolab.com/?user=SrSatriano&theme=tokyonight&hide_border=true&background=0f172a&ring=22c55e&fire=38bdf8&currStreakLabel=38bdf8" alt="Sequência de contribuições no GitHub" />

<br/><br/>

<table>
  <tr>
    <td><strong>Portfólio</strong></td>
    <td><a href="https://srsatriano.github.io/portfolio-matheus-satriano/">srsatriano.github.io/portfolio-matheus-satriano</a></td>
  </tr>
  <tr>
    <td><strong>GitHub</strong></td>
    <td><a href="https://github.com/SrSatriano">github.com/SrSatriano</a></td>
  </tr>
  <tr>
    <td><strong>LinkedIn</strong></td>
    <td><a href="https://www.linkedin.com/in/matheus-rodrigues-satriano">linkedin.com/in/matheus-rodrigues-satriano</a></td>
  </tr>
  <tr>
    <td><strong>g.dev</strong></td>
    <td><a href="https://g.dev/satriano">g.dev/satriano</a></td>
  </tr>
  <tr>
    <td><strong>E-mail</strong></td>
    <td><a href="mailto:matheussatriano@hotmail.com">matheussatriano@hotmail.com</a></td>
  </tr>
</table>

<br/>

<a href="https://www.buymeacoffee.com/matheussatriano">
  <img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy me a coffee" />
</a>

<br/><br/>

<p><strong>Aberto a desafios técnicos, projetos open source, back-end, sistemas quant, IA local e boas conversas sobre latência.</strong></p>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0891b2,50:134e4a,100:050816&height=120&section=footer&animation=twinkling" width="100%" alt="" />
