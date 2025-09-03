# NFL 4th Down Decision Analysis

## Project Overview

This comprehensive analysis examines NFL 4th down decision-making patterns from 1999-2024, revealing how teams' strategies have evolved with the analytics revolution. The project demonstrates advanced data analysis skills, statistical modeling, and business insight generation.

## Key Findings

- **108,866+ 4th down situations** analyzed across 25+ years
- **Analytics Revolution Impact**: Teams became significantly more aggressive post-2015
- **Field Position Optimization**: Clear patterns in decision-making by field position
- **Strategy Evolution**: Run vs pass preferences and QB sneak usage trends
- **Success Rate Analysis**: Conversion rates by distance and game situation

## Business Value

### For NFL Teams

- Optimize 4th down decision-making based on field position and game situation
- Identify successful strategies for different scenarios
- Track league-wide trends to stay competitive

### For Data Science Roles

- Complex data manipulation and cleaning
- Multi-dimensional analysis and visualization
- Time series analysis and trend identification
- Business insight generation from data

## Analysis Dimensions

1. **Overall Decision Patterns** - Go-for-it vs Kick frequencies and yearly trends
2. **Success Rate Analysis** - Conversion rates by distance and strategy
3. **Game Situation Context** - Time-based and field position patterns
4. **Strategic Evolution** - QB sneak usage and multi-dimensional analysis
5. **Yearly Trends** - How strategy has evolved over 25+ years
6. **Heatmap Analysis** - Multi-dimensional relationship visualization

## Technical Stack

- **Python** with Pandas for data manipulation
- **Plotly** for interactive visualizations
- **Statistical Analysis** for trend identification
- **Data Cleaning** and validation
- **Multi-dimensional Analysis** with heatmaps

## Project Structure

```
nfl-4th-down-decisions/
├── fourth_down_scripts.py          # Main analysis script
├── create_dashboard.py             # Dashboard generator
├── pbp_data/                       # NFL play-by-play data
│   ├── play_by_play_1999.parquet
│   ├── play_by_play_2000.parquet
│   └── ... (1999-2024)
├── *.html                          # Interactive visualizations
└── README.md                       # This file
```

## Getting Started

1. **Install Dependencies**

   ```bash
   pip install pandas plotly
   ```

2. **Download Data**

   The NFL play-by-play data files are not included in this repository due to size constraints. You can download them from:

   - [nflfastR data repository](https://github.com/nflverse/nflfastR-data)
   - Place the parquet files in a `pbp_data/` directory
   - Files needed: `play_by_play_YYYY.parquet` for years 1999-2024

3. **Run Analysis**

   ```bash
   python fourth_down_scripts.py
   ```

4. **Generate Dashboard and Presentation**

   ```bash
   python create_dashboard.py
   python create_presentation.py
   ```

5. **View Results**

   - Open `NFL_4th_Down_Analysis_Dashboard.html` for comprehensive analysis
   - Open `NFL_Analysis_Presentation.html` for executive summary
   - Explore interactive charts in the `charts/` directory

## Interactive Visualizations

The analysis generates 19 interactive visualizations covering:

### Core Analysis

- Overall Go vs Kick Decisions
- Yearly Decision Trends
- Success Rates by Distance

### Strategic Analysis

- Run vs Pass Strategy Comparison
- Time-Based Aggression Patterns
- Field Position Decision Making

### Advanced Heatmaps

- Field Position vs Distance Heatmap
- Time vs Field Position Heatmap
- Yearly Field Position Evolution

### Trend Analysis

- Success Rate Trends by Year
- Strategy Evolution Trends
- Time-Based Strategy Trends

_Note: Visualizations are generated when you run the analysis scripts_

## Methodology

### Data Sources

- NFL play-by-play data from 1999-2024
- 108,866+ 4th down situations analyzed
- Comprehensive field position and game situation data

### Analysis Techniques

- Time series analysis for trend identification
- Multi-dimensional heatmap analysis
- Success rate calculations with statistical significance
- QB sneak identification using player name matching

### Key Metrics

- **Go-for-it Rate**: Percentage of 4th downs where teams attempt to convert
- **Success Rate**: Percentage of go-for-it attempts that result in first downs
- **Field Position Categories**: 10 zones from own goal line to opponent goal line
- **Time Categories**: 5 game situation buckets from first half to final 5 minutes

## Portfolio Value

This project demonstrates:

- **Data Analysis Skills**: Complex data manipulation and cleaning
- **Statistical Analysis**: Trend identification and success rate calculations
- **Visualization**: Interactive charts and heatmaps
- **Business Insight**: Actionable recommendations for NFL teams
- **Technical Proficiency**: Python, Pandas, Plotly, and data science best practices

## Contact

For questions about this analysis or to discuss data science opportunities, please reach out through your preferred contact method.

---

_This analysis showcases advanced data science skills and business insight generation capabilities suitable for data analyst, data scientist, or sports analytics roles._
