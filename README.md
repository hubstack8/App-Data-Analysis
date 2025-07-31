# Computational Infrastructure Entities Usage Dashboard

This Streamlit dashboard provides visual analytics on computational infrastructure used in research, including hardware, software, cloud platforms, collaborations, and topic-wise trends.

## Dashboard Categories and Visualizations

### 1. Geographic Analysis
- GPU usage by country (hierarchical view)

### 2. Organizational Insights
- GPU usage by organization (hierarchical view)

### 3. Publication Metrics
- GPU vs CPU paper counts  
- Overall entities distribution

### 4. Cloud Platform Analytics
- Usage trends over the past 10 years  
- Top organizations and countries using cloud platforms  
- AWS and Google Cloud service usage breakdowns

### 5. Hardware Analysis
- Device memory configurations  
- GPU brand and category distribution  
- GPU generation trends  
- Hardware-memory co-occurrence  
- Common hardware setups and usage rankings

### 6. Collaboration Networks
- Collaboration graphs and pairings  
- International and organizational collaboration trends  
- Activity and diversity metrics

### 7. Software Ecosystem
- Software entity associations  
- Hardware-software heatmaps  
- Memory usage by software  
- Software evolution over time

### 8. Research Topics
- GPU usage by topic  
- Device counts per topic  
- Topic-based GPU usage trends

## Technologies Used
- Python, Streamlit, Plotly, HTML, CSS

## Run the App
Install dependencies and run:
```bash
pip install streamlit
streamlit run app.py

