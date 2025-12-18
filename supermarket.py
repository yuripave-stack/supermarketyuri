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
        'Profit': np.random.randint(200, 1000, 30),
        'Quantity': np.random.randint(10, 100, 30),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Food'], 30),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 30),
        'Customer_Rating': np.random.uniform(3.0, 5.0, 30).round(1)
    }
    sample_df = pd.DataFrame(sample_data)
    
    csv = sample_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Sample CSV",
        data=csv,
        file_name="sample_business_data.csv",
        mime="text/csv"
    )

# Process uploaded file
if uploaded_file is not None:
    try:
        with st.spinner(f"{lang['processing']}..."):
            # Determine engine based on file extension
            if uploaded_file.name.endswith('.xls'):
                df = pd.read_excel(uploaded_file, engine='xlrd')
            else:
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            
            # Clean and process data
            df = clean_dataframe(df)
            
            # Detect column types
            date_cols, numeric_cols, categorical_cols = detect_column_types(df)
            
            # Store in session state
            st.session_state.df = df
            st.session_state.processed = True
            st.session_state.file_name = uploaded_file.name
            st.session_state.column_types = {
                'date': date_cols,
                'numeric': numeric_cols,
                'categorical': categorical_cols
            }
            
            st.success(f"✅ {lang['file_uploaded']}")
            
            # Show quick file info
            with st.expander("📄 File Information", expanded=True):
                col_info1, col_info2, col_info3 = st.columns(3)
                with col_info1:
                    st.metric("File Name", uploaded_file.name)
                with col_info2:
                    st.metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")
                with col_info3:
                    st.metric("Rows x Columns", f"{len(df)} × {len(df.columns)}")
                    
    except Exception as e:
        st.error(f"❌ {lang['error']}: {str(e)}")
        st.info("""
        **💡 Troubleshooting Tips:**
        1. Make sure the Excel file is not open in another program
        2. Check if the file is corrupted
        3. Try saving as .xlsx format
        4. Ensure you have openpyxl installed: `pip install openpyxl`
        """)

# Display dashboard if data is available
if st.session_state.processed and st.session_state.df is not None:
    df = st.session_state.df
    date_cols = st.session_state.column_types.get('date', [])
    numeric_cols = st.session_state.column_types.get('numeric', [])
    categorical_cols = st.session_state.column_types.get('categorical', [])
    
    # ===================== SIDEBAR FILTERS =====================
    with st.sidebar:
        st.markdown("---")
        st.header(f"🔧 {lang['filter_data']}")
        
        # Row limit slider
        row_limit = st.slider("Rows to display", 5, 1000, 100, 5)
        
        # Column selection
        if numeric_cols:
            selected_numeric = st.multiselect(
                f"📈 {lang['select_value_col']}",
                numeric_cols,
                default=numeric_cols[:min(3, len(numeric_cols))]
            )
        else:
            selected_numeric = []
            
        if date_cols:
            selected_date = st.selectbox(
                f"📅 {lang['select_date_col']}",
                date_cols
            )
        else:
            selected_date = None
            
        if categorical_cols:
            selected_category = st.selectbox(
                f"🏷️ {lang['select_category_col']}",
                categorical_cols
            )
        else:
            selected_category = None
        
        # Additional filters
        st.markdown("---")
        st.subheader("Advanced Filters")
        
        # Missing values filter
        show_missing = st.checkbox("Show rows with missing values only", False)
        
        # Date range filter (if date column exists)
        if selected_date and selected_date in df.columns:
            try:
                min_date = df[selected_date].min()
                max_date = df[selected_date].max()
                date_range = st.date_input(
                    "Date Range",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date
                )
                if len(date_range) == 2:
                    mask = (df[selected_date] >= pd.Timestamp(date_range[0])) & \
                           (df[selected_date] <= pd.Timestamp(date_range[1]))
                    df = df[mask]
            except:
                pass
        
        # Reset button in sidebar
        if st.button(f"🔄 {lang['reset']} Filters", use_container_width=True, type="secondary"):
            # Only reset filters, not the data
            st.rerun()
    
    # ===================== DATA PREVIEW =====================
    st.header(f"🔍 {lang['data_preview']}")
    
    # Apply missing values filter
    preview_df = df.copy()
    if show_missing:
        preview_df = preview_df[preview_df.isnull().any(axis=1)]
    
    # Display data preview with tabs
    tab_preview, tab_structure, tab_quality = st.tabs(["📋 Data Preview", "🏗️ Data Structure", "✅ Data Quality"])
    
    with tab_preview:
        st.dataframe(preview_df.head(row_limit), use_container_width=True)
        
        # Show data summary
        if len(preview_df) == 0 and show_missing:
            st.success("🎉 No missing values found in the dataset!")
        else:
            st.caption(f"Showing {min(row_limit, len(preview_df))} of {len(preview_df)} rows")
    
    with tab_structure:
        col_struct1, col_struct2 = st.columns(2)
        
        with col_struct1:
            st.subheader("Column Types")
            type_data = {
                'Type': ['Date', 'Numeric', 'Categorical', 'Other'],
                'Count': [len(date_cols), len(numeric_cols), len(categorical_cols), 
                         len(df.columns) - len(date_cols) - len(numeric_cols) - len(categorical_cols)]
            }
            type_df = pd.DataFrame(type_data)
            st.dataframe(type_df, use_container_width=True)
            
            # Column list
            st.subheader("All Columns")
            for i, col in enumerate(df.columns, 1):
                col_type = "📅 Date" if col in date_cols else \
                          "🔢 Numeric" if col in numeric_cols else \
                          "🏷️ Categorical" if col in categorical_cols else "📝 Other"
                st.write(f"{i}. **{col}** - {col_type}")
        
        with col_struct2:
            st.subheader("Data Types")
            dtype_counts = df.dtypes.astype(str).value_counts().resetindex()
            dtype_counts.columns = ['Data Type', 'Count']
            
            if not dtype_counts.empty:
                fig_dtype = px.pie(
                    dtype_counts, 
                    values='Count', 
                    names='Data Type',
                    title="Data Type Distribution",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig_dtype, use_container_width=True)
    
    with tab_quality:
        st.subheader("📊 Data Quality Report")
        
        # Calculate quality metrics
        total_cells = len(df) * len(df.columns)
        missing_cells = df.isnull().sum().sum()
        missing_percentage = (missing_cells / total_cells * 100) if total_cells > 0 else 0
        
        duplicate_rows = df.duplicated().sum()
        duplicate_percentage = (duplicate_rows / len(df) * 100) if len(df) > 0 else 0
        
        # Quality metrics display
        col_qual1, col_qual2, col_qual3 = st.columns(3)
        
        with col_qual1:
            st.metric("Completeness", f"{(100 - missing_percentage):.1f}%", 
                     f"-{missing_percentage:.1f}% missing")
        
        with col_qual2:
            st.metric("Uniqueness", f"{(100 - duplicate_percentage):.1f}%",
                     f"-{duplicate_percentage:.1f}% duplicates")
        
        with col_qual3:
            # Check for inconsistent data types
            inconsistent_cols = 0
            for col in df.columns:
                if df[col].apply(type).nunique() > 1:
                    inconsistent_cols += 1
            consistency = ((len(df.columns) - inconsistent_cols) / len(df.columns) * 100) if len(df.columns) > 0 else 100
            st.metric("Consistency", f"{consistency:.1f}%")
        
        # Missing values by column
        st.subheader("Missing Values by Column")
        missing_by_col = df.isnull().sum().reset_index()
        missing_by_col.columns = ['Column', 'Missing Count']
        missing_by_col = missing_by_col[missing_by_col['Missing Count'] > 0]
        
        if not missing_by_col.empty:
            fig_missing = px.bar(
                missing_by_col,
                x='Column',
                y='Missing Count',
                title="Missing Values per Column",
                color='Missing Count',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_missing, use_container_width=True)
        else:
            st.success("✅ No missing values found in any column!")
    
    # ===================== KPI DASHBOARD =====================
    st.header(f"📈 {lang['kpi_section']}")
    
    # Create summary statistics
    summary = create_summary_statistics(df, numeric_cols, date_cols, categorical_cols)
    
    # KPI Metrics Row 1
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        st.metric(
            lang['total_records'],
            f"{summary['total_rows']:,}",
            help="Total number of rows in the dataset"
        )
    
    with kpi_col2:
        st.metric(
            lang['total_columns'],
            summary['total_columns'],
            help="Total number of columns in the dataset"
        )
    
    with kpi_col3:
        st.metric(
            lang['date_columns'],
            summary['date_columns'],
            help="Number of columns detected as dates"
        )
    
    with kpi_col4:
        st.metric(
            lang['numeric_columns'],
            summary['numeric_columns'],
            help="Number of columns detected as numeric"
        )
    
    # KPI Metrics Row 2
    kpi_col5, kpi_col6, kpi_col7, kpi_col8 = st.columns(4)
    
    with kpi_col5:
        st.metric(
            lang['missing_values'],
            f"{summary['missing_values']:,}",
            delta=f"{(summary['missing_values']/summary['total_rows']*100):.1f}%" if summary['total_rows'] > 0 else "0%",
            delta_color="inverse",
            help="Total number of missing values"
        )
    
    with kpi_col6:
        st.metric(
            "Duplicate Rows",
            summary['duplicate_rows'],
            delta=f"{(summary['duplicate_rows']/summary['total_rows']*100):.1f}%" if summary['total_rows'] > 0 else "0%",
            delta_color="inverse",
            help="Number of duplicate rows"
        )
    
    with kpi_col7:
        st.metric(
            "Memory Usage",
            f"{summary['memory_usage_mb']:.1f} MB",
            help="Total memory used by the dataset"
        )
    
    with kpi_col8:
        if numeric_cols and 'numeric_stats' in summary:
            avg_of_avgs = np.mean([stats['mean'] for stats in summary['numeric_stats'].values()])
            st.metric(
                "Avg Numeric Value",
                f"{avg_of_avgs:,.2f}",
                help="Average of all numeric column means"
            )
        else:
            st.metric("Avg Numeric Value", "N/A")
    
    st.markdown("---")
    
    # ===================== VISUALIZATIONS =====================
    st.header(f"📊 {lang['visualizations']}")
    
    # Create tabs for different visualizations
    viz_tabs = st.tabs([
        "📈 Time Series", 
        "📊 Distributions", 
        "🔗 Correlations", 
        "🏷️ Categories",
        "📋 Summary"
    ])
    
    with viz_tabs[0]:  # Time Series Tab
        if selected_date and selected_numeric:
            st.subheader(f"{lang['time_series']}")
            
            # Time series line chart
            ts_data = df.groupby(selected_date)[selected_numeric].sum().reset_index()
            
            fig_ts = go.Figure()
            for col in selected_numeric:
                fig_ts.add_trace(go.Scatter(
                    x=ts_data[selected_date],
                    y=ts_data[col],
                    mode='lines+markers',
                    name=col,
                    line=dict(width=2)
                ))
            
            fig_ts.update_layout(
                title=f"{lang['trend']} Analysis",
                xaxis_title=selected_date,
                yaxis_title="Value",
                hovermode='x unified',
                height=500,
                showlegend=True
            )
            
            st.plotly_chart(fig_ts, use_container_width=True)
            
            # Time series statistics
            col_ts1, col_ts2, col_ts3 = st.columns(3)
            with col_ts1:
                if len(ts_data) > 1:
                    start_val = ts_data[selected_numeric[0]].iloc[0]
                    end_val = ts_data[selected_numeric[0]].iloc[-1]
                    growth = ((end_val - start_val) / start_val * 100) if start_val != 0 else 0
                    st.metric(f"Growth ({selected_numeric[0]})", f"{growth:+.1f}%")
            
            with col_ts2:
                if len(ts_data) > 0:
                    total_val = ts_data[selected_numeric[0]].sum()
                    st.metric(f"Total ({selected_numeric[0]})", f"{total_val:,.0f}")
            
            with col_ts3:
                if len(ts_data) > 0:
                    avg_val = ts_data[selected_numeric[0]].mean()
                    st.metric(f"Average ({selected_numeric[0]})", f"{avg_val:,.2f}")
        else:
            st.info("Select a date column and numeric columns for time series analysis")
    
    with viz_tabs[1]:  # Distributions Tab
        if selected_numeric:
            st.subheader(f"{lang['distribution']}")
            
            selected_var = st.selectbox(
                "Select variable for distribution analysis:",
                selected_numeric,
                key="dist_var_select"
            )
            
            col_dist1, col_dist2 = st.columns(2)
            
            with col_dist1:
                # Histogram with density
                fig_hist = px.histogram(
                    df,
                    x=selected_var,
                    nbins=30,
                    title=f"Histogram of {selected_var}",
                    marginal="box",
                    color_discrete_sequence=['#636EFA'],
                    opacity=0.7
                )
                fig_hist.update_layout(height=400)
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col_dist2:
                # Box plot
                fig_box = px.box(
                    df,
                    y=selected_var,
                    title=f"Box Plot of {selected_var}",
                    color_discrete_sequence=['#00CC96']
                )
                fig_box.update_layout(height=400)
