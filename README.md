<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1e3a8a,100:0891b2&height=180&section=header&text=Matheus%20Rodrigues%20Satriano&fontSize=36&fontColor=ffffff&animation=twinkling" width="100%" alt="" />

<div align="center">

### Desenvolvedor back-end · HFT · IA · Web3

[![Portfólio web](https://img.shields.io/badge/Portfólio_web-acesse-0891b2?style=for-the-badge)](https://srsatriano.github.io/portfolio-matheus-satriano/)
[![GitHub](https://img.shields.io/badge/GitHub-SrSatriano-181717?style=for-the-badge&logo=github)](https://github.com/SrSatriano)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-conectar-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/matheus-rodrigues-satriano)
[![E-mail](https://img.shields.io/badge/E--mail-contato-EA4335?style=for-the-badge&logo=gmail)](mailto:matheussatriano@hotmail.com)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=20&pause=1000&color=38BDF8&center=true&width=620&lines=Back-end+%26+sistemas+de+mercado;Autor+do+LHN+Sovereign+V90;IA+local+%C2%B7+Web3+%C2%B7+Fiscal+BR" alt="" />

<br/>

<img src="https://img.shields.io/badge/LHN-Sovereign_V90-22c55e?style=flat-square" alt="" />
<img src="https://img.shields.io/badge/OSS-30_m%C3%B3dulos-0ea5e9?style=flat-square" alt="" />
<img src="https://img.shields.io/badge/Docs-pt--BR-blue?style=flat-square" alt="" />
<img src="https://img.shields.io/badge/Brasil-UTC--3-6b7280?style=flat-square" alt="" />

</div>

---

## Navegação rápida

| | Seção |
|:---:|---|
| ★ | [**LHN Sovereign V90**](#lhn-sovereign-v90) — sistema HFT principal |
| 1 | [Sobre](#sobre) |
| 2 | [Projetos em destaque](#destaques) |
| 3 | [Todos os repositórios](#repositorios) |
| 4 | [Stack](#stack) |
| 5 | [Contato](#contato) |
| 6 | [GitHub Stats](#stats) |

---

<a id="sobre"></a>

## Sobre

Graduando em **Ciência da Computação**. Desenvolvo **back-end**, sistemas para **mercados** e produtos com **IA** — com documentação em **português** e código aberto no GitHub.

| Foco | O que faço |
|------|------------|
| **Trading / HFT** | Terminal quant **[LHN Sovereign V90](https://github.com/SrSatriano/LHN-V90-IA)**, motores C++/Rust, pricing SIMD, simuladores |
| **IA** | RAG local, inferência, pipelines de mídia, testes anti-alucinação |
| **Web3 & BR** | Contratos, análise de tokens, OCR fiscal, tax-loss harvesting |

> Cada repositório OSS traz README e guias (`ARCHITECTURE`, `DEPLOYMENT`, `OPERATIONS`). O nível de implementação varia por projeto — limitações e roadmap estão documentados quando aplicável.

---

<a id="lhn-sovereign-v90"></a>

## LHN Sovereign V90

**Repositório principal · trading quantitativo em cripto**

<a href="https://github.com/SrSatriano/LHN-V90-IA">
<img src="https://github-readme-stats.vercel.app/api/pin/?username=SrSatriano&repo=LHN-V90-IA&theme=tokyonight&hide_border=true&bg_color=0f172a&title_color=38bdf8&icon_color=22c55e" alt="LHN-V90-IA" />
</a>

<table>
<tr>
<td width="50%" valign="top">

**O que é**  
Estação local para pesquisa, simulação e execução controlada em perpétuos **Bybit V5** (linear USDT).

**Stack**  
`Python` · `FastAPI` · `Next.js` · `Bybit V5` · `TensorFlow/Keras` · `WebSocket`

**Portas (padrão)**  
Painel **9090** · API **9002**

</td>
<td width="50%" valign="top">

**Inclui**  
Motor assíncrono, feeds WS/REST, IA (forja/replay), risco, guardian, Telegram, Nexus (LLM opcional).

**Licença**  
Source-available · **PolyForm Noncommercial** — estudo e experimentação; uso comercial requer acordo com o autor.

**Docs**  
README completo em pt-BR no repositório.

</td>
</tr>
</table>

```
Next.js (9090) ── REST / WS ──► FastAPI (9002) ──► Bybit · IA · workspace local
```

**→ [Abrir LHN-V90-IA no GitHub](https://github.com/SrSatriano/LHN-V90-IA)**

---

<a id="destaques"></a>

## Destaques

Módulos open source que complementam o ecossistema (release documentada **v1.0**).

<table>
<tr>
<th>Projeto</th>
<th>Descrição</th>
</tr>
<tr>
<td>

**[Order Book Engine](https://github.com/SrSatriano/ultra-low-latency-order-book-engine)**  
`C++` · gRPC · ZeroMQ

</td>
<td>Matching FIFO, sharding e benchmarks de latência</td>
</tr>
<tr>
<td>

**[AVX-512 Pricing](https://github.com/SrSatriano/avx512-options-pricing-engine)**  
`C++` · SIMD

</td>
<td>Black-Scholes e Monte Carlo vetorizados na CPU</td>
</tr>
<tr>
<td>

**[Second Mind Vault](https://github.com/SrSatriano/local-rag-second-mind-vault)**  
`Python` · FastAPI · Ollama

</td>
<td>RAG offline com ingestão e consulta via API</td>
</tr>
<tr>
<td>

**[Trading Super-Terminal](https://github.com/SrSatriano/unified-trading-super-terminal)**  
`Rust` · Ratatui

</td>
<td>TUI para risco, exposição e kill switch</td>
</tr>
<tr>
<td>

**[Analytics Dashboard](https://github.com/SrSatriano/multi-channel-analytics-dashboard)**  
`Next.js` · Recharts

</td>
<td>Métricas multicanal (RPM, retenção, conversão)</td>
</tr>
<tr>
<td>

**[Fiscal OCR](https://github.com/SrSatriano/fiscal-data-ocr-engine)** · **[Tax Harvest](https://github.com/SrSatriano/tax-loss-harvesting-engine)**  

</td>
<td>Ferramentas fiscais para o mercado brasileiro</td>
</tr>
</table>

**Site com todos os projetos:** [srsatriano.github.io/portfolio-matheus-satriano](https://srsatriano.github.io/portfolio-matheus-satriano/)

---

<a id="repositorios"></a>

## Repositórios

<details>
<summary><b>HFT & quant</b> — LHN + 8 módulos</summary>

| Repositório | Resumo |
|-------------|--------|
| [**LHN-V90-IA**](https://github.com/SrSatriano/LHN-V90-IA) | Sistema principal |
| [ultra-low-latency-order-book-engine](https://github.com/SrSatriano/ultra-low-latency-order-book-engine) | Order book C++ |
| [smc-liquidity-scanner](https://github.com/SrSatriano/smc-liquidity-scanner) | SMC + ML |
| [unified-trading-super-terminal](https://github.com/SrSatriano/unified-trading-super-terminal) | TUI Rust |
| [avx512-options-pricing-engine](https://github.com/SrSatriano/avx512-options-pricing-engine) | Pricing AVX-512 |
| [mempool-arbitrage-mev-bot](https://github.com/SrSatriano/mempool-arbitrage-mev-bot) | MEV educacional |
| [chaos-engineering-trading-toolkit](https://github.com/SrSatriano/chaos-engineering-trading-toolkit) | Chaos em homologação |
| [dark-pool-market-impact-simulator](https://github.com/SrSatriano/dark-pool-market-impact-simulator) | Simulador de impacto |
| [tax-loss-harvesting-engine](https://github.com/SrSatriano/tax-loss-harvesting-engine) | Harvest fiscal BR |

</details>

<details>
<summary><b>IA & dados</b> — 8 módulos</summary>

| Repositório | Resumo |
|-------------|--------|
| [local-rag-second-mind-vault](https://github.com/SrSatriano/local-rag-second-mind-vault) | RAG offline |
| [distributed-ai-inference-cluster](https://github.com/SrSatriano/distributed-ai-inference-cluster) | Cluster LLM |
| [voice-cloning-tts-api-gateway](https://github.com/SrSatriano/voice-cloning-tts-api-gateway) | TTS / voz |
| [autonomous-short-form-video-pipeline](https://github.com/SrSatriano/autonomous-short-form-video-pipeline) | Vídeo curto |
| [viral-trend-sentiment-predictor](https://github.com/SrSatriano/viral-trend-sentiment-predictor) | Trends + ML |
| [realtime-deepfake-streaming-bridge](https://github.com/SrSatriano/realtime-deepfake-streaming-bridge) | Pesquisa CUDA |
| [cognitive-bias-hallucination-trap](https://github.com/SrSatriano/cognitive-bias-hallucination-trap) | QA em LLMs |
| [algorithmic-lofi-audio-generator](https://github.com/SrSatriano/algorithmic-lofi-audio-generator) | Áudio lo-fi |

</details>

<details>
<summary><b>Produto & SaaS</b> — 4 módulos</summary>

| Repositório | Resumo |
|-------------|--------|
| [multi-channel-analytics-dashboard](https://github.com/SrSatriano/multi-channel-analytics-dashboard) | Dashboard |
| [fiscal-data-ocr-engine](https://github.com/SrSatriano/fiscal-data-ocr-engine) | OCR fiscal |
| [enterprise-b2b-saas-boilerplate](https://github.com/SrSatriano/enterprise-b2b-saas-boilerplate) | SaaS B2B |
| [family-treasury-dao-tracker](https://github.com/SrSatriano/family-treasury-dao-tracker) | Tesouraria familiar |

</details>

<details>
<summary><b>Web3</b> — 5 módulos</summary>

| Repositório | Resumo |
|-------------|--------|
| [tokenomics-staking-protocol](https://github.com/SrSatriano/tokenomics-staking-protocol) | Staking |
| [identity-vault-zk-proofs](https://github.com/SrSatriano/identity-vault-zk-proofs) | ZK proofs |
| [p2p-orderbook-gossip](https://github.com/SrSatriano/p2p-orderbook-gossip) | P2P order book |
| [honeypot-rugpull-analyzer](https://github.com/SrSatriano/honeypot-rugpull-analyzer) | Análise de tokens |
| [cross-border-ledger-fabric](https://github.com/SrSatriano/cross-border-ledger-fabric) | Hyperledger Fabric |

</details>

<details>
<summary><b>Infra & sistemas</b> — 5 módulos</summary>

| Repositório | Resumo |
|-------------|--------|
| [zero-to-hero-workstation-provisioner](https://github.com/SrSatriano/zero-to-hero-workstation-provisioner) | Ansible |
| [ebpf-latency-tracer-financial](https://github.com/SrSatriano/ebpf-latency-tracer-financial) | eBPF (Linux) |
| [hypervisor-ai-isolation](https://github.com/SrSatriano/hypervisor-ai-isolation) | Isolamento IA |
| [gitops-infra-state-reconciler](https://github.com/SrSatriano/gitops-infra-state-reconciler) | GitOps |
| [high-compression-log-router](https://github.com/SrSatriano/high-compression-log-router) | Logs Zstd |

</details>

---

<a id="stack"></a>

## Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/Rust-000?style=flat-square&logo=rust&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="" />
  <img src="https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white" alt="" />
</p>

---

<a id="contato"></a>

## Contato

<div align="center">

| | |
|---|---|
| **Portfólio** | [srsatriano.github.io/portfolio-matheus-satriano](https://srsatriano.github.io/portfolio-matheus-satriano/) |
| **Google Developers** | [g.dev/satriano](https://g.dev/satriano) |
| **E-mail** | matheussatriano@hotmail.com |

<br/>

<a href="https://www.buymeacoffee.com/matheussatriano">
  <img src="https://img.shields.io/badge/Buy_Me_a_Coffee-apoie-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="" />
</a>

</div>

---

<a id="stats"></a>

## GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=SrSatriano&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0f172a&title_color=38bdf8&icon_color=22c55e" alt="" />
<img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=SrSatriano&theme=tokyonight&hide_border=true&background=0f172a" alt="" />

<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=SrSatriano&layout=compact&theme=tokyonight&hide_border=true&bg_color=0f172a&title_color=38bdf8&langs_count=8" alt="" />

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0891b2,100:0f172a&height=80&section=footer" width="100%" alt="" />

**Comece pelo** [LHN Sovereign V90](https://github.com/SrSatriano/LHN-V90-IA) **ou pelo** [portfólio web](https://srsatriano.github.io/portfolio-matheus-satriano/)

<img src="https://img.shields.io/static/v1?label=&message=Aberto+a+oportunidades&color=22c55e&style=flat-square" alt="" />

</div>
