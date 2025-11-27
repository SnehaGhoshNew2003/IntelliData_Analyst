# app/agents/visualization_agent.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO


class VisualizationAgent:

    def recommend_visualizations(self, df: pd.DataFrame, analysis_report):
        specs = []

        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

        important_numeric = analysis_report.get("important_numeric", numeric_cols)
        important_cat = analysis_report.get("important_categorical", categorical_cols)

        for col in important_numeric:
            specs.append({"type": "histogram", "column": col})

        for col in important_numeric:
            specs.append({"type": "boxplot", "column": col})

        if len(important_numeric) > 0:
            specs.append({"type": "lineplot", "columns": important_numeric})

        for col in important_cat:
            specs.append({"type": "barchart", "column": col})

        if len(important_numeric) >= 2:
            for i in range(len(important_numeric) - 1):
                specs.append({
                    "type": "scatter",
                    "x": important_numeric[i],
                    "y": important_numeric[i + 1]
                })

        if len(important_numeric) >= 2:
            specs.append({"type": "heatmap", "columns": important_numeric})

        return specs


    def generate_visualizations(self, df: pd.DataFrame, specs):
        images = []

        for spec in specs:
            try:
                # Always create a clean figure
                fig, ax = plt.subplots(figsize=(6, 4))
                type_ = spec["type"]

                # HISTOGRAM
                if type_ == "histogram":
                    col = spec["column"]
                    if df[col].dropna().empty:
                        plt.close(fig)
                        continue
                    ax.hist(df[col].dropna(), bins=30)
                    ax.set_title(f"Histogram: {col}")

                # BOXPLOT
                elif type_ == "boxplot":
                    col = spec["column"]
                    sns.boxplot(x=df[col], ax=ax)
                    ax.set_title(f"Box Plot: {col}")

                # LINEPLOT
                elif type_ == "lineplot":
                    cols = spec["columns"]
                    ax.plot(df[cols])
                    ax.set_title("Line Plot of Numeric Columns")
                    ax.legend(cols)

                # BARCHART
                elif type_ == "barchart":
                    col = spec["column"]
                    df[col].value_counts().plot(kind="bar", ax=ax)
                    ax.set_title(f"Bar Chart: {col}")

                # SCATTER
                elif type_ == "scatter":
                    x = spec["x"]
                    y = spec["y"]
                    ax.scatter(df[x], df[y])
                    ax.set_xlabel(x)
                    ax.set_ylabel(y)
                    ax.set_title(f"Scatter Plot: {x} vs {y}")

                # HEATMAP
                elif type_ == "heatmap":
                    cols = spec["columns"]
                    corr = df[cols].corr()
                    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                    ax.set_title("Correlation Heatmap")

                # Convert to Base64
                buffer = BytesIO()
                fig.savefig(buffer, format="png", bbox_inches="tight")
                buffer.seek(0)
                img_b64 = base64.b64encode(buffer.read()).decode("utf-8")
                plt.close(fig)

                images.append(img_b64)

            except Exception as e:
                print(f"[Visualization Error] {spec} → {e}")

        return images
