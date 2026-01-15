<div align="center">
  <img src="./docs/source/_static/besser_logo_light.png" alt="BESSER platform" width="500"/>
</div>

# B-UML Dataset


The **B-UML Dataset** is a large-scale dataset containing **5,000+ B-UML models**, designed to support research in **modeling languages**, **model-driven engineering (MDE)**, and **AI-assisted modeling**.

The dataset provides **multiple synchronized representations** of each model, enabling reproducible, quantitative, and scalable experimentation.

---

## 📦 Dataset Overview

Each entry in the B-UML Dataset includes:

- **B-UML Model**  
  Editable in the **BESSER Web Modeling Environment (WME)**

- **Model Image**  
  Rendered visual representation of the model

- **Structured Metadata**
  - Number of classes  
  - Number of associations  
  - Number of attributes  
  - Number of functions (operations)

- **Deterministic Textual Description**
  - Classes  
  - Attributes  
  - Associations  
  > Generated deterministically for reproducibility (no prompt randomness)

- **Python Code**
  - Programmatic representation of the model  
  - Suitable for automation, analysis, and ML pipelines

- **Labels / Categories**
  - Consistent labels derived from the underlying database  
  - Enable controlled experiments and category-based evaluation

---

## 🧠 Origin of the Dataset

The B-UML Dataset is **derived from the Ecore-based Modelset**, a well-established collection of models in the community

🔗 https://models-lab.github.io/blog/2021/modelset/

The original Ecore models were systematically transformed and enriched into **B-UML representations**, while preserving structural diversity and consistency.


---

## 🛠 Tool Support

- **BESSER Web Modeling Environment (WME)**  
  All B-UML models are directly editable in BESSER WME.

---

## 🎯 Intended Use Cases

The dataset is suitable for:

- Benchmarking modeling tools and transformations  
- Model-to-text and text-to-model research  
- LLM evaluation and training for modeling tasks  
- Model analysis and metrics-based studies  
- Teaching and experimentation in MDE courses  

If your evaluation previously relied on “a small illustrative example”, this dataset is for you.

---

## 📁 Repository Structure 

```text
dataset/
├── model_1
│   ├── name_BUML_model
│   ├── image.png
│   ├── metadata.txt
│   ├── python_code.txt
│   ├── model_path.txt
│   ├── textual_description.txt
│   └── category.txt
readme.md

## Code of Conduct

At BESSER, our commitment is centered on establishing and maintaining development environments that are welcoming, inclusive, safe and free from all forms of harassment. All participants are expected to voluntarily respect and support our [Code of Conduct](CODE_OF_CONDUCT.md).

## Governance

The development of this project follows the governance rules described in the [GOVERNANCE.md](GOVERNANCE.md) document.

## Contact
You can reach us at: [info@besser-pearl.org](mailto:info@besser-pearl-org)

Website: https://besser-pearl.org

## License

This project is licensed under the [MIT](https://mit-license.org/) license.
