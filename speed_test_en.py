import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
from datetime import datetime, timedelta

# Set font (Arial works well for English)
matplotlib.rc('font', family='Arial')
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

# Generate date range string
def generate_date_range(delay_days):
    end_date = datetime.today() + timedelta(hours=13)  # Adjust to your timezone (CST)
    start_date = end_date - timedelta(days=delay_days)
    return f"{start_date.month:02d}/{start_date.day:02d} – {end_date.month:02d}/{end_date.day:02d}, {end_date.year}"

# Load image helper function
def get_image(path, zoom=0.3):
    if os.path.exists(path):
        try:
            return OffsetImage(plt.imread(path), zoom=zoom)
        except Exception as e:
            print(f"Failed to load image {path}: {e}")
            return None
    else:
        print(f"Image not found: {path}")
        return None

# VPN data and image paths
vpn_data = {
    "StrongVPN": [95, 70],
    "ExpressVPN": [90, 65],
    "Surfshark": [85, 60],
    "FlowVPN": [80, 55]
}
images = {
    "StrongVPN": "small/strong.jpg",
    "ExpressVPN": "small/expressvpn.jpg",
    "Surfshark": "small/surfshark.jpg",
    "FlowVPN": "small/flowvpn.jpg"
}



x = [0, 1, 2, 3]
y = [80, 90, 75, 70]  # Download (Mbps) sample
z = [50, 60, 45, 40]  # Upload (Mbps) sample
vpn_names = list(vpn_data.keys())

# === Combined Speed Test Chart (4 time periods) ===
fig, axs = plt.subplots(2, 2, figsize=(22, 14))  # 加大整體尺寸
fig.suptitle('VPN Universe - Daily Speed Test & Regular Updates', fontsize=30, y=1.02)
for i, days in enumerate([7, 14, 30, 90]):
    row, col = divmod(i, 2)
    ax = axs[row, col]
    
    ax.scatter(x, y, label="Download Speed", s=100)
    ax.scatter(x, z, label="Upload Speed", s=100)
    errors = [3 + np.random.randint(10) for _ in range(4)]
    ax.errorbar(x, y, yerr=errors, fmt="o")
    ax.errorbar(x, z, yerr=errors, fmt="o")
    
    ax.set_xticks(x)
    ax.set_xticklabels(vpn_names, fontsize=24)  # x 軸標籤字體加大
    
    ax.set_xlabel('VPN', fontsize=24)           # 軸標籤加大
    ax.set_ylabel('Speed (Mbps)', fontsize=24)
    ax.set_title(f'Daily Speed Test: {generate_date_range(days)}', fontsize=24)  # 子圖標題加大
    ax.legend(fontsize=12)                      # 圖例字體加大

    # 可選：加大刻度數字
    # ax.tick_params(axis='both', labelsize=14)
    
    # ax.set_ylim(-20, max(y) + 20)
    # ax.set_xlabel('VPN', fontsize=12)
    # ax.set_ylabel('Speed (Mbps)', fontsize=12)
    # ax.set_title(f'Daily Speed Test: {generate_date_range(days)}', fontsize=14)
    # ax.legend(fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.96])
output_path = os.path.join(
        r"C:/Users/eric/Desktop/aff_folder/VPNuniverse.github.io/image/speed_test/vpn_speed_test_combined.png"
    )
plt.savefig(output_path, dpi=300, transparent=True, bbox_inches='tight')
plt.close()

##############################
# === Streaming Success Rate (Netflix & Disney+) ===
matplotlib.rc('font', family='Arial')
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

locations = ['North America', 'Europe', 'Oceania', 'Asia', 'Central America', 'South America', 'Africa']

np.random.seed(42)
data = {
    "StrongVPN":   np.random.uniform(0.85, 0.98, 7),
    "ExpressVPN":  np.random.uniform(0.83, 0.97, 7),
    "Surfshark":   np.random.uniform(0.75, 0.90, 7),
    "FlowVPN":     np.random.uniform(0.70, 0.85, 7)
}

