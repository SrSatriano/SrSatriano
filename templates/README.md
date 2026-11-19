<a id="topo"></a>

<div align="center">

{{pic:banner.svg|Matheus Rodrigues Satriano: back-end, sistemas quant, IA local e infraestrutura soberana}}

<br/><br/>

<a href="https://srsatriano.github.io/portfolio-matheus-satriano/"><img src="https://img.shields.io/badge/Portf%C3%B3lio-online-0891b2?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfólio online" /></a>
<a href="https://github.com/SrSatriano?tab=repositories"><img src="https://img.shields.io/badge/Reposit%C3%B3rios-{{COUNT}}_p%C3%BAblicos-181717?style=for-the-badge&logo=github" alt="Repositórios no GitHub" /></a>
<a href="https://www.linkedin.com/in/matheus-rodrigues-satriano"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:matheussatriano@hotmail.com"><img src="https://img.shields.io/badge/E--mail-contato-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" /></a>

<br/><br/>

{{STATS}}

<br/><br/>

{{pic:terminal.svg|Terminal: LHN Sovereign V90; C++, Rust, Python, TypeScript, Go, Kotlin; se o problema não precisa sair da máquina, ele roda local}}

</div>

<br/>

<div align="center">

### 🧭 Navegue pelas frentes

{{NAV}}

<br/>

<sub>
<a href="#quem-sou">👋 Quem sou</a> ·
<a href="#em-numeros">📊 Em números</a> ·
<a href="#lhn-sovereign-v90">🛰️ LHN V90</a> ·
<a href="#destaques">⭐ Destaques</a> ·
<a href="#catalogo">🗂️ Catálogo</a> ·
<a href="#ecossistema">🔗 Ecossistema</a> ·
<a href="#por-onde-comecar">🧑‍💻 Por onde começar</a> ·
<a href="#stack">🧰 Stack</a> ·
<a href="#atividade">📈 Atividade</a> ·
<a href="#contato">📬 Contato</a>
</sub>

</div>

---

<a id="quem-sou"></a>

## 👋 Quem sou

Sou **Matheus Rodrigues Satriano**, graduando em **Ciência da Computação** e desenvolvedor focado em sistemas que exigem **controle, desempenho e clareza operacional**.

Meu centro de gravidade é back-end, mas eu atravesso a stack quando isso melhora o produto: APIs, painéis, motores de execução, apps Android, infraestrutura local, automação, telemetria e modelos de IA rodando perto dos dados.

