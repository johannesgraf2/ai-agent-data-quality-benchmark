# 🗺️ Project Roadmap

## Phase 1: Foundation ✅ (Current)
- [x] Create GitHub repository
- [x] Define agent architecture (4 specialized agents)
- [x] Set up project structure (backend, frontend, docs)
- [x] Implement core metrics (F1, corruption rate)
- [x] Create basic FastAPI skeleton
- [x] Initialize React + Vite frontend

## Phase 2: Metrics Implementation (Week 1)
**Metrics Agent tasks:**
- [ ] Implement distribution drift (KL divergence, Wasserstein)
- [ ] Implement reliability scoring (execution similarity)
- [ ] Implement robustness metric
- [ ] Create auditability scorer (LLM-as-judge)
- [ ] Write comprehensive unit tests
- [ ] Document all formulas and assumptions

**Research Agent tasks:**
- [ ] Write `docs/METHODOLOGY.md` with benchmark design
- [ ] Define 108 task specifications
- [ ] Document error injection strategies
- [ ] Create ground truth validation process

## Phase 3: Backend Development (Week 2)
**Backend Agent tasks:**
- [ ] Implement benchmark executor (task orchestration)
- [ ] Build model client wrappers (Gemini, GPT, Claude)
- [ ] Create dataset loader and error injection pipeline
- [ ] Implement results storage (JSON or DB)
- [ ] Build all API endpoints
- [ ] Add async execution for parallel tasks
- [ ] Error handling and logging

## Phase 4: Frontend Dashboard (Week 3)
**Visualization Agent tasks:**
- [ ] Create Overview Page (global KPIs + dimension bars)
- [ ] Build Dimension Deep Dive (per-dimension analysis)
- [ ] Implement Task-Level Explorer (diff visualization)
- [ ] Create confusion matrix component
- [ ] Build drift comparison charts
- [ ] Add heatmap for corruption by column
- [ ] Implement responsive layout
- [ ] Add loading states and error handling

## Phase 5: Dataset Preparation (Week 4)
**Research Agent tasks:**
- [ ] Curate 9 diverse datasets (e-commerce, healthcare, finance, etc.)
- [ ] Clean and validate datasets
- [ ] Implement error injection for each dimension
- [ ] Create protected columns for corruption detection
- [ ] Generate ground truth files
- [ ] Document dataset characteristics

## Phase 6: Benchmark Execution (Week 5)
**Backend Agent tasks:**
- [ ] Run full 108-task benchmark on Gemini 3 Pro
- [ ] Compute all metrics
- [ ] Generate result files
- [ ] Create reliability tests (duplicate runs)
- [ ] Perform robustness tests (perturbations)
- [ ] Collect auditability justifications

**Research Agent tasks:**
- [ ] Validate results for statistical significance
- [ ] Analyze failure modes
- [ ] Document findings in `docs/RESULTS.md`

## Phase 7: Model Comparison (Week 6)
**Backend Agent tasks:**
- [ ] Run benchmark on GPT-5.1 (if budget allows)
- [ ] Run benchmark on Claude 4 (if budget allows)
- [ ] Compare results across models

**Research Agent tasks:**
- [ ] Statistical comparison (paired t-tests)
- [ ] Effect size analysis
- [ ] Document comparative findings

## Phase 8: Dashboard Polish (Week 7)
**Visualization Agent tasks:**
- [ ] Refine UI/UX based on feedback
- [ ] Add model comparison views
- [ ] Improve accessibility (WCAG AA)
- [ ] Optimize performance (lazy loading, virtualization)
- [ ] Create export functionality (PDF reports, CSV data)

## Phase 9: Documentation & Thesis Writing (Week 8-10)
**Research Agent tasks:**
- [ ] Write methodology chapter
- [ ] Document results and analysis
- [ ] Create visualizations for thesis
- [ ] Write discussion and limitations
- [ ] Prepare thesis defense presentation

**All Agents:**
- [ ] Code cleanup and refactoring
- [ ] Final testing and validation
- [ ] README and documentation polish

## Phase 10: Deployment & Sharing (Week 11)
**Backend Agent tasks:**
- [ ] Deploy backend to cloud (Heroku/Railway/Fly.io)
- [ ] Set up CI/CD pipeline

**Visualization Agent tasks:**
- [ ] Deploy frontend (Netlify/Vercel)
- [ ] Configure custom domain (optional)

**Research Agent tasks:**
- [ ] Prepare public demo
- [ ] Write blog post or paper
- [ ] Share with academic community

---

## Next Immediate Steps

**Johannes, you should:**
1. **Review this architecture** - Does it match your thesis vision?
2. **Clarify model focus** - Primary focus on Gemini 3 Pro, or test multiple?
3. **Dataset planning** - Do you have specific datasets in mind, or should agents curate?
4. **Budget considerations** - API costs for 108 tasks × models × reliability runs
5. **Timeline** - Is this 11-week timeline feasible for your thesis deadline?

**Agents are ready to:**
- Metrics Agent → Continue implementing drift, reliability, robustness
- Backend Agent → Build the benchmark executor
- Visualization Agent → Start building React dashboard
- Research Agent → Document methodology and task specifications

🦞 **What would you like to focus on first?**
