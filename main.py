"""
TimeSeriesAnalyticsPlatform - Main Application Entry Point
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class TimeSeriesApp(App):
    """Main Kivy application class"""
    
    def build(self):
        """Build the application UI"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        label = Label(
            text='TimeSeriesAnalyticsPlatform v1.0.0',
            font_size='24sp'
        )
        layout.add_widget(label)
        
        info_label = Label(
            text='Statistical Time-Series Analytics Platform\n\nFeatures:\n- Data Import (TXT, CSV, JSON, XLSX)\n- Descriptive Statistics\n- Threshold Analysis\n- Rolling Windows\n- Sequence Analysis\n- Distribution Analysis\n- Anomaly Detection\n- Confidence Intervals\n- Interactive Visualizations\n- Comprehensive Reporting',
            font_size='14sp'
        )
        layout.add_widget(info_label)
        
        return layout


if __name__ == '__main__':
    TimeSeriesApp().run()