| Direção | Como isso vira código | Onde ver |
|---|---|---|
| ⚡ **Baixa latência** | C++20, Rust, SIMD/AVX-512, estruturas de dados e benchmarks | [Order Book](https://github.com/SrSatriano/ultra-low-latency-order-book-engine) · [AVX-512 Pricing](https://github.com/SrSatriano/avx512-options-pricing-engine) |
| 🧠 **IA local** | RAG offline, Ollama, gateway de inferência, avaliação de LLMs | [Second Mind Vault](https://github.com/SrSatriano/local-rag-second-mind-vault) · [infergw](https://github.com/SrSatriano/distributed-ai-inference-cluster) |
| 📈 **Mercado financeiro** | order book, pricing, risco, SMC, imposto na B3 e painéis operacionais | [LHN V90](https://github.com/SrSatriano/LHN-V90-IA) · [SMC Scanner](https://github.com/SrSatriano/smc-liquidity-scanner) |
| 🛠️ **Infra soberana** | Docker, Ansible, eBPF, GitOps e logs comprimidos, sem depender de nuvem | [logroute](https://github.com/SrSatriano/high-compression-log-router) · [eBPF Tracer](https://github.com/SrSatriano/ebpf-latency-tracer-financial) |
| 🇧🇷 **Produto real** | NF-e, IR na B3, vagas, finanças pessoais, com README e testes | [Fiscal OCR](https://github.com/SrSatriano/fiscal-data-ocr-engine) · [Vagas Alerta](https://github.com/SrSatriano/vagas-alerta) |

> [!TIP]
> **Princípio pessoal:** se o problema não precisa sair da máquina, ele deve conseguir rodar local. A nuvem entra por necessidade técnica, não por reflexo.

---

<a id="em-numeros"></a>

## 📊 Em números

<div align="center">

{{pic:overview.svg|Resumo dos repositórios públicos}}

{{pic:categories.svg|Projetos por frente de trabalho}}

<table>
<tr>
<td width="50%">{{pic:languages.svg|Projetos por linguagem principal}}</td>
<td width="50%">{{pic:timeline.svg|Linha do tempo dos repositórios}}</td>
</tr>
</table>

</div>

---

<a id="lhn-sovereign-v90"></a>

## 🛰️ LHN Sovereign V90

<table>
<tr>
<td width="52%" valign="top">

**LHN Sovereign V90** é meu terminal quantitativo local para pesquisa, automação controlada e operação assistida em cripto.

Ele combina **FastAPI**, **Next.js**, integração com **Bybit V5** (REST + WebSocket), camadas de risco, workspace local e módulos de IA em Keras/TensorFlow. A ideia central: manter o operador no controle, reduzir dependências externas e deixar o sistema observável.

| Camada | Papel |
|---|---|
| 🖥️ **Painel** | leitura de estado, parâmetros e operação |
| 🔌 **API** | orquestração, configuração, risco, execução e integração |
| ⚙️ **Core** | decisão, replay, backfill, radar, labeler e ciclo de treino |
| 🧠 **IA local** | inferência e análise perto dos dados |
| 🗄️ **Workspace** | persistência, auditoria, logs e artefatos |
| 📱 **Mirror** | painel remoto no Android ([lhn-android-apps](https://github.com/SrSatriano/lhn-android-apps)) |

> **Licença:** PolyForm Noncommercial. O código é público para estudo, mas não é MIT.

</td>
<td width="48%" valign="top" align="center">

<a href="https://github.com/SrSatriano/LHN-V90-IA">{{pic:cards/LHN-V90-IA.svg|LHN Sovereign V90}}</a>

<br/><br/>

<a href="https://github.com/SrSatriano/LHN-V90-IA"><img src="https://img.shields.io/badge/Abrir_o_reposit%C3%B3rio-LHN--V90--IA-0891b2?style=for-the-badge&logo=github" alt="Abrir o repositório LHN-V90-IA" /></a>

<img src="https://img.shields.io/badge/FastAPI-9002-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI na porta 9002" />
<img src="https://img.shields.io/badge/Next.js-9090-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js na porta 9090" />
<img src="https://img.shields.io/badge/Bybit-V5-f7a600?style=flat-square" alt="Bybit V5" />
<img src="https://img.shields.io/badge/IA-local-22c55e?style=flat-square" alt="IA local" />

</td>
</tr>
</table>

<div align="center">

{{pic:lhn-architecture.svg|Arquitetura do LHN Sovereign V90}}

</div>

---

<a id="destaques"></a>

## ⭐ Destaques

Os projetos que eu mostraria primeiro. Cada card abre o repositório.

<div align="center">

{{FEATURED}}

</div>

---

<a id="catalogo"></a>

## 🗂️ Catálogo completo

Todos os {{COUNT}} repositórios públicos, agrupados por frente. À esquerda, o card (clique para abrir); à direita, os destaques técnicos, a stack, o status do CI e os links úteis.

> [!NOTE]
> **Selos nos cards:** `★ DESTAQUE` bom ponto de partida · `CI` testes no GitHub Actions · `ONLINE` tem site publicado · `MIT` / `POLYFORM NC` licença.

{{CATALOG}}

---

<a id="ecossistema"></a>

## 🔗 Ecossistema

Cada frente orbita o LHN: os módulos isolam um problema (latência, risco, inferência, logs) para estudar e medir separado, e o que amadurece volta para o sistema principal.

<div align="center">

{{pic:constellation.svg|Constelação dos repositórios públicos por frente}}

</div>

---

<a id="por-onde-comecar"></a>

## 🧑‍💻 Por onde começar

| Se você quer ver… | Comece por | Por quê |
|---|---|---|
| ⚡ **Performance e microestrutura** | [Order Book](https://github.com/SrSatriano/ultra-low-latency-order-book-engine) → [AVX-512 Pricing](https://github.com/SrSatriano/avx512-options-pricing-engine) | C++20 sem dependências, benchmarks e CI |
| 🛰️ **Um sistema completo** | [LHN Sovereign V90](https://github.com/SrSatriano/LHN-V90-IA) → [LHN Android](https://github.com/SrSatriano/lhn-android-apps) | back-end, painel, risco, IA e app móvel |
| 🧠 **IA local e privacidade** | [Second Mind Vault](https://github.com/SrSatriano/local-rag-second-mind-vault) → [infergw](https://github.com/SrSatriano/distributed-ai-inference-cluster) | RAG com citações e gateway OpenAI-compatível |
| 🇧🇷 **Produto para o Brasil** | [Fiscal OCR](https://github.com/SrSatriano/fiscal-data-ocr-engine) → [Tax-Loss B3](https://github.com/SrSatriano/tax-loss-harvesting-engine) | NF-e, DANFE e imposto de renda na B3 |
| 🔔 **Ferramentas do dia a dia** | [Vagas Alerta](https://github.com/SrSatriano/vagas-alerta) → [RotaNorte](https://github.com/SrSatriano/rotanorte) | coleta, deduplicação, notas e alertas no Telegram |
| 🎬 **Criação de conteúdo** | [VideoOS](https://github.com/SrSatriano/videoos) → [Channel Analytics](https://github.com/SrSatriano/multi-channel-analytics-dashboard) | edição em massa e métricas de canais |
| 🦀 **Rust e sistemas** | [logroute](https://github.com/SrSatriano/high-compression-log-router) → [Terminal TUI](https://github.com/SrSatriano/unified-trading-super-terminal) | Zstd, CLI, Ratatui e testes |
| ⛓️ **Web3** | [Identity Vault ZK](https://github.com/SrSatriano/identity-vault-zk-proofs) → [Honeypot Analyzer](https://github.com/SrSatriano/honeypot-rugpull-analyzer) | provas Groth16 e análise de contratos |

<details>
<summary><b>💡 Como rodar qualquer projeto</b></summary>

<br/>

Todos os repositórios têm README em português com pré-requisitos, instalação, configuração e testes. O caminho costuma ser o mesmo:

```bash
git clone https://github.com/SrSatriano/<repositorio>.git
cd <repositorio>
# siga a seção "Instalação e execução" do README
```

Projetos com selo **CI** rodam os testes a cada push; clique no selo para ver a última execução no GitHub Actions.

</details>

<a id="indice"></a>

<details>
<summary><b>📇 Índice A–Z: todos os {{COUNT}} projetos em uma tabela</b></summary>

<br/>

{{INDEX}}

</details>

---

<a id="stack"></a>

## 🧰 Stack

<div align="center">

**Linguagens e core**

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=python,rust,cpp,typescript,go,kotlin,java,javascript,solidity,bash&perline=10&theme=light" />
  <img src="https://skillicons.dev/icons?i=python,rust,cpp,typescript,go,kotlin,java,javascript,solidity,bash&perline=10" alt="Python, Rust, C++, TypeScript, Go, Kotlin, Java, JavaScript, Solidity e Bash" />
</picture>

<br/><br/>

**Web, APIs, mobile e dados**

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=fastapi,nextjs,react,vite,tailwind,nodejs,androidstudio,postgres,sqlite,redis&perline=10&theme=light" />
  <img src="https://skillicons.dev/icons?i=fastapi,nextjs,react,vite,tailwind,nodejs,androidstudio,postgres,sqlite,redis&perline=10" alt="FastAPI, Next.js, React, Vite, Tailwind, Node.js, Android, PostgreSQL, SQLite e Redis" />
</picture>

<br/><br/>

**IA e infraestrutura**

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=tensorflow,pytorch,sklearn,docker,ansible,linux,githubactions,nginx,grafana,prometheus&perline=10&theme=light" />
  <img src="https://skillicons.dev/icons?i=tensorflow,pytorch,sklearn,docker,ansible,linux,githubactions,nginx,grafana,prometheus&perline=10" alt="TensorFlow, PyTorch, scikit-learn, Docker, Ansible, Linux, GitHub Actions, Nginx, Grafana e Prometheus" />
</picture>

<br/><br/>

<img src="https://img.shields.io/badge/C%2B%2B20-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++20" />
<img src="https://img.shields.io/badge/AVX--512-512BD4?style=flat-square&logo=intel&logoColor=white" alt="AVX-512" />
<img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA" />
<img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white" alt="Jetpack Compose" />
<img src="https://img.shields.io/badge/PySide6-41CD52?style=flat-square&logo=qt&logoColor=white" alt="PySide6" />
<img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic" />
<img src="https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white" alt="Electron" />
<img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white" alt="Ollama" />
<img src="https://img.shields.io/badge/vLLM-30A2FF?style=flat-square" alt="vLLM" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain" />
<img src="https://img.shields.io/badge/Whisper-412991?style=flat-square" alt="Whisper" />
<img src="https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white" alt="FFmpeg" />
<img src="https://img.shields.io/badge/eBPF-000000?style=flat-square" alt="eBPF" />
<img src="https://img.shields.io/badge/QEMU%2FKVM-FF6600?style=flat-square&logo=qemu&logoColor=white" alt="QEMU/KVM" />
<img src="https://img.shields.io/badge/Zstd-5A5A5A?style=flat-square" alt="Zstd" />
<img src="https://img.shields.io/badge/libp2p-000000?style=flat-square" alt="libp2p" />
<img src="https://img.shields.io/badge/Bybit_V5-F7A600?style=flat-square" alt="Bybit V5" />
<img src="https://img.shields.io/badge/MetaTrader_5-0B6BB4?style=flat-square" alt="MetaTrader 5" />
<img src="https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white" alt="Solidity" />
<img src="https://img.shields.io/badge/Hardhat-FFF100?style=flat-square&logo=hardhat&logoColor=black" alt="Hardhat" />
<img src="https://img.shields.io/badge/Circom-ZK-6d28d9?style=flat-square" alt="Circom, ZK" />
<img src="https://img.shields.io/badge/Hyperledger_Fabric-2F2F72?style=flat-square&logo=hyperledger&logoColor=white" alt="Hyperledger Fabric" />

</div>

<details>
<summary><b>🧪 Como eu construo</b></summary>

<br/>

| Camada | Preferência técnica |
|---|---|
| **Core** | código mensurável, explícito e testável; benchmark antes de otimizar |
| **API** | contratos simples, FastAPI, OpenAPI e validação com Pydantic |
| **Interface** | Next.js, TUI em Rust, Jetpack Compose ou PySide6, conforme quem vai usar |
| **Dados** | SQLite (com FTS5 e WAL) quando basta, PostgreSQL e Redis quando a carga pede |
| **IA** | modelos open source, RAG offline, avaliação contra baseline e nada de promessa que o modelo não cumpre |
| **Operação** | logs úteis, health checks, Docker Compose, CI no GitHub Actions e README em português |

</details>

---

<a id="atividade"></a>

## 📈 Atividade

<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=SrSatriano&theme=default" />
  <img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=SrSatriano&theme=github_dark" alt="Estatísticas detalhadas do perfil GitHub" />
</picture>
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=SrSatriano&theme=default" />
  <img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=SrSatriano&theme=github_dark" alt="Linguagens por repositório" />
</picture>
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com/?user=SrSatriano&theme=default&hide_border=true" />
  <img height="180" src="https://streak-stats.demolab.com/?user=SrSatriano&theme=tokyonight&hide_border=true&background=0f172a&ring=22c55e&fire=38bdf8&currStreakLabel=38bdf8" alt="Sequência de contribuições no GitHub" />
</picture>

</div>

---

<a id="contato"></a>

## 📬 Contato

<div align="center">

<table>
  <tr><td align="center">🌐</td><td><strong>Portfólio</strong></td><td><a href="https://srsatriano.github.io/portfolio-matheus-satriano/">srsatriano.github.io/portfolio-matheus-satriano</a></td></tr>
  <tr><td align="center">🎬</td><td><strong>Satriano Studio</strong></td><td><a href="https://srsatriano.github.io/satriano-studio/">srsatriano.github.io/satriano-studio</a></td></tr>
  <tr><td align="center">🐙</td><td><strong>GitHub</strong></td><td><a href="https://github.com/SrSatriano">github.com/SrSatriano</a></td></tr>
  <tr><td align="center">💼</td><td><strong>LinkedIn</strong></td><td><a href="https://www.linkedin.com/in/matheus-rodrigues-satriano">linkedin.com/in/matheus-rodrigues-satriano</a></td></tr>
  <tr><td align="center">🧑‍💻</td><td><strong>g.dev</strong></td><td><a href="https://g.dev/satriano">g.dev/satriano</a></td></tr>
  <tr><td align="center">✉️</td><td><strong>E-mail</strong></td><td><a href="mailto:matheussatriano@hotmail.com">matheussatriano@hotmail.com</a></td></tr>
</table>

<br/>

<a href="https://www.buymeacoffee.com/matheussatriano"><img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy me a coffee" /></a>

<br/><br/>

**Aberto a desafios técnicos, projetos open source, back-end, sistemas quant, IA local e boas conversas sobre latência.**

<sub>Atualizado em {{UPDATED}} · visuais gerados por <a href="scripts/build_profile.py"><code>scripts/build_profile.py</code></a> a partir de <a href="data/projects.json"><code>data/projects.json</code></a> · tema claro e escuro automáticos</sub>

<br/><br/>

<a href="#topo">⬆ voltar ao topo</a>

<br/><br/>

{{pic:footer.svg|}}

</div>
