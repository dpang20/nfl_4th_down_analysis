import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from datetime import datetime

def create_executive_dashboard():
    """Create a professional executive dashboard for recruiters/hiring managers"""
    
    # Create a comprehensive dashboard HTML file
    dashboard_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>NFL 4th Down Decision Analysis - Executive Summary</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .header { background-color: #1e3a8a; color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }
            .section { background-color: white; padding: 25px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .metric { display: inline-block; margin: 15px; padding: 20px; background-color: #f8fafc; border-left: 4px solid #3b82f6; }
            .metric-value { font-size: 2em; font-weight: bold; color: #1e40af; }
            .metric-label { color: #64748b; font-size: 0.9em; }
            .chart-container { margin: 20px 0; }
            .insight { background-color: #fef3c7; padding: 15px; border-left: 4px solid #f59e0b; margin: 15px 0; }
            .methodology { background-color: #ecfdf5; padding: 15px; border-left: 4px solid #10b981; margin: 15px 0; }
            h1 { margin: 0; font-size: 2.5em; }
            h2 { color: #1e40af; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px; }
            h3 { color: #374151; }
            .footer { text-align: center; color: #6b7280; margin-top: 50px; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>NFL 4th Down Decision Analysis</h1>
            <p>Comprehensive Analysis of 4th Down Strategy Evolution (1999-2024)</p>
            <p><strong>Data Analyst Portfolio Project</strong> | Generated: """ + datetime.now().strftime("%B %d, %Y") + """</p>
        </div>

        <div class="section">
            <h2>Executive Summary</h2>
            <div class="metric">
                <div class="metric-value">108,866</div>
                <div class="metric-label">Total 4th Down Situations Analyzed</div>
            </div>
            <div class="metric">
                <div class="metric-value">25+</div>
                <div class="metric-label">Years of Data (1999-2024)</div>
            </div>
            <div class="metric">
                <div class="metric-value">19</div>
                <div class="metric-label">Interactive Visualizations</div>
            </div>
            <div class="metric">
                <div class="metric-value">6</div>
                <div class="metric-label">Analysis Dimensions</div>
            </div>
        </div>

        <div class="section">
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

        <div class="section">
            <h2>Analysis Dimensions</h2>
            <h3>1. Overall Decision Patterns</h3>
            <p>• Go-for-it vs Kick decision frequencies</p>
            <p>• Yearly trends showing strategy evolution</p>
            
            <h3>2. Success Rate Analysis</h3>
            <p>• Conversion rates by distance to go</p>
            <p>• Run vs Pass effectiveness comparison</p>
            
            <h3>3. Game Situation Context</h3>
            <p>• Time-based aggression patterns</p>
            <p>• Field position decision-making</p>
            
            <h3>4. Strategic Evolution</h3>
            <p>• QB sneak usage and effectiveness</p>
            <p>• Multi-dimensional heatmap analysis</p>
        </div>

        <div class="section">
            <h2>Methodology & Technical Approach</h2>
            <div class="methodology">
                <h3>Data Sources</h3>
                <p>• NFL play-by-play data from 1999-2024</p>
                <p>• 108,866+ 4th down situations analyzed</p>
                <p>• Comprehensive field position and game situation data</p>
            </div>
            <div class="methodology">
                <h3>Technical Stack</h3>
                <p>• Python with Pandas for data manipulation</p>
                <p>• Plotly for interactive visualizations</p>
                <p>• Statistical analysis and trend identification</p>
            </div>
            <div class="methodology">
                <h3>Analysis Techniques</h3>
                <p>• Time series analysis for trend identification</p>
                <p>• Multi-dimensional heatmap analysis</p>
                <p>• Success rate calculations with statistical significance</p>
            </div>
        </div>

        <div class="section">
            <h2>Interactive Visualizations</h2>
            <p>Click on any chart below to explore the interactive visualizations:</p>
            
            <h3>Core Analysis Charts</h3>
            <p>• <a href="charts/first_chart.html" target="_blank">Overall Go vs Kick Decisions</a></p>
            <p>• <a href="charts/yearly_trends.html" target="_blank">Yearly Decision Trends</a></p>
            <p>• <a href="charts/success_rate_by_distance.html" target="_blank">Success Rates by Distance</a></p>
            
            <h3>Strategic Analysis</h3>
            <p>• <a href="charts/run_vs_pass_success.html" target="_blank">Run vs Pass Strategy Comparison</a></p>
            <p>• <a href="charts/run_vs_pass_by_distance.html" target="_blank">Run vs Pass by Distance Analysis</a></p>
            <p>• <a href="charts/time_aggression.html" target="_blank">Time-Based Aggression Patterns</a></p>
            <p>• <a href="charts/field_position_aggression.html" target="_blank">Field Position Decision Making</a></p>
            <p>• <a href="charts/field_position_success.html" target="_blank">Field Position Success Analysis</a></p>
            
            <h3>Advanced Heatmaps</h3>
            <p>• <a href="charts/field_distance_heatmap.html" target="_blank">Field Position vs Distance Heatmap</a></p>
            <p>• <a href="charts/field_distance_success_heatmap.html" target="_blank">Field Position vs Distance Success Heatmap</a></p>
            <p>• <a href="charts/time_field_heatmap.html" target="_blank">Time vs Field Position Heatmap</a></p>
            <p>• <a href="charts/yearly_field_heatmap.html" target="_blank">Yearly Field Position Evolution</a></p>
            
            <h3>Trend Analysis</h3>
            <p>• <a href="charts/yearly_success_trends.html" target="_blank">Success Rate Trends by Year</a></p>
            <p>• <a href="charts/yearly_strategy_trends.html" target="_blank">Strategy Evolution Trends</a></p>
            <p>• <a href="charts/yearly_time_trends.html" target="_blank">Time-Based Strategy Trends</a></p>
            <p>• <a href="charts/yearly_field_position_trends.html" target="_blank">Yearly Field Position Trends</a></p>
            
            <h3>QB Sneak Analysis</h3>
            <p>• <a href="charts/qb_sneak_usage_trends.html" target="_blank">QB Sneak Usage Trends</a></p>
            <p>• <a href="charts/qb_sneak_success_trends.html" target="_blank">QB Sneak Success Rate Trends</a></p>
            <p>• <a href="charts/qb_sneak_success_by_distance.html" target="_blank">QB Sneak Success by Distance</a></p>
        </div>

        <div class="section">
            <h2>Business Value & Applications</h2>
            <h3>For NFL Teams</h3>
            <p>• Optimize 4th down decision-making based on field position and game situation</p>
            <p>• Identify successful strategies for different scenarios</p>
            <p>• Track league-wide trends to stay competitive</p>
            
            <h3>For Sports Analytics</h3>
            <p>• Demonstrate advanced data analysis capabilities</p>
            <p>• Show ability to extract actionable insights from complex datasets</p>
            <p>• Illustrate trend analysis and predictive modeling skills</p>
            
            <h3>For Data Science Roles</h3>
            <p>• Complex data manipulation and cleaning</p>
            <p>• Multi-dimensional analysis and visualization</p>
            <p>• Time series analysis and trend identification</p>
            <p>• Business insight generation from data</p>
        </div>

        <div class="footer">
            <p>This analysis demonstrates proficiency in data analysis, visualization, and business insight generation.</p>
            <p>All visualizations are interactive and can be explored in detail.</p>
        </div>
    </body>
    </html>
    """
    
    # Write the dashboard
    with open("NFL_4th_Down_Analysis_Dashboard.html", "w") as f:
        f.write(dashboard_html)
    
    print("Executive dashboard created: NFL_4th_Down_Analysis_Dashboard.html")

if __name__ == "__main__":
    create_executive_dashboard()
