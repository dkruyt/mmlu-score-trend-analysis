# MMLU Score Trend Analysis

This project analyzes the trend of MMLU (Massive Multitask Language Understanding) scores of AI models over time. It uses data from a CSV file containing information about various AI models, their release dates, MMLU scores, and other attributes.

![plot](mmlu_score_graph.png?raw=true "mmlu score")

## Dependencies

- Python 3.x
- pandas
- matplotlib
- scikit-learn

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/dkruyt/mmlu-score-trend-analysis.git
   ```

2. Install the required dependencies:
   ```
   pip install pandas matplotlib scikit-learn
   ```

## Usage

1. Prepare the data:
   - Ensure that you have a CSV file named `llm-mmlu.csv` in the same directory as the script.
   - The CSV file should contain the following columns: 'Model', 'Organization', 'Release Date', 'MMLU Score', 'Model Type'.

2. Run the script:
   ```
   python mmlu_score_trend_analysis.py
   ```

3. View the results:
   - The script will generate a graph named `mmlu_score_graph.png` in the same directory.
   - The graph will display the MMLU scores of AI models over time, with separate colors for open and closed models.
   - Linear regression trend lines will be plotted for both open and closed models to show the overall trend.

## Customization

- You can modify the script to use a different input CSV file by changing the file name in the following line:
  ```python
  updated_df = pd.read_csv('llm-mmlu.csv')
  ```

- You can adjust the graph's appearance by modifying the plotting code, such as changing colors, labels, titles, etc.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The data used in this project is sourced from the `llm-mmlu.csv` file.
- The analysis and visualization are performed using the pandas, matplotlib, and scikit-learn libraries.