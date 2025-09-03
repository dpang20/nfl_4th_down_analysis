import os
from datetime import datetime

def create_presentation_summary():
    """Create a concise presentation summary for recruiters"""
    
    presentation_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>NFL 4th Down Analysis - Presentation Summary</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .container { max-width: 1200px; margin: 0 auto; background: white; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); overflow: hidden; }
            .header { background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 40px; text-align: center; }
            .slide { padding: 40px; border-bottom: 1px solid #e5e7eb; }
            .slide:last-child { border-bottom: none; }
            h1 { font-size: 3em; margin: 0; font-weight: 300; }
            h2 { color: #1e40af; font-size: 2em; margin-bottom: 20px; }
            h3 { color: #374151; font-size: 1.5em; margin-bottom: 15px; }
            .metric-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }
            .metric { background: #f8fafc; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #3b82f6; }
            .metric-value { font-size: 2.5em; font-weight: bold; color: #1e40af; margin-bottom: 5px; }
            .metric-label { color: #64748b; font-size: 0.9em; }
            .insight { background: #fef3c7; padding: 20px; border-radius: 10px; border-left: 4px solid #f59e0b; margin: 15px 0; }
            .skill { background: #ecfdf5; padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #10b981; }
            .chart-link { display: inline-block; background: #3b82f6; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 5px; }
            .chart-link:hover { background: #1e40af; }
            ul { list-style: none; padding: 0; }
            li { padding: 8px 0; border-bottom: 1px solid #f3f4f6; }
            li:before { content: "✓ "; color: #10b981; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>NFL 4th Down Decision Analysis</h1>
                <p style="font-size: 1.2em; margin: 10px 0;">Data Science Portfolio Project</p>
                <p>Comprehensive Analysis of 4th Down Strategy Evolution (1999-2024)</p>
            </div>

            <div class="slide">
                <h2>Project Overview</h2>
                <p style="font-size: 1.1em; line-height: 1.6;">This project analyzes NFL 4th down decision-making patterns across 25+ years, revealing how teams' strategies have evolved with the analytics revolution. It demonstrates advanced data analysis skills, statistical modeling, and business insight generation.</p>
                
                <div class="metric-grid">
                    <div class="metric">
                        <div class="metric-value">108,866</div>
                        <div class="metric-label">4th Down Situations</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">25+</div>
                        <div class="metric-label">Years of Data</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">19</div>
                        <div class="metric-label">Interactive Charts</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">6</div>
                        <div class="metric-label">Analysis Dimensions</div>
                    </div>
                </div>
            </div>

            <div class="slide">
                <h2>Key Business Insights</h2>
                
                <div class="insight">
                    <h3>Analytics Revolution Impact</h3>
                    <p>Teams have become significantly more aggressive on 4th downs since 2015, reflecting the influence of advanced analytics on NFL decision-making.</p>
                </div>
                
                <div class="insight">
                    <h3>Field Position Optimization</h3>
                    <p>Success rates vary dramatically by field position and distance, revealing clear optimization opportunities for teams.</p>
                </div>
                
                <div class="insight">
                    <h3>Strategy Evolution</h3>
                    <p>Play-calling strategies have evolved over time, with teams adapting to rule changes and analytical insights.</p>
                </div>
            </div>

            <div class="slide">
                <h2>Technical Skills Demonstrated</h2>
                
                <div class="skill">
                    <strong>Data Manipulation:</strong> Complex data cleaning and transformation using Pandas
                </div>
                <div class="skill">
                    <strong>Statistical Analysis:</strong> Success rate calculations and trend identification
                </div>
                <div class="skill">
                    <strong>Visualization:</strong> Interactive charts and multi-dimensional heatmaps
                </div>
                <div class="skill">
                    <strong>Business Intelligence:</strong> Converting data into actionable insights
                </div>
                <div class="skill">
                    <strong>Time Series Analysis:</strong> Identifying trends and patterns over 25+ years
                </div>
                <div class="skill">
                    <strong>Multi-dimensional Analysis:</strong> Field position, time, distance, and strategy analysis
                </div>
            </div>

            <div class="slide">
                <h2>Analysis Dimensions</h2>
                
                <ul>
                    <li><strong>Overall Decision Patterns:</strong> Go-for-it vs Kick frequencies and yearly trends</li>
                    <li><strong>Success Rate Analysis:</strong> Conversion rates by distance and strategy</li>
                    <li><strong>Game Situation Context:</strong> Time-based and field position patterns</li>
                    <li><strong>Strategic Evolution:</strong> QB sneak usage and multi-dimensional analysis</li>
                    <li><strong>Yearly Trends:</strong> How strategy has evolved over 25+ years</li>
                    <li><strong>Heatmap Analysis:</strong> Multi-dimensional relationship visualization</li>
                </ul>
            </div>

            <div class="slide">
                <h2>Interactive Visualizations</h2>
                <p>Click any chart below to explore the interactive visualizations:</p>
                
                <h3>Core Analysis</h3>
                <a href="charts/first_chart.html" target="_blank" class="chart-link">Overall Decisions</a>
                <a href="charts/yearly_trends.html" target="_blank" class="chart-link">Yearly Trends</a>
                <a href="charts/success_rate_by_distance.html" target="_blank" class="chart-link">Success Rates</a>
                
                <h3>Strategic Analysis</h3>
                <a href="charts/run_vs_pass_success.html" target="_blank" class="chart-link">Run vs Pass</a>
                <a href="charts/run_vs_pass_by_distance.html" target="_blank" class="chart-link">Run vs Pass by Distance</a>
                <a href="charts/time_aggression.html" target="_blank" class="chart-link">Time Patterns</a>
                <a href="charts/field_position_aggression.html" target="_blank" class="chart-link">Field Position</a>
                <a href="charts/field_position_success.html" target="_blank" class="chart-link">Field Position Success</a>
                
                <h3>Advanced Heatmaps</h3>
                <a href="charts/field_distance_heatmap.html" target="_blank" class="chart-link">Field vs Distance</a>
                <a href="charts/field_distance_success_heatmap.html" target="_blank" class="chart-link">Field vs Distance Success</a>
                <a href="charts/time_field_heatmap.html" target="_blank" class="chart-link">Time vs Field</a>
                <a href="charts/yearly_field_heatmap.html" target="_blank" class="chart-link">Yearly Evolution</a>
                
                <h3>Trend Analysis</h3>
                <a href="charts/yearly_success_trends.html" target="_blank" class="chart-link">Success Trends</a>
                <a href="charts/yearly_strategy_trends.html" target="_blank" class="chart-link">Strategy Trends</a>
                <a href="charts/yearly_time_trends.html" target="_blank" class="chart-link">Time Trends</a>
                <a href="charts/yearly_field_position_trends.html" target="_blank" class="chart-link">Field Position Trends</a>
                
                <h3>QB Sneak Analysis</h3>
                <a href="charts/qb_sneak_usage_trends.html" target="_blank" class="chart-link">QB Sneak Usage</a>
                <a href="charts/qb_sneak_success_trends.html" target="_blank" class="chart-link">QB Sneak Success</a>
                <a href="charts/qb_sneak_success_by_distance.html" target="_blank" class="chart-link">QB Sneak by Distance</a>
            </div>

            <div class="slide">
                <h2>Business Value</h2>
                
                <h3>For NFL Teams</h3>
                <ul>
                    <li>Optimize 4th down decision-making based on field position and game situation</li>
                    <li>Identify successful strategies for different scenarios</li>
                    <li>Track league-wide trends to stay competitive</li>
                </ul>
                
                <h3>For Data Science Roles</h3>
                <ul>
                    <li>Complex data manipulation and cleaning</li>
                    <li>Multi-dimensional analysis and visualization</li>
                    <li>Time series analysis and trend identification</li>
                    <li>Business insight generation from data</li>
                </ul>
            </div>

            <div class="slide">
                <h2>Next Steps</h2>
                <p style="font-size: 1.1em; line-height: 1.6;">This analysis demonstrates proficiency in data analysis, visualization, and business insight generation. The project showcases skills relevant for data analyst, data scientist, or sports analytics roles.</p>
                
                <div style="text-align: center; margin-top: 30px;">
                    <p style="font-size: 1.2em; color: #1e40af;"><strong>Ready to discuss how these skills can benefit your organization</strong></p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("NFL_Analysis_Presentation.html", "w") as f:
        f.write(presentation_html)
    
    print("Presentation summary created: NFL_Analysis_Presentation.html")

if __name__ == "__main__":
    create_presentation_summary()
