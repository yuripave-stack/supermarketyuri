import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
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
        "forecast": "Forecast"
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
        "forecast": "Perkiraan"
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
        "forecast": "预测"
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
    st.markdown("**Version:** 2.0")
    st.markdown("**Last Updated:** Dec 2024")
    st.markdown("**Developer:** Business Analytics Team")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.markdown("1. Ensure Excel file is not open")
    st.markdown("2. Remove empty rows/columns")
    st.markdown("3. Use consistent date formats")

# ===================== MAIN APP =====================
st.title(f"📊 {lang['title']}")
st.markdown("---")

# File upload section
st.header(f"📁 {lang['upload']}")
st.write(lang['upload_desc'])

uploaded_file = st.file_uploader(
    lang['drag_drop'],
    type=['xlsx', 'xls'],
    help=lang['file_limit']
)

# Process uploaded file
if uploaded_file is not None:
    try:
        with st.spinner(lang['processing']):
            # Read Excel file
            if uploaded_file.name.endswith('.xls'):
                df = pd.read_excel(uploaded_file, engine='xlrd')
            else:
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            
            # Store in session state
            st.session_state.df = df
            st.session_state.processed = True
            st.session_state.file_name = uploaded_file.name
            
            st.success(f"✅ {lang['file_uploaded']}: {uploaded_file.name}")
            
    except Exception as e:
        st.error(f"❌ {lang['error']}: {str(e)}")
        st.info("💡 Make sure you have openpyxl installed: `pip install openpyxl`")

# Display dashboard if data is available
if st.session_state.processed and st.session_state.df is not None:
    df = st.session_state.df
    
    # Detect column types
    date_cols = []
    numeric_cols = []
    categorical_cols = []
    
    for col in df.columns:
        # Try to detect date columns
        try:
            df[col] = pd.to_datetime(df[col], errors='ignore')
            if df[col].dtype == 'datetime64[ns]':
                date_cols.append(col)
                continue
        except:
            pass
        
        # Check if numeric
        if pd.api.types.is_numeric_dtype(df[col]):
            numeric_cols.append(col)
        else:
            categorical_cols.append(col)
    
    # ===================== SIDEBAR FILTERS =====================
    with st.sidebar:
        st.markdown("---")
        st.header(f"🔧 {lang['filter_data']}")
        
        # Row limit
        row_limit = st.slider("Rows to display", 5, 100, 20)
        
        # Column selection
        if numeric_cols:
            selected_numeric = st.multiselect(
                f"📈 {lang['select_value_col']}",
                numeric_cols,
                default=numeric_cols[:min(2, len(numeric_cols))]
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
        
        # Reset button
        if st.button(f"🔄 {lang['reset']}"):
            st.session_state.df = None
            st.session_state.processed = False
            st.rerun()
    
    # ===================== DATA PREVIEW =====================
    st.header(f"🔍 {lang['data_preview']}")
    st.dataframe(df.head(row_limit), use_container_width=True)
    
    # ===================== KPI SECTION =====================
    st.header(f"📈 {lang['kpi_section']}")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(lang['total_records'], len(df))
    
    with col2:
        st.metric(lang['total_columns'], len(df.columns))
    
    with col3:
        st.metric(lang['date_columns'], len(date_cols))
    
    with col4:
        st.metric(lang['numeric_columns'], len(numeric_cols))
    
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        missing_total = df.isnull().sum().sum()
        st.metric(lang['missing_values'], missing_total)
    
    with col6:
        duplicate_rows = df.duplicated().sum()
        st.metric("Duplicate Rows", duplicate_rows)
    
    with col7:
        memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
        st.metric("Memory Usage (MB)", f"{memory_usage:.2f}")
    
    with col8:
        if numeric_cols:
            avg_numeric = df[numeric_cols].mean().mean()
            st.metric("Avg Numeric Value", f"{avg_numeric:.2f}")
    
    st.markdown("---")
    
    # ===================== CHARTS SECTION =====================
    st.header(f"📊 {lang['charts_section']}")
    
    # Create tabs for charts
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Data Types", 
        "📈 Time Series", 
        "📊 Distributions", 
        "🔗 Correlations", 
        "🏷️ Categories"
    ])
    
    with tab1:
        # Data Types Distribution
        st.subheader(lang['data_types'])
        dtype_counts = df.dtypes.astype(str).value_counts().reset_index()
        dtype_counts.columns = ['Data Type', 'Count']
        
        if not dtype_counts.empty:
            fig1 = px.pie(
                dtype_counts, 
                values='Count', 
                names='Data Type',
                title=lang['data_types'],
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        # Time Series Analysis
        if selected_date and selected_numeric:
            st.subheader(lang['time_series'])
            
            # Aggregate by date
            time_series_df = df.groupby(selected_date)[selected_numeric].sum().reset_index()
            
            fig2 = go.Figure()
            for col in selected_numeric:
                fig2.add_trace(go.Scatter(
                    x=time_series_df[selected_date],
                    y=time_series_df[col],
                    mode='lines+markers',
                    name=col,
                    line=dict(width=2)
                ))
            
            fig2.update_layout(
                title=f"{lang['trend']} Analysis",
                xaxis_title=selected_date,
                yaxis_title="Value",
                hovermode='x unified',
                height=500
            )
            
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("Select a date column and numeric columns for time series analysis")
    
    with tab3:
        # Distribution Analysis
        if selected_numeric:
            st.subheader(lang['distribution'])
            
            selected_var = st.selectbox(
                "Select variable:",
                selected_numeric,
                key="dist_var"
            )
            
            col_dist1, col_dist2 = st.columns(2)
            
            with col_dist1:
                # Histogram
                fig3a = px.histogram(
                    df, 
                    x=selected_var,
                    title=f"Histogram of {selected_var}",
                    nbins=30,
                    color_discrete_sequence=['#636EFA'],
                    marginal="box"
                )
                fig3a.update_layout(height=400)
                st.plotly_chart(fig3a, use_container_width=True)
            
            with col_dist2:
                # Box plot
                fig3b = px.box(
                    df, 
                    y=selected_var,
                    title=f"Box Plot of {selected_var}",
                    color_discrete_sequence=['#00CC96']
                )
                fig3b.update_layout(height=400)
                st.plotly_chart(fig3b, use_container_width=True)
        else:
            st.info("Select numeric columns for distribution analysis")
    
    with tab4:
        # Correlation Matrix
        if len(selected_numeric) > 1:
            st.subheader(lang['correlation'])
            
            corr_matrix = df[selected_numeric].corr()
            
            fig4 = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto",
                color_continuous_scale='RdBu_r',
                title=lang['correlation'],
                height=500
            )
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("Select at least 2 numeric columns for correlation analysis")
    
    with tab5:
        # Category Analysis
        if selected_category:
            st.subheader(lang['category_analysis'])
            
            col_cat1, col_cat2 = st.columns(2)
            
            with col_cat1:
                # Top categories bar chart
                top_cats = df[selected_category].value_counts().head(10).reset_index()
                top_cats.columns = [selected_category, 'Count']
                
                fig5a = px.bar(
                    top_cats,
                    x=selected_category,
                    y='Count',
                    title=f"Top 10 {selected_category}",
                    color='Count',
                    color_continuous_scale='Viridis'
                )
                fig5a.update_layout(height=400, xaxis_tickangle=45)
                st.plotly_chart(fig5a, use_container_width=True)
            
            with col_cat2:
                # Category vs numeric value
                if selected_numeric:
                    num_col = selected_numeric[0]
                    cat_avg = df.groupby(selected_category)[num_col].mean().reset_index()
                    cat_avg.columns = [selected_category, f'Avg {num_col}']
                    cat_avg = cat_avg.sort_values(f'Avg {num_col}', ascending=False).head(10)
                    
                    fig5b = px.bar(
                        cat_avg,
                        x=selected_category,
                        y=f'Avg {num_col}',
                        title=f"Average {num_col} by {selected_category}",
                        color=f'Avg {num_col}',
                        color_continuous_scale='Plasma'
                    )
                    fig5b.update_layout(height=400, xaxis_tickangle=45)
                    st.plotly_chart(fig5b, use_container_width=True)
                else:
                    # Pie chart if no numeric columns
                    top_cats_pie = df[selected_category].value_counts().head(10).reset_index()
                    top_cats_pie.columns = [selected_category, 'Count']
                    
                    fig_pie = px.pie(
                        top_cats_pie,
                        values='Count',
                        names=selected_category,
                        title=f"Top 10 {selected_category}",
                        hole=0.3
                    )
                    fig_pie.update_layout(height=400)
                    st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("Select a categorical column for category analysis")
    
    # ===================== DATA DOWNLOAD =====================
    st.markdown("---")
    st.header(f"💾 {lang['download_data']}")
    
    col_dl1, col_dl2 = st.columns(2)
    
    with col_dl1:
        # CSV Download
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download as CSV",
            data=csv_data,
            file_name="processed_data.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col_dl2:
        # Excel Download
        try:
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Data')
            excel_data = output.getvalue()
            
            st.download_button(
                label="📥 Download as Excel",
                data=excel_data,
                file_name="processed_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        except:
            st.info("Install openpyxl for Excel download")

else:
    # Show instructions when no file is uploaded
    st.info(f"👆 {lang['upload_desc']}")
    
    st.markdown("### 📋 Example Data Structure")
    sample_data = {
        'Date': pd.date_range('2024-01-01', periods=5),
        'Sales': [1000, 1500, 800, 2000, 1200],
        'Quantity': [10, 15, 8, 20, 12],
        'Category': ['A', 'B', 'A', 'C', 'B'],
        'Region': ['North', 'South', 'North', 'East', 'West']
    }
    sample_df = pd.DataFrame(sample_data)
    st.dataframe(sample_df, use_container_width=True)
    
    st.markdown("""
    **Ideal data should include:**
    - 📅 At least one date column
    - 🔢 At least one numeric column
    - 🏷️ At least one categorical column
    """)

# ===================== FOOTER =====================
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>📊 <b>Multi-Language Business Dashboard</b> • v2.0 • Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Add simple CSS
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    .stDownloadButton > button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)
