
# ∿Lib: Collapse Logic for Post-Quantum Cryptography

**∿Lib** implements symbolic collapse filtering for cryptographic systems under AI and quantum threat.  
It introduces a non-binary operator (`∿`) to detect and reject semantically mirrored key structures, adversarial inputs, and identity compromises.

---

## 🔐 Core Features

- Symbolic ∿ operator for adversarial key rejection
- Integration with post-quantum cryptographic systems (e.g. CRYSTALS-Dilithium)
- Empirical threshold optimization with ROC analysis
- 7+ adversary types: mirror, rotate, flip, XOR, compound
- Sub-3ms performance with <10MB memory footprint
- Self-nullifying identity credential modeling

---

## 📦 Repository Structure

```
lib/           # Core ∿ logic: aun_operator, transforms
examples/      # PQC integration scaffolds
tests/         # Adversarial testing framework
docs/          # Visuals, reports, and site materials
arxiv_submission/  # Whitepaper and metadata
```

---

## 📊 Performance Snapshot

- ROC AUC: 0.61
- Optimal collapse at `t = 6`, `s_min = 0.4`
- F1 Score Peak: 0.65 (under subtle XOR + mirror conditions)

---

## 📜 License

MIT © 2025 Jerry Katz  
[halifaxjerrykatz@gmail.com](mailto:halifaxjerrykatz@gmail.com)

This research bridges nonduality logic with cryptographic resilience.

---

_For full documentation, clone the repo or see the whitepaper in `/arxiv_submission`._