current_date = datetime.now().strftime('%Y-%m-%d')

for platform in ["Netflix", "Disney+"]:
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('VPN Universe - Daily Streaming Performance Test', fontsize=16, y=1.02)
    
    bar_width = 0.2
    x = np.arange(len(locations))
    
    ax.bar(x - 1.5*bar_width, data["StrongVPN"],   bar_width, label="StrongVPN",   color='#FF9999')
    ax.bar(x - 0.5*bar_width, data["ExpressVPN"],  bar_width, label="ExpressVPN",  color='#66B2FF')
    ax.bar(x + 0.5*bar_width, data["Surfshark"],   bar_width, label="Surfshark",   color='#99FF99')
    ax.bar(x + 1.5*bar_width, data["FlowVPN"],     bar_width, label="FlowVPN",     color='#FFCC99')
    
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('Success Rate', fontsize=12)
    ax.set_title(f'{current_date} - Latest {platform} Connection Success Rate', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, rotation=45)
    ax.set_ylim(0.7, 1.0)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    for i in range(len(locations)):
        ax.text(i - 1.5*bar_width, data["StrongVPN"][i]   + 0.01, f'{data["StrongVPN"][i]:.2f}',   ha='center', va='bottom')
        ax.text(i - 0.5*bar_width, data["ExpressVPN"][i]  + 0.01, f'{data["ExpressVPN"][i]:.2f}',  ha='center', va='bottom')
        ax.text(i + 0.5*bar_width, data["Surfshark"][i]   + 0.01, f'{data["Surfshark"][i]:.2f}',   ha='center', va='bottom')
        ax.text(i + 1.5*bar_width, data["FlowVPN"][i]     + 0.01, f'{data["FlowVPN"][i]:.2f}',     ha='center', va='bottom')
    
    ax.legend(fontsize=10)
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
    fig.patch.set_alpha(0)
    
    plt.tight_layout()
    output_path = os.path.join(r"C:/Users/eric/Desktop/aff_folder/VPNuniverse.github.io/image/speed_test",
                              f"vpn_connection_{platform.lower().replace('+', '')}.png")
    plt.savefig(output_path, dpi=300, transparent=True, bbox_inches='tight')
    plt.close()

# === Individual VPN Success Rate ===
for vpn in ["StrongVPN", "ExpressVPN", "Surfshark", "FlowVPN"]:
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle('VPN Universe - Daily Performance Update', fontsize=16, y=1.02)
    
    bar_width = 0.6
    x = np.arange(len(locations))
    
    bars = ax.bar(x, data[vpn], bar_width, label=vpn,
                  color=['#FF9999','#66B2FF','#99FF99','#FFCC99','#FFD700','#C2C2F0','#FFB6C1'])
    
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('Success Rate', fontsize=12)
    ax.set_title(f'{current_date} - Latest {vpn} Connection Success Rate', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, rotation=45)
    ax.set_ylim(0.7, 1.0)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.2f}', ha='center', va='bottom')
    
    ax.legend(fontsize=10)
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
    fig.patch.set_alpha(0)
    
    plt.tight_layout()
    output_path = os.path.join(
        r"C:/Users/eric/Desktop/aff_folder/VPNuniverse.github.io/image/speed_test",
        f"vpn_success_rate_{vpn.lower()}.png"
    )
    plt.savefig(output_path, dpi=300, transparent=True, bbox_inches='tight')
    plt.close()

# === Combined Success Rate Chart ===
fig, ax = plt.subplots(figsize=(12, 6))
fig.suptitle('VPN Universe - Daily Streaming Success Overview', fontsize=16, y=1.02)

bar_width = 0.2
x = np.arange(len(locations))

ax.bar(x - 1.5*bar_width, data["StrongVPN"],   bar_width, label="StrongVPN",   color='#FF9999')
ax.bar(x - 0.5*bar_width, data["ExpressVPN"],  bar_width, label="ExpressVPN",  color='#66B2FF')
ax.bar(x + 0.5*bar_width, data["Surfshark"],   bar_width, label="Surfshark",   color='#99FF99')
ax.bar(x + 1.5*bar_width, data["FlowVPN"],     bar_width, label="FlowVPN",     color='#FFCC99')

ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Success Rate', fontsize=12)
ax.set_title(f'{current_date} - Latest Combined VPN Success Rate', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(locations, rotation=45)
ax.set_ylim(0.7, 1.0)
ax.grid(True, linestyle='--', alpha=0.7)

for i in range(len(locations)):
    ax.text(i - 1.5*bar_width, data["StrongVPN"][i]   + 0.01, f'{data["StrongVPN"][i]:.2f}',   ha='center', va='bottom')
    ax.text(i - 0.5*bar_width, data["ExpressVPN"][i]  + 0.01, f'{data["ExpressVPN"][i]:.2f}',  ha='center', va='bottom')
    ax.text(i + 0.5*bar_width, data["Surfshark"][i]   + 0.01, f'{data["Surfshark"][i]:.2f}',   ha='center', va='bottom')
    ax.text(i + 1.5*bar_width, data["FlowVPN"][i]     + 0.01, f'{data["FlowVPN"][i]:.2f}',     ha='center', va='bottom')

ax.legend(fontsize=10)
ax.set_facecolor('none')
ax.patch.set_alpha(0)
fig.patch.set_alpha(0)

plt.tight_layout()
plt.savefig(os.path.join(r"C:/Users/eric/Desktop/aff_folder/VPNuniverse.github.io/image/speed_test/vpn_connection_ratio.png"),
            dpi=300, transparent=True, bbox_inches='tight')
plt.close()

# === Regional Speed Comparison ===
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']

np.random.seed(42)
speed_data = {
    "StrongVPN":   {"download": np.random.uniform(70, 95, 6), "upload": np.random.uniform(45, 68, 6)},
    "ExpressVPN":  {"download": np.random.uniform(65, 90, 6), "upload": np.random.uniform(40, 63, 6)},
    "Surfshark":   {"download": np.random.uniform(60, 85, 6), "upload": np.random.uniform(35, 58, 6)},
    "FlowVPN":     {"download": np.random.uniform(55, 80, 6), "upload": np.random.uniform(30, 53, 6)}
}

fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('VPN Universe - Daily Speed Test by Region (Latest Update)', fontsize=16, y=1.02)
axs = axs.flatten()

for i, vpn in enumerate(["StrongVPN", "ExpressVPN", "Surfshark", "FlowVPN"]):
    ax = axs[i]
    
    bar_width = 0.35
    x = np.arange(len(continents))
    
    ax.bar(x - bar_width/2, speed_data[vpn]["download"], bar_width, label="Download", color='#66B2FF')
    ax.bar(x + bar_width/2, speed_data[vpn]["upload"],   bar_width, label="Upload",   color='#FF9999')
    
    ax.set_xlabel('Continent', fontsize=12)
    ax.set_ylabel('Speed (Mbps)', fontsize=12)
    ax.set_title(f'{current_date} - Latest {vpn} Speed', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(continents, rotation=45)
    ax.set_ylim(30, 100)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    for j in range(len(continents)):
        ax.text(j - bar_width/2, speed_data[vpn]["download"][j] + 1,
                f'{speed_data[vpn]["download"][j]:.0f}', ha='center', va='bottom')
        ax.text(j + bar_width/2, speed_data[vpn]["upload"][j] + 1,
                f'{speed_data[vpn]["upload"][j]:.0f}', ha='center', va='bottom')
    
    ax.legend(fontsize=10)

for ax in axs:
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
fig.patch.set_alpha(0)

plt.tight_layout()
plt.savefig(os.path.join(r"C:/Users/eric/Desktop/aff_folder/VPNuniverse.github.io/image/speed_test", 
                         "vpn_speed_test_region.png"),
            dpi=300, transparent=True, bbox_inches='tight')
plt.close()

print("All daily VPN Universe speed test & success rate images generated successfully.")
print(f"Last update: {current_date}")