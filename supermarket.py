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
    layout="wide"
)

# ===================== MULTI-LANGUAGE SUPPORT =====================
# Language dictionary
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

# Initialize session state for language
if 'language' not in st.session_state:
    st.session_state.language = "English"
if 'df' not in st.session_state:
    st.session_state.df = None
if 'processed' not in st.session_state:
    st.session_state.processed = False
if 'file_name' not in st.session_state:
    st.session_state.file_name = None

# Language selector in sidebar
with st.sidebar:
    st.title("🌍 Language / 语言 / Bahasa")
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

# ===================== HELPER FUNCTIONS =====================
def detect_column_types(df):
    """Detect column types with better accuracy"""
    date_cols = []
    numeric_cols = []
    categorical_cols = []
    
    for col in df.columns:
        # Try to detect date columns
        try:
            # Convert to datetime if possible
            temp_series = pd.to_datetime(df[col], errors='coerce')
            if temp_series.notna().any():
                date_cols.append(col)
                continue
        except:
            pass
        
        # Check if numeric
        if pd.api.types.is_numeric_dtype(df[col]):
            numeric_cols.append(col)
        # Check if categorical/object
        elif pd.api.types.is_string_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
            categorical_cols.append(col)
        else:
            # Default to categorical for unknown types
            categorical_cols.append(col)
    
    return date_cols, numeric_cols, categorical_cols

def clean_dataframe(df):
    """Clean and prepare dataframe for analysis"""
    df_clean = df.copy()
    
    # Convert object columns with few unique values to category
    for col in df_clean.select_dtypes(include=['object']).columns:
        if df_clean[col].nunique() < 50:
            df_clean[col] = df_clean[col].astype('category')
    
    return df_clean

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
                # For older Excel format
                df = pd.read_excel(uploaded_file, engine='xlrd')
            else:
                # For newer Excel format
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            
            # Clean and process data
            df = clean_dataframe(df)
            
            # Store in session state
            st.session_state.df = df
            st.session_state.processed = True
            st.session_state.file_name = uploaded_file.name
            
            st.success(f"✅ {lang['file_uploaded']}: {uploaded_file.name}")
            
            # Show file info
            st.info(f"📄 **File Details:** {uploaded_file.name} | Size: {uploaded_file.size / 1024:.1f} KB")
            
    except Exception as e:
        st.error(f"❌ {lang['error']}: {str(e)}")
        st.info("""
        💡 **Tips untuk mengatasi error:**
        1. Pastikan file Excel tidak sedang terbuka di aplikasi lain
        2. Pastikan format file benar (.xlsx atau .xls)
        3. Coba install dependencies: `pip install openpyxl xlrd`
        4. Jika file .xls, pastikan engine='xlrd'
        """)

# Display dashboard if data is available
if st.session_state.processed and st.session_state.df is not None:
    df = st.session_state.df
    
    # Detect column types
    date_cols, numeric_cols, categorical_cols = detect_column_types(df)
    
    # ===================== DATA PREVIEW =====================
    st.header(f"🔍 {lang['data_preview']}")
    
    # Data filters in sidebar
    with st.sidebar:
        st.header(f"🔧 {lang['filter_data']}")
        
        # Column type filters
        if numeric_cols:
            selected_numeric = st.multiselect(
                f"📈 {lang['select_value_col']}",
                numeric_cols,
                default=numeric_cols[:min(2, len(numeric_cols))]
            )
        else:
            selected_numeric = []
            st.warning(lang['no_numeric_col'])
        
        # Date filter
        if date_cols:
            selected_date = st.selectbox(
                f"📅 {lang['select_date_col']}",
                date_cols
            )
        else:
            selected_date = None
            st.warning(lang['no_date_col'])
        
        # Categorical filter
        if categorical_cols:
            selected_category = st.selectbox(
                f"🏷️ {lang['select_category_col']}",
                categorical_cols
            )
        else:
            selected_category = None
            st.warning(lang['no_category_col'])
        
        # Row limit
        row_limit = st.slider("Rows to display", 5, 100, 10)
        
        # Missing values filter
        show_missing_only = st.checkbox("Show only rows with missing values", False)
        
        st.markdown("---")
        st.markdown(f"**📊 Data Summary:**")
        st.markdown(f"- Rows: {len(df)}")
        st.markdown(f"- Columns: {len(df.columns)}")
        st.markdown(f"- Memory: {df.memory_usage(deep=True).sum() / 1024 / 1024:.1f} MB")
    
    # Display filtered data preview
    preview_df = df.copy()
    
    if show_missing_only:
        # Show only rows with any missing values
        preview_df = preview_df[preview_df.isnull().any(axis=1)]
    
    st.dataframe(preview_df.head(row_limit), use_container_width=True)
    
    if len(preview_df) == 0 and show_missing_only:
        st.success("✅ No rows with missing values found!")
    
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
    
    # Additional metrics row
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        missing_total = df.isnull().sum().sum()
        st.metric(lang['missing_values'], missing_total)
    
    with col6:
        duplicate_rows = df.duplicated().sum()
        st.metric("Duplicate Rows / Baris Duplikat / 重复行数", duplicate_rows)
    
    with col7:
        memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
        st.metric("Memory Usage (MB)", f"{memory_usage:.1f}")
    
    with col8:
        if numeric_cols:
            avg_numeric = df[numeric_cols].mean().mean()
            st.metric("Avg Numeric Value", f"{avg_numeric:.2f}")
        else:
            st.metric("Avg Numeric Value", "N/A")
    
    st.markdown("---")
    
    # ===================== CHARTS SECTION =====================
    st.header(f"📊 {lang['charts_section']}")
    
    # Create tabs for better organization
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Data Types", 
        "📈 Time Series", 
        "📊 Distributions", 
        "🔗 Correlations", 
        "🏷️ Categories"
    ])
    
    with tab1:
        # Chart 1: Data Types Distribution
        st.subheader(f"{lang['data_types']}")
        dtype_counts = df.dtypes.astype(str).value_counts().reset_index()
        dtype_counts.columns = ['Data Type', 'Count']
        
        if len(dtype_counts) > 0:
            fig1 = px.pie(
                dtype_counts, 
                values='Count', 
                names='Data Type',
                title=f"{lang['data_types']} Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("No data available for data type analysis")
    
    with tab2:
        # Chart 2: Time Series Analysis
        if selected_date and selected_numeric:
            st.subheader(f"{lang['time_series']}")
            
            # Aggregate by date
            time_series_df = df.groupby(selected_date)[selected_numeric].sum().reset_index()
            
            # Create line chart
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
            
            # Show summary statistics
            col_ts1, col_ts2, col_ts3 = st.columns(3)
            with col_ts1:
                if len(time_series_df) > 1:
                    latest_value = time_series_df[selected_numeric[0]].iloc[-1]
                    previous_value = time_series_df[selected_numeric[0]].iloc[-2] if len(time_series_df) > 1 else 0
                    growth = ((latest_value - previous_value) / previous_value * 100) if previous_value != 0 else 0
                    st.metric(f"Latest {selected_numeric[0]}", f"{latest_value:,.2f}", f"{growth:+.1f}%")
            
            with col_ts2:
                if len(time_series_df) > 0:
                    total_value = time_series_df[selected_numeric[0]].sum()
                    st.metric(f"Total {selected_numeric[0]}", f"{total_value:,.2f}")
            
            with col_ts3:
                if len(time_series_df) > 0:
                    avg_value = time_series_df[selected_numeric[0]].mean()
                    st.metric(f"Average {selected_numeric[0]}", f"{avg_value:,.2f}")
        else:
            st.info("Select a date column and numeric columns for time series analysis")
    
    with tab3:
        # Chart 3: Distribution Analysis
        if selected_numeric:
            st.subheader(f"{lang['distribution']}")
            
            selected_var = st.selectbox(
                "Select variable for distribution analysis:",
                selected_numeric,
                key="dist_var"
            )
            
            col_chart3_1, col_chart3_2 = st.columns(2)
            
            with col_chart3_1:
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
            
            with col_chart3_2:
                # Box plot
                fig3b = px.box(
                    df, 
                    y=selected_var,
                    title=f"Box Plot of {selected_var}",
                    color_discrete_sequence=['#00CC96']
                )
                fig3b.update_layout(height=400)
                st.plotly_chart(fig3b, use_container_width=True)
            
            # Statistics
            col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
            with col_stats1:
                st.metric("Mean", f"{df[selected_var].mean():.2f}")
            with col_stats2:
                st.metric("Median", f"{df[selected_var].median():.2f}")
            with col_stats3:
                st.metric("Std Dev", f"{df[selected_var].std():.2f}")
            with col_stats4:
                st.metric("Skewness", f"{df[selected_var].skew():.2f}")
        else:
            st.info("Select numeric columns for distribution analysis")
    
    with tab4:
        # Chart 4: Correlation Matrix
        if len(selected_numeric) > 1:
            st.subheader(f"{lang['correlation']}")
            
            corr_matrix = df[selected_numeric].corr()
            
            fig4 = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto",
                color_continuous_scale='RdBu_r',
                title=f"{lang['correlation']} Matrix",
                labels=dict(color="Correlation"),
                height=500
            )
            st.plotly_chart(fig4, use_container_width=True)
            
            # Find top correlations
            st.subheader("Top Correlations")
            corr_pairs = []
            for i in range(len(corr_matrix.columns)):
                for j in range(i+1, len(corr_matrix.columns)):
                    corr_pairs.append({
                        'Variable 1': corr_matrix.columns[i],
                        'Variable 2': corr_matrix.columns[j],
                        'Correlation': corr_matrix.iloc[i, j]
                    })
            
            corr_df = pd.DataFrame(corr_pairs)
            corr_df['Abs Correlation'] = corr_df['Correlation'].abs()
            corr_df = corr_df.sort_values('Abs Correlation', ascending=False).head(10)
            
            st.dataframe(corr_df[['Variable 1', 'Variable 2', 'Correlation']].round(3), use_container_width=True)
        else:
            st.info("Select at least 2 numeric columns for correlation analysis")
    
    with tab5:
        # Chart 5: Category Analysis
        if selected_category:
            st.subheader(f"{lang['category_analysis']}")
            
            col_cat1, col_cat2 = st.columns(2)
            
            with col_cat1:
                # Top categories bar chart
                top_categories = df[selected_category].value_counts().head(15).reset_index()
                top_categories.columns = [selected_category, 'Count']
                
                fig5a = px.bar(
                    top_categories,
                    x=selected_category,
                    y='Count',
                    title=f"Top 15 {selected_category} Categories",
                    color='Count',
                    color_continuous_scale='Viridis',
                    height=400
                )
                fig5a.update_xaxes(tickangle=45)
                st.plotly_chart(fig5a, use_container_width=True)
            
            with col_cat2:
                # Category vs numeric value
                if selected_numeric:
                    category_avg = df.groupby(selected_category)[selected_numeric].mean().mean(axis=1).reset_index()
                    category_avg.columns = [selected_category, 'Average Value']
                    category_avg = category_avg.sort_values('Average Value', ascending=False).head(15)
                    
                    fig5b = px.bar(
                        category_avg,
                        x=selected_category,
                        y='Average Value',
                        title=f"Average Values by {selected_category}",
                        color='Average Value',
                        color_continuous_scale='Plasma',
                        height=400
                    )
                    fig5b.update_xaxes(tickangle=45)
                    st.plotly_chart(fig5b, use_container_width=True)
                else:
                    st.info("Select numeric columns to see average values by category")
            
            # Show category statistics
            st.subheader("Category Statistics")
            col_cat_stats1, col_cat_stats2, col_cat_stats3 = st.columns(3)
            
            with col_cat_stats1:
                unique_cats = df[selected_category].nunique()
                st.metric("Unique Categories", unique_cats)
            
            with col_cat_stats2:
                top_cat = df[selected_category].mode().iloc[0] if len(df[selected_category].mode()) > 0 else "N/A"
                st.metric("Most Common Category", str(top_cat))
            
            with col_cat_stats3:
                if selected_numeric and len(selected_numeric) > 0:
                    cat_with_max = df.loc[df[selected_numeric[0]].idxmax(), selected_category]
                    st.metric(f"Category with Max {selected_numeric[0]}", str(cat_with_max))
        else:
            st.info("Select a categorical column for category analysis")
    
    # ===================== DATA SUMMARY & INSIGHTS =====================
    st.markdown("---")
    st.header(f"💡 {lang['insights']}")
    
    col_insight1, col_insight2 = st.columns(2)
    
    with col_insight1:
        st.subheader(f"📋 {lang['data_summary']}")
        
        summary_stats = []
        
        # Basic stats
        summary_stats.append(f"**{lang['total_records']}**: {len(df):,}")
        summary_stats.append(f"**{lang['total_columns']}**: {len(df.columns)}")
        summary_stats.append(f"**{lang['missing_values']}**: {df.isnull().sum().sum():,}")
        summary_stats.append(f"**Duplicate Rows**: {df.duplicated().sum():,}")
        
        if numeric_cols:
            summary_stats.append(f"**{lang['numeric_columns']}**: {len(numeric_cols)}")
            if len(numeric_cols) > 0:
                total_numeric = df[numeric_cols].sum().sum()
                summary_stats.append(f"**Total numeric values**: {total_numeric:,.2f}")
        
        if date_cols:
            summary_stats.append(f"**{lang['date_columns']}**: {len(date_cols)}")
            if len(date_cols) > 0:
                date_range = f"{df[date_cols[0]].min().date()} to {df[date_cols[0]].max().date()}"
                summary_stats.append(f"**Date range**: {date_range}")
        
        if categorical_cols:
            summary_stats.append(f"**Categorical columns**: {len(categorical_cols)}")
        
        for stat in summary_stats:
            st.markdown(f"• {stat}")
    
    with col_insight2:
        st.subheader(f"🔍 Quick {lang['insights']}")
        
        insights = []
        
        # Generate insights based on data
        missing_total = df.isnull().sum().sum()
        if missing_total > 0:
            missing_pct = (missing_total / (len(df) * len(df.columns))) * 100
            insights.append(f"⚠️ **Missing Values**: {missing_total:,} values ({missing_pct:.1f}%) - Consider data imputation")
        
        duplicate_rows = df.duplicated().sum()
        if duplicate_rows > 0:
            dup_pct = (duplicate_rows / len(df)) * 100
            insights.append(f"⚠️ **Duplicates**: {duplicate_rows:,} rows ({dup_pct:.1f}%) - Consider removing duplicates")
        
        if numeric_cols and len(selected_numeric) > 0:
            for num_col in selected_numeric[:3]:  # Check first 3 numeric columns
                skewness = df[num_col].skew()
                if abs(skewness) > 1:
                    skew_type = "right" if skewness > 0 else "left"
                    insights.append(f"📊 **Skewed Data**: '{num_col}' is {skew_type}-skewed (skewness: {skewness:.2f})")
        
        if selected_date and selected_numeric and len(selected_numeric) > 0:
            if len(df) > 1 and selected_date in df.columns:
                try:
                    sorted_df = df.sort_values(selected_date)
                    first_val = sorted_df[selected_numeric[0]].iloc[0]
                    last_val = sorted_df[selected_numeric[0]].iloc[-1]
                    if first_val != 0:
                        growth = ((last_val - first_val) / first_val) * 100
                        insights.append(f"📈 **Growth Trend**: {selected_numeric[0]} changed by {growth:+.1f}% over time")
                except:
                    pass
        
        if not insights:
            insights.append("✅ **Data Quality**: Good - No significant data quality issues detected")
            insights.append("✅ **Data Structure**: Appropriate mix of data types for analysis")
            insights.append("✅ **Ready for Analysis**: Data is clean and well-structured")
        
        for insight in insights:
            st.markdown(f"• {insight}")
    
    # ===================== DATA DOWNLOAD =====================
    st.markdown("---")
    st.header(f"💾 {lang['download_data']}")
    
    # Create processed data
    processed_df = df.copy()
    
    # Convert to different formats for download
    col_dl1, col_dl2, col_dl3 = st.columns(3)
    
    with col_dl1:
        # CSV Download
        csv_data = processed_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download as CSV",
            data=csv_data,
            file_name=f"processed_{st.session_state.file_name.replace('.xlsx', '').replace('.xls', '')}.csv",
            mime="text/csv",
            help="Download the processed data as CSV file",
            use_container_width=True
        )
    
    with col_dl2:
        # Excel Download
        try:
            import io
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                processed_df.to_excel(writer, index=False, sheet_name='Data')
                
                # Add summary sheet
                summary_data = {
                    'Metric': [lang['total_records'], lang['total_columns'], 
                              lang['missing_values'], lang['date_columns'],
                              lang['numeric_columns'], 'File Name'],
                    'Value': [len(df), len(df.columns), df.isnull().sum().sum(), 
                             len(date_cols), len(numeric_cols), st.session_state.file_name]
                }
                pd.DataFrame(summary_data).to_excel(writer, index=False, sheet_name='Summary')
            
            excel_data = output.getvalue()
            
            st.download_button(
                label="📥 Download as Excel",
                data=excel_data,
                file_name=f"processed_{st.session_state.file_name.replace('.xlsx', '').replace('.xls', '')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                help="Download the processed data as Excel file",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Cannot create Excel file: {str(e)}")
            st.info("Make sure openpyxl is installed: `pip install openpyxl`")
    
    with col_dl3:
        # Reset button
        if st.button(f"🔄 {lang['reset']} & Upload New File", use_container_width=True, type="secondary"):
            st.session_state.df = None
            st.session_state.processed = False
            st.session_state.file_name = None
            st.rerun()

else:
    # Show sample data or instructions when no file is uploaded
    st.info(f"👆 {lang['upload_desc']}")
    
    # Display sample data structure
    st.markdown("### 📋 Example Data Structure")
    
    # Create more comprehensive sample data
    sample_data = {
        'Date': pd.date_range('2024-01-01', periods=10),
        'Sales': [1000, 1500, 800, 2000, 1200, 1800, 900, 2200, 1300, 1700],
        'Quantity': [10, 15, 8, 20, 12, 18, 9, 22, 13, 17],
        'Profit': [200, 300, 150, 400, 240, 360, 180, 440, 260, 340],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 
                    'Electronics', 'Home', 'Electronics', 'Clothing', 'Home'],
        'Region': ['North', 'South', 'North', 'East', 'West', 
                  'North', 'South', 'East', 'West', 'North'],
        'Customer_Rating': [4.5, 3.8, 4.2, 4.8, 3.9, 4.6, 4.1, 4.9, 4.0, 4.3]
    }
    sample_df = pd.DataFrame(sample_data)
    st.dataframe(sample_df, use_container_width=True)
    
    st.markdown("""
    ### 🎯 **Ideal data structure should include:**
    
    | Column Type | Example | Purpose |
    |------------|---------|---------|
    | 📅 **Date/Time** | `2024-01-01`, `Order_Date` | Time series analysis, trends |
    | 🔢 **Numeric** | `Sales`, `Quantity`, `Price` | Calculations, distributions |
    | 🏷️ **Categorical** | `Category`, `Region`, `Status` | Grouping, comparisons |
    | 📝 **Text** | `Product_Name`, `Description` | Text analysis, categorization |
    
    ### 💡 **Tips for best results:**
    1. Ensure dates are in proper date format
    2. Use consistent naming conventions
    3. Clean data before uploading (remove empty rows/columns)
    4. File size should be under 200MB for optimal performance
    """)

# ===================== FOOTER =====================
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**📊 Multi-Language Business Dashboard**")
    st.markdown("Version 2.1 • Powered by Streamlit")
    st.markdown("© 2024 All rights reserved")

with footer_col2:
    st.markdown("**✨ Key Features:**")
    st.markdown("• 📈 5+ Interactive Chart Types")
    st.markdown("• 🌍 3 Language Support")
    st.markdown("• 🔍 Smart Data Detection")
    st.markdown("• 📊 Real-time Analytics")

with footer_col3:
    st.markdown("**🚀 Quick Start:**")
    st.markdown("1. 📁 Upload Excel file")
    st.markdown("2. 🌍 Select language")
    st.markdown("3. 🔍 Explore insights")
    st.markdown("4. 📥 Download results")

# Add custom CSS for better appearance
st.markdown("""
<style>
    /* Metric cards styling */
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        padding: 20px 15px;
        border-radius: 10px;
        border-left: 5px solid #4e8cff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Button styling */
    .stDownloadButton > button, .stButton > button {
        width: 100%;
        background: linear-gradient(45deg, #4e8cff, #6a5af9);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stDownloadButton > button:hover, .stButton > button:hover {
        background: linear-gradient(45deg, #3a7cff, #5a4af9);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 140, 255, 0.3);
    }
    
    /* Tab styling */
    .stT
