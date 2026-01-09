# XAVOS-Eval: X-Ray Angiography Video Object Segmentation Evaluation

<p align="left">
  <img src="https://img.shields.io/badge/XAVOS Task-VOS%20Evaluation-orange" alt="Task">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

---

## 🚀 Quick Start

### 📦 Installation

**Locally (recommended):**
```bash
git clone [https://github.com/xilin-x/xavos-eval](https://github.com/xilin-x/xavos-eval)
pip install -e xavos-eval
```

### 🛠️ Usage

#### ▶️ Run as a script
From the ```xavos-eval``` root directory:

```bash
python benchmark.py \
  -g <path to ground-truth directory> \
  -m <path to prediction directory> \
  -d <dataset type>

```
Supported dataset types:
 - ```DAVIS2016```
 - ```DAVIS2017```
 - ```MOSXAV-VAL```
 - ```MOSXAV-TEST```
 - ```XACV```
 - ```Other```

**Example**
```bash
# DAVIS 2016
python benchmark.py -g examples/DAVIS2016/gt -m examples/DAVIS2016/pred -d DAVIS2016

# DAVIS 2017
python benchmark.py -g examples/DAVIS2017/gt -m examples/DAVIS2017/pred -d DAVIS2017

# MOSXAV validation set
python benchmark.py -g examples/MOSXAV/val/gt -m examples/MOSXAV/val/pred -d MOSXAV-VAL

# MOSXAV test set
python benchmark.py -g examples/MOSXAV/test/gt -m examples/MOSXAV/test/pred -d MOSXAV-TEST

# XACV dataset
python benchmark.py -g examples/XACV/test/gt -m examples/XACV/test/pred -d XACV
```

#### 📚 Use as a Python library

```python
from xavos_eval.lib import benchmark

# Both arguments are lists: multiple datasets can be evaluated at once
benchmark(
    [<path to ground-truth directory>],
    [<path to prediction directory>],
    <dataset type>
)
```
[!TIP] See benchmark.py for an example, and see lib/benchmark.py for the function signature with additional options. A results.csv will be saved in the prediction directory.

💡 **Tip**
- **''See** ```benchmark.py``` **for a complete usage example''**
- **''See** ```lib/benchmark.py``` **for the full function signature and optional arguments''**
- **''A** ```results.csv``` **file will be automatically saved in the prediction directory''**


## 📝 Background

This toolkit is designed to **accelerate J&F evaluation** for **X-ray angiography video object segmentation (VOS)** benchmarks, including **MOSXAV** and **XACV**.

The implementation is adapted from the excellent [vos-benchmark](https://github.com/hkchengrex/vos-benchmark) repository and extended to support **X-ray angiography-specific datasets**.

The evaluation script has been **validated on DAVIS 2016/2017**, producing identical results to the official DAVIS evaluation code.

## 🔗 Related Projects

- **Official DAVIS 2017 evaluation implementation:** [https://github.com/davisvideochallenge/davis2017-evaluation](https://github.com/davisvideochallenge/davis2017-evaluation)
- **Simple Video Object Segmentation benchmark:** [https://github.com/hkchengrex/vos-benchmark](https://github.com/hkchengrex/vos-benchmark)

## 🎓 Citation

If this project is useful for your research, please consider citing **MOSXAV**:

```bibtex
@article{FSVOSXA,
    title={Few-Shot Video Object Segmentation in X-Ray Angiography Using Local Matching and Spatio-Temporal Consistency Loss},
    author={Xi, Lin and Ma, Yingliang and Zhuang, Xiahai},
    journal={arXiv preprint arXiv:2601.00988},
    year={2026}
}
```
