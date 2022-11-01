import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(context="notebook")
sns.set_style("whitegrid", {"font.family":"sans-serif", "font.sans-serif":"Verdana"})

legend_labels = {"CHECK_CUDA_ERRORS_ABORT": "std::abort",
                 "CHECK_CUDA_ERRORS_ABORT_NO_PRINT": "std::abort (no print)",
                 "CHECK_CUDA_ERRORS_ASSERT": "assert",
                 "CHECK_CUDA_ERRORS_EXCEPTION": "std::runtime_error",
                 "CHECK_CUDA_ERRORS_EXCEPTION_NO_MESSAGE": "std::runtime_error (no message)"}
data = pd.read_csv("summary.csv")

cuda_error_implementations = data["Check CUDA errors implementation"].unique()

fig, axes = plt.subplots(2, sharex=True)
actors = []

for c in cuda_error_implementations:
    cuda_data = data[data["Check CUDA errors implementation"] == c]
    cuda_data = cuda_data.sort_values(by="Num arrays")

    a = axes[0].plot(cuda_data["Num arrays"], cuda_data["Wall clock time [s]"])[0]
    axes[1].plot(cuda_data["Num arrays"], cuda_data["Resident set size [mbyte]"], color=a.get_color())
    actors.append(a)

for a in axes:
    a.set_yscale("log")
    a.set_xscale("log")
    sns.despine(ax=a)

axes[1].set_xlabel("Number of arrays")
axes[0].set_ylabel("Wall clock time [s]")
axes[1].set_ylabel("Resident set size [mbyte]")


fig.legend(actors, [legend_labels[c] for c in cuda_error_implementations], 
           loc="lower center", ncol=2)
plt.tight_layout(pad=0, rect=[0.0, 0.05, 1.0, 1.0])
plt.show()