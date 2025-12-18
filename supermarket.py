import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
import io
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Multi-Language Business Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== MULTI-LANGUAGE SUPPORT =====================
LANGUAGES = {
    "English": {
        "title": "Business Intelligence Dashboard",
        "upload": "Upload Excel File",
        "upload_desc": "Upload an Excel file (.xlsx or .xls). The app will automatically detect date, numeric, and categorical columns and show analytical charts.",
        "drag_drop": "Drag and drop file here",
        "file_limit": "Limit 200MB per file • XLSX, XLS",
        "processing": "Processing data...",
        "data_preview": "Data Preview",
        "kpi_section": "Key Performance Indicators",
        "charts_section": "Analytical Charts",
        "total_records": "Total Records",
        "total_columns": "Total Columns",
        "date_columns": "Date Columns",
        "numeric_columns": "Numeric Columns",
        "data_types": "Data Types Overview",
        "missing_values": "Missing Values",
        "time_series": "Time Series Analysis",
        "distribution": "Distribution Analysis",
        "correlation": "Correlation Matrix",
        "category_analysis": "Category Analysis",
        "top_categories": "Top Categories",
        "download_data": "Download Processed Data",
        "select_date_col": "Select Date Column",
        "select_value_col": "Select Value Column",
        "select_category_col": "Select Category Column",
        "no_date_col": "No date column detected",
        "no_numeric_col": "No numeric column detected",
        "no_category_col": "No categorical column detected",
        "error": "Error",
        "success": "Success",
        "file_uploaded": "File uploaded successfully",
        "select_language": "Select Language",
        "reset": "Reset",
        "filter_data": "Filter Data",
        "apply_filter": "Apply Filter",
        "clear_filter": "Clear Filter",
        "data_summary": "Data Summary",
        "insights": "Insights",
        "trend": "Trend",
        "comparison": "Comparison",
        "forecast": "Forecast",
        "data_quality": "Data Quality Check",
        "statistics": "Statistics",
        "overview": "Overview",
        "export": "Export",
        "visualizations": "Visualizations"
    },
    "Indonesia": {
        "title": "Dasbor Bisnis Inteligensi",
        "upload": "Unggah File Excel",
        "upload_desc": "Unggah file Excel (.xlsx atau .xls). Aplikasi akan mendeteksi kolom tanggal, numerik, dan kategorikal secara otomatis dan menampilkan grafik analitis.",
        "drag_drop": "Seret dan lepas file di sini",
        "file_limit": "Batas 200MB per file • XLSX, XLS",
        "processing": "Memproses data...",
        "data_preview": "Pratinjau Data",
        "kpi_section": "Indikator Kinerja Utama",
        "charts_section": "Grafik Analitis",
        "total_records": "Total Data",
        "total_columns": "Total Kolom",
        "date_columns": "Kolom Tanggal",
        "numeric_columns": "Kolom Numerik",
        "data_types": "Ringkasan Tipe Data",
        "missing_values": "Nilai Kosong",
        "time_series": "Analisis Deret Waktu",
        "distribution": "Analisis Distribusi",
        "correlation": "Matriks Korelasi",
        "category_analysis": "Analisis Kategori",
        "top_categories": "Kategori Teratas",
        "download_data": "Unduh Data Hasil Olahan",
        "select_date_col": "Pilih Kolom Tanggal",
        "select_value_col": "Pilih Kolom Nilai",
        "select_category_col": "Pilih Kolom Kategori",
        "no_date_col": "Tidak ada kolom tanggal terdeteksi",
        "no_numeric_col": "Tidak ada kolom numerik terdeteksi",
        "no_category_col": "Tidak ada kolom kategorikal terdeteksi",
        "error": "Error",
        "success": "Berhasil",
        "file_uploaded": "File berhasil diunggah",
        "select_language": "Pilih Bahasa",
        "reset": "Reset",
        "filter_data": "Filter Data",
        "apply_filter": "Terapkan Filter",
        "clear_filter": "Hapus Filter",
        "data_summary": "Ringkasan Data",
        "insights": "Insights",
        "trend": "Tren",
        "comparison": "Perbandingan",
        "forecast": "Perkiraan",
        "data_quality": "Pemeriksaan Kualitas Data",
        "statistics": "Statistik",
        "overview": "Gambaran Umum",
        "export": "Ekspor",
        "visualizations": "Visualisasi"
    },
    "中文": {
        "title": "商业智能仪表板",
        "upload": "上传 Excel 文件",
        "upload_desc": "上传 Excel 文件（.xlsx 或 .xls）。应用将自动检测日期、数值和分类列，并显示分析图表。",
        "drag_drop": "拖放文件到此处",
        "file_limit": "每文件限制 200MB • XLSX, XLS",
        "processing": "处理数据中...",
        "data_preview": "数据预览",
        "kpi_section": "关键绩效指标",
        "charts_section": "分析图表",
        "total_records": "总记录数",
        "total_columns": "总列数",
        "date_columns": "日期列",
        "numeric_columns": "数值列",
        "data_types": "数据类型概览",
        "missing_values": "缺失值",
        "time_series": "时间序列分析",
        "distribution": "分布分析",
        "correlation": "相关矩阵",
        "category_analysis": "类别分析",
        "top_categories": "顶级类别",
        "download_data": "下载处理后的数据",
        "select_date_col": "选择日期列",
        "select_value_col": "选择数值列",
        "select_category_col": "选择分类列",
        "no_date_col": "未检测到日期列",
        "no_numeric_col": "未检测到数值列",
        "no_category_col": "未检测到分类列",
        "error": "错误",
        "success": "成功",
        "file_uploaded": "文件上传成功",
        "select_language": "选择语言",
        "reset": "重置",
        "filter_data": "筛选数据",
        "apply_filter": "应用筛选",
        "clear_filter": "清除筛选",
        "data_summary": "数据摘要",
        "insights": "洞察",
        "trend": "趋势",
        "comparison": "比较",
        "forecast": "预测",
        "data_quality": "数据质量检查",
        "statistics": "统计",
        "overview": "概览",
        "export": "导出",
        "visualizations": "可视化"
    }
}

# Initialize session state
if 'language' not in st.session_state:
    st.session_state.language = "English"
if 'df' not in st.session_state:
    st.session_state.df = None
if 'processed' not in st.session_state:
    st.session_state.processed = False
if 'file_name' not in st.session_state:
    st.session_state.file_name = None
if 'column_types' not in st.session_state:
    st.session_state.column_types = {}

# ===================== SIDEBAR =====================
with st.sidebar:
    st.title("🌍 Language Settings")
    selected_language = st.selectbox(
        LANGUAGES[st.session_state.language]["select_language"],
        options=list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.language)
    )
    
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        st.rerun()
    
    st.markdown("---")
    lang = LANGUAGES[st.session_state.language]
    
    # Display app info
    st.markdown("### 📱 App Information")
    st.markdown("**Version:** 2.2")
    st.markdown("**Last Updated:** Dec 2024")
    st.markdown("**Developer:** Business Analytics Team")
    
    st.markdown("---")
    
    # Quick tips
    st.markdown("### 💡 Quick Tips")
    st.markdown("1. Ensure Excel file is not open")
    st.markdown("2. Remove empty rows/columns")
    st.markdown("3. Use consistent date formats")
    st.markdown("4. Check for duplicate headers")

# ===================== HELPER FUNCTIONS =====================
def detect_column_types(df):
    """Detect column types with improved accuracy"""
    date_cols = []
    numeric_cols = []
    categorical_cols = []
    
    for col in df.columns:
        # Skip if all values are NaN
        if df[col].isna().all():
            categorical_cols.append(col)
            continue
            
        # Try to detect date columns
        try:
            # Sample first non-null value
            sample_val = df[col].dropna().iloc[0] if not df[col].dropna().empty else None
            
            # Try different date detection methods
            if isinstance(sample_val, (datetime, pd.Timestamp)):
                date_cols.append(col)
            elif isinstance(sample_val, str):
                # Try to parse string as date
                try:
                    pd.to_datetime(df[col], errors='raise')
                    date_cols.append(col)
                except:
                    # Check if it looks like a date string
                    if any(keyword in col.lower() for keyword in ['date', 'time', 'day', 'month', 'year', 'tanggal', 'waktu']):
                        try:
                            df[col] = pd.to_datetime(df[col], errors='coerce')
                            if df[col].notna().any():
                                date_cols.append(col)
                                continue
                        except:
                            pass
                    
                    # Default to categorical for string columns with few unique values
                    if df[col].nunique() < 50 or df[col].nunique() / len(df) < 0.1:
                        categorical_cols.append(col)
                    else:
                        categorical_cols.append(col)
            elif pd.api.types.is_numeric_dtype(df[col]):
                numeric_cols.append(col)
            elif pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == 'object':
                if df[col].nunique() < 50:
                    categorical_cols.append(col)
                else:
                    categorical_cols.append(col)
            else:
                categorical_cols.append(col)
        except:
            # If detection fails, try basic dtype check
            if pd.api.types.is_numeric_dtype(df[col]):
                numeric_cols.append(col)
            else:
                categorical_cols.append(col)
    
    return date_cols, numeric_cols, categorical_cols

def clean_dataframe(df):
    """Clean and prepare dataframe for analysis"""
    df_clean = df.copy()
    
    # Remove completely empty rows and columns
    df_clean = df_clean.dropna(how='all')
    df_clean = df_clean.loc[:, df_clean.notna().any()]
    
    # Trim whitespace from string columns
    for col in df_clean.select_dtypes(include=['object']).columns:
        df_clean[col] = df_clean[col].astype(str).str.strip()
    
    # Convert 'object' columns with few unique values to 'category'
    for col in df_clean.select_dtypes(include=['object']).columns:
        if df_clean[col].nunique() < 50:
            df_clean[col] = pd.Categorical(df_clean[col])
    
    return df_clean

def create_summary_statistics(df, numeric_cols, date_cols, categorical_cols):
    """Create comprehensive summary statistics"""
    summary = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': int(df.isnull().sum().sum()),
        'duplicate_rows': int(df.duplicated().sum()),
        'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024 / 1024,
        'date_columns': len(date_cols),
        'numeric_columns': len(numeric_cols),
        'categorical_columns': len(categorical_cols)
    }
    
    # Add numeric column statistics
    if numeric_cols:
        summary['numeric_stats'] = {}
        for col in numeric_cols[:5]:  # Limit to first 5 numeric columns
            summary['numeric_stats'][col] = {
                'mean': float(df[col].mean()),
                'median': float(df[col].median()),
                'std': float(df[col].std()),
                'min': float(df[col].min()),
                'max': float(df[col].max())
            }
    
    # Add date range if available
    if date_cols:
        for col in date_cols:
            try:
                summary['date_range'] = {
                    'min': df[col].min().strftime('%Y-%m-%d'),
                    'max': df[col].max().strftime('%Y-%m-%d')
                }
                break
            except:
                continue
    
    return summary

# ===================== MAIN APP =====================
st.title(f"📊 {lang['title']}")
st.markdown("---")

# File upload section
st.header(f"📁 {lang['upload']}")
col_upload1, col_upload2 = st.columns([2, 1])

with col_upload1:
    st.write(lang['upload_desc'])
    
    uploaded_file = st.file_uploader(
        lang['drag_drop'],
        type=['xlsx', 'xls'],
        help=lang['file_limit'],
        label_visibility="collapsed"
    )

with col_upload2:
    # Sample data download
    st.markdown("### 📋 Need Sample Data?")
    sample_data = {
        'Date': pd.date_range('2024-01-01', periods=30),
        'Sales': np.random.randint(1000, 5000, 30),
