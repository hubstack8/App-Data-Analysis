import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit page config for wider layout
st.set_page_config(
    page_title="computational infrastructure Entities Usage Analytics Dashboard", 
    layout="wide",
    page_icon="🖥️",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Category headers */
    .category-header {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #2a5298;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: white;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2a5298;
        color: white;
        border-color: #2a5298;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #f0f2f6;
        border: 1px solid #d0d2d6;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #e0e2e6;
        border-color: #b0b2b6;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Metric cards */
    [data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Success/Error messages */
    .stSuccess {
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
        padding: 0.75rem;
        border-radius: 6px;
    }
    
    .stError {
        background-color: #f8d7da;
        border-color: #f5c6cb;
        color: #721c24;
        padding: 0.75rem;
        border-radius: 6px;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header with gradient
st.markdown("""
<div class="main-header">
    <h1 style="margin: 0; font-size: 2.5rem;">🖥️ Computational Infrastructure Entities Usage Analytics Dashboard</h1>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 1.1rem;">Comprehensive Analysis of Hardware, Software, and Research Trends</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# CONFIGURATION SECTION - EASY TO MODIFY
# =============================================================================

# Base paths - Update these according to your directory structure
BASE_PATHS = {
    "country": "EDA_fig/Country",
    "organization": "EDA_fig/organisation",
    "paper": "EDA_fig/paper",
    "cloud_platform": "EDA_fig/CLoud_platform",
    "hardware": "EDA_fig/hardware",
    "affiliation": "EDA_fig/Affiliation_Overview",
    "software": "EDA_fig/software",
    "topic": "EDA_fig/topic_modelling"
}


# Define your visualizations here - Add new ones by simply adding to this dictionary
VISUALIZATIONS = {
    # Country visualizations
    "GPU Usage Country wise (Hierarchical)": {
        "file_path": os.path.join(BASE_PATHS["country"], "country_gpu_usage_plotly_viz_5.html"),
        "description": "Hierarchical visualization of GPU usage by country",
        "icon": "🌍",
        "category": "country"
    },
    
    # Organization visualizations
    "GPU Usage Organisation wise (Hierarchical)": {
        "file_path": os.path.join(BASE_PATHS["organization"], "org_gpu_usage_plotly_viz_5.html"),
        "description": "GPU Usage organisation wise (Hierarchical)",
        "icon": "🏢",
        "category": "organization"
    },
    
    # Paper visualizations
    "GPU vs CPU Paper Count": {
        "file_path": os.path.join(BASE_PATHS["paper"], "total_paper_gpu_cpu_paper.html"),
        "description": "GPU vs CPU paper count visualization",
        "icon": "📊",
        "category": "paper"
    },
        "Overall entities distribution": {
        "file_path": os.path.join(BASE_PATHS["paper"], "overall_entity_distribution.html"),
        "description": "Overall entities distribution",
        "icon": "📊",
        "category": "paper"
    },
    
    # Cloud Platform visualizations
    "Top Cloud Platform Usage past 10 years": {
        "file_path": os.path.join(BASE_PATHS["cloud_platform"], "cloud_platform_total_usage_sunburst.html"),
        "description": "Cloud platform usage over time",
        "icon": "☁️",
        "category": "cloud_platform"
    },
    "Top Organizations by Cloud Platform Usage": {
        "file_path": os.path.join(BASE_PATHS["cloud_platform"], "Cloud_Platform_usage_organisation_plotly_viz_1.html"),
        "description": "Leading organizations in cloud platform adoption",
        "icon": "🏢",
        "category": "cloud_platform"
    },
    "Top Countries by Cloud Platform Usage": {
        "file_path": os.path.join(BASE_PATHS["cloud_platform"], "Cloud_Platform_country_usage_plotly_viz_3.html"),
        "description": "Geographic distribution of cloud platform usage",
        "icon": "🌍",
        "category": "cloud_platform"
    },
    "AWS Services Usage Trends": {
        "file_path": os.path.join(BASE_PATHS["cloud_platform"], "aws_base_entities_interactive_dashboard.html"),
        "description": "Detailed analysis of AWS services adoption over time",
        "icon": "🔶",
        "category": "cloud_platform"
    },
    "Google Cloud Services Usage Trends": {
        "file_path": os.path.join(BASE_PATHS["cloud_platform"], "google_clould_base_entities_interactive_dashboard.html"),
        "description": "Comprehensive view of Google Cloud services utilization",
        "icon": "🔵",
        "category": "cloud_platform"
    },
    
    # Hardware visualizations
    "Device Memory Configuration Usage": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "device_memory_analysis.html"),
        "description": "Analysis of device memory configurations across research papers",
        "icon": "💾",
        "category": "hardware"
    },
    "GPU Brand Distribution": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "gpu_brand_distribution.html"),
        "description": "Market share analysis of GPU brands in research",
        "icon": "🎮",
        "category": "hardware"
    },
    "Hardware Device Categories": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "gpu_category_distribution.html"),
        "description": "Distribution of hardware devices by category",
        "icon": "📱",
        "category": "hardware"
    },
    "GPU Generation Evolution": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "gpu_evolution_over_time.html"),
        "description": "Timeline of GPU generation adoption in research",
        "icon": "📈",
        "category": "hardware"
    },
    "Hardware-Memory Co-occurrence": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "hardware_memory_bubble_chart.html"),
        "description": "Correlation analysis between hardware types and memory configurations",
        "icon": "🔗",
        "category": "hardware"
    },
    "Nvidia GPU Generations": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "nvidia_gpu_generations.html"),
        "description": "Detailed breakdown of Nvidia GPU usage by generation",
        "icon": "🟢",
        "category": "hardware"
    },
    "Top Hardware-Count Combinations": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "top_hardware_count_combinations.html"),
        "description": "Most common hardware and device count configurations",
        "icon": "🔢",
        "category": "hardware"
    },
    "Most Used Hardware Devices": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "top_hardware_devices.html"),
        "description": "Ranking of the 30 most frequently used hardware devices",
        "icon": "🏆",
        "category": "hardware"
    },
    "Hardware-Memory-Count Configurations": {
        "file_path": os.path.join(BASE_PATHS["hardware"], "top_hardware_memory_count_triplets.html"),
        "description": "Analysis of common hardware, memory, and count combinations",
        "icon": "⚙️",
        "category": "hardware"
    },
    
    # Affiliation visualizations
    "Collaboration Network": {
        "file_path": os.path.join(BASE_PATHS["affiliation"], "collaboration_network.html"),
        "description": "Interactive network visualization of top 50 research collaborations",
        "icon": "🤝",
        "category": "affiliation"
    },
    "Top Collaboration Pairs": {
        "file_path": os.path.join(BASE_PATHS["affiliation"], "collaboration_pairs_top20.html"),
        "description": "Most frequent organization collaboration pairs",
        "icon": "👥",
        "category": "affiliation"
    },
    "International Collaborations": {
        "file_path": os.path.join(BASE_PATHS["affiliation"], "international_collaborations.html"),
        "description": "Cross-border research collaboration patterns",
        "icon": "🌐",
        "category": "affiliation"
    },
    "Organization Activity": {
        "file_path": os.path.join(BASE_PATHS["affiliation"], "organization_collaboration_activity.html"),
        "description": "Research activity levels of top 25 organizations",
        "icon": "📊",
        "category": "affiliation"
    },
    "Collaboration Intensity": {
        "file_path": os.path.join(BASE_PATHS["affiliation"], "collaboration_diversity_analysis.html"),
        "description": "Analysis of collaboration intensity and diversity metrics",
        "icon": "📈",
        "category": "affiliation"
    },
    
    # Software visualizations
    "Entity Associations": {
        "file_path": os.path.join(BASE_PATHS["software"], "entity_associations.html"),
        "description": "Network of top 20 software entity associations",
        "icon": "🔗",
        "category": "software"
    },
    "Hardware-Software Heatmap": {
        "file_path": os.path.join(BASE_PATHS["software"], "hw_sw_heatmap.html"),
        "description": "Co-occurrence analysis of hardware and software combinations",
        "icon": "🗺️",
        "category": "software"
    },
    "Memory Distribution by Software": {
        "file_path": os.path.join(BASE_PATHS["software"], "memory_distribution_by_software.html"),
        "description": "Memory size patterns across different software frameworks",
        "icon": "💿",
        "category": "software"
    },
    "Software by Device Count": {
        "file_path": os.path.join(BASE_PATHS["software"], "software_by_device_count.html"),
        "description": "Software framework usage patterns by device count categories",
        "icon": "📱",
        "category": "software"
    },
    "Hardware-Software Co-evolution": {
        "file_path": os.path.join(BASE_PATHS["software"], "temporal_coevolution.html"),
        "description": "Temporal analysis of hardware-software co-occurrence patterns",
        "icon": "🔄",
        "category": "software"
    },
    "Software Evolution Timeline": {
        "file_path": os.path.join(BASE_PATHS["software"], "temporal_evolution.html"),
        "description": "Historical trends in software framework adoption",
        "icon": "📅",
        "category": "software"
    },
    
    # Topic Modeling visualizations
    "GPU Usage by Research Topic": {
        "file_path": os.path.join(BASE_PATHS["topic"], "3_heatmap_gpu_intensity.html"),
        "description": "Heatmap showing GPU usage intensity across different research topics",
        "icon": "🔥",
        "category": "topic"
    },
    "Device Count by Topic": {
        "file_path": os.path.join(BASE_PATHS["topic"], "device_counts_by_topic.html"),
        "description": "Average device utilization across research domains",
        "icon": "📊",
        "category": "topic"
    },
    "GPU Temporal Trends by Topic": {
        "file_path": os.path.join(BASE_PATHS["topic"], "gpu_temporal_trends_clean.html"),
        "description": "Evolution of GPU usage patterns across research topics over time",
        "icon": "📈",
        "category": "topic"
    },
    "GPU Usage Rate by Topic": {
        "file_path": os.path.join(BASE_PATHS["topic"], "gpu_usage_by_topic_clean.html"),
        "description": "Comparative analysis of GPU adoption rates by research area",
        "icon": "💹",
        "category": "topic"
    }
}

# Height presets
HEIGHT_PRESETS = {
    "Compact": 600,
    "Small": 800,
    "Standard": 1000,
    "Large": 1200,
    "Extra Large": 1400,
    "Full": 1600
}

# Category display configuration
CATEGORY_CONFIG = {
    "country": {"name": "Geographic Analysis", "icon": "🌍", "color": "#3498db"},
    "organization": {"name": "Organizational Insights", "icon": "🏢", "color": "#e74c3c"},
    "paper": {"name": "Publication Metrics", "icon": "📄", "color": "#f39c12"},
    "cloud_platform": {"name": "Cloud Platform Analytics", "icon": "☁️", "color": "#9b59b6"},
    "hardware": {"name": "Hardware Analysis", "icon": "🖥️", "color": "#1abc9c"},
    "affiliation": {"name": "Collaboration Networks", "icon": "🤝", "color": "#34495e"},
    "software": {"name": "Software Ecosystem", "icon": "💻", "color": "#16a085"},
    "topic": {"name": "Research Topics", "icon": "🔬", "color": "#d35400"}
}

# =============================================================================
# CORE FUNCTIONS
# =============================================================================

def render_plotly_html_large(html_path, height=1000):
    """Load and embed Plotly HTML with consistent size."""
    if not os.path.exists(html_path):
        st.error(f"⚠️ Could not find the file: {html_path}")
        return
    
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Enhanced styling with better responsiveness
        wrapped_html = f"""
        <div style="width:100%; height:{height}px; overflow:auto; border: 1px solid #e0e0e0; border-radius: 10px; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <style>
                /* Reset and base styles */
                * {{ box-sizing: border-box; }}
                body {{ margin: 0; padding: 20px; background: white; }}
                
                /* Force Plotly container dimensions */
                .plotly-graph-div {{ 
                    width: 100% !important; 
                    height: {height-60}px !important;
                    min-height: {height-60}px !important;
                }}
                
                /* Ensure proper scaling */
                .plotly-graph-div > div {{ 
                    width: 100% !important;
                    height: 100% !important;
                }}
            </style>
            {html_content}
            
            <script>
                // Force resize after load
                setTimeout(function() {{
                    if (typeof Plotly !== 'undefined') {{
                        var plots = document.querySelectorAll('.plotly-graph-div');
                        plots.forEach(function(plot) {{
                            Plotly.Plots.resize(plot);
                        }});
                    }}
                }}, 500);
            </script>
        </div>
        """
        
        components.html(wrapped_html, height=height, scrolling=True)
        
    except Exception as e:
        st.error(f"❌ Error loading visualization: {str(e)}")
        st.info("Please check the file format and ensure it's a valid HTML file.")

def get_visualizations_by_category():
    """Organize visualizations by category."""
    categories = {}
    for viz_name, config in VISUALIZATIONS.items():
        category = config.get("category", "other")
        if category not in categories:
            categories[category] = []
        categories[category].append((viz_name, config))
    return categories

def render_category_section(category_name, visualizations):
    """Render a category section with its visualizations."""
    # Get category configuration
    cat_config = CATEGORY_CONFIG.get(category_name, {
        "name": category_name.replace("_", " ").title(),
        "icon": "📊",
        "color": "#95a5a6"
    })
    
    # Category header with custom styling
    st.markdown(f"""
    <div class="category-header" style="border-left-color: {cat_config['color']}">
        <h2 style="margin: 0; color: {cat_config['color']}">
            {cat_config['icon']} {cat_config['name']}
        </h2>
        <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;">
            {len(visualizations)} visualizations available
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for visualizations
    viz_names = [config.get('icon', '📊') + " " + viz_name for viz_name, config in visualizations]
    tabs = st.tabs(viz_names)
    
    # Render each visualization
    for tab, (viz_name, config) in zip(tabs, visualizations):
        with tab:
            # Visualization header
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {config['description']}")
            with col2:
                file_exists = os.path.exists(config["file_path"])
                if file_exists:
                    st.success("✅ Available")
                else:
                    st.error("❌ Not Found")
                    continue
            
            # Height controls in columns
            col1, col2, col3, col4 = st.columns(4)
            
            height = HEIGHT_PRESETS["Standard"]  # Default
            
            with col1:
                if st.button("🔹 Compact", key=f"compact_{category_name}_{viz_name}", use_container_width=True):
                    height = HEIGHT_PRESETS["Compact"]
            
            with col2:
                if st.button("🔸 Standard", key=f"standard_{category_name}_{viz_name}", use_container_width=True):
                    height = HEIGHT_PRESETS["Standard"]
            
            with col3:
                if st.button("🔶 Large", key=f"large_{category_name}_{viz_name}", use_container_width=True):
                    height = HEIGHT_PRESETS["Large"]
            
            with col4:
                if st.button("🔷 Full", key=f"full_{category_name}_{viz_name}", use_container_width=True):
                    height = HEIGHT_PRESETS["Full"]
            
            # Custom height expander
            with st.expander("⚙️ Advanced Size Settings"):
                custom_height = st.slider(
                    "Custom Height (pixels)", 
                    min_value=400, 
                    max_value=2000, 
                    value=height, 
                    step=50,
                    key=f"slider_{category_name}_{viz_name}"
                )
                if st.button("Apply Custom Size", key=f"apply_{category_name}_{viz_name}"):
                    height = custom_height
            
            # Render visualization
            render_plotly_html_large(config["file_path"], height=height)

# =============================================================================
# MAIN APP LAYOUT
# =============================================================================

# Get categories
categories = get_visualizations_by_category()

# Create main navigation tabs
main_tab_names = []
for cat_key in categories.keys():
    cat_config = CATEGORY_CONFIG.get(cat_key, {"name": cat_key, "icon": "📊"})
    main_tab_names.append(f"{cat_config['icon']} {cat_config['name']}")

main_tabs = st.tabs(main_tab_names)

# Render each category
for main_tab, (category_name, visualizations) in zip(main_tabs, categories.items()):
    with main_tab:
        render_category_section(category_name, visualizations)

# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("### 🎛️ Dashboard Controls")
    
    # Quick stats
    st.markdown("#### 📊 Quick Stats")
    total_viz = len(VISUALIZATIONS)
    working_viz = sum(1 for config in VISUALIZATIONS.values() if os.path.exists(config["file_path"]))
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total", total_viz)
    with col2:
        st.metric("Active", working_viz)
    
    st.progress(working_viz / total_viz if total_viz > 0 else 0)
    
    # File status by category
    st.markdown("#### 📁 Status by Category")
    
    for category_name, viz_list in categories.items():
        cat_config = CATEGORY_CONFIG.get(category_name, {"name": category_name, "icon": "📊"})
        working = sum(1 for _, config in viz_list if os.path.exists(config["file_path"]))
        total = len(viz_list)
        
        st.markdown(f"""
        **{cat_config['icon']} {cat_config['name']}**  
        {working}/{total} visualizations active
        """)
        
        if working < total:
            with st.expander(f"View missing files ({total - working})"):
                for viz_name, config in viz_list:
                    if not os.path.exists(config["file_path"]):
                        st.error(f"❌ {viz_name}")
    
    # Refresh button
    st.markdown("---")
    if st.button("🔄 Refresh Dashboard", use_container_width=True):
        st.rerun()
    
    # Help section
    with st.expander("❓ Help & Instructions"):
        st.markdown("""
        **Adding New Visualizations:**
        
        1. Add to `VISUALIZATIONS` dictionary
        2. Specify: file_path, description, icon, category
        3. Save and refresh the dashboard
        
        **File Requirements:**
        - HTML files with Plotly visualizations
        - Place in appropriate category folder
        - Ensure correct file paths
        
        **Categories:**
        - country: Geographic analysis
        - organization: Organizational data
        - hardware: Hardware metrics
        - software: Software analysis
        - cloud_platform: Cloud services
        - affiliation: Collaborations
        - topic: Research topics
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; color: #666;'>
    <p style='margin: 0;'>GPU Usage Analytics Dashboard</p>
    <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;'>
        Powered by Streamlit • Data Visualization Suite
    </p>
</div>
""", unsafe_allow_html=True)

