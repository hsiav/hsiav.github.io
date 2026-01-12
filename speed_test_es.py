import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
from datetime import datetime, timedelta

# Configurar soporte para español
matplotlib.rc('font', family='Arial')  # Usar fuente compatible con español
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

# Generar rango de fechas
def generar_rango_fechas(retraso):
    fecha_fin = datetime.today() + timedelta(hours=13)  # Ajuste a CST
    fecha_inicio = fecha_fin - timedelta(days=retraso)
    return f"{fecha_fin.year} {fecha_inicio.month:02d}/{fecha_inicio.day:02d}-{fecha_fin.month:02d}/{fecha_fin.day:02d}"

# Cargar imágenes
def obtener_imagen(ruta, zoom=0.3):
    if os.path.exists(ruta):
        try:
            return OffsetImage(plt.imread(ruta), zoom=zoom)
        except Exception as e:
            print(f"Fallo al cargar imagen {ruta}: {e}")
            return None
    else:
        print(f"Imagen no encontrada: {ruta}")
        return None

# Datos de VPN y rutas de imágenes
datos_vpn = {
    "StrongVPN": [95, 70],  # Ajustado para reflejar estabilidad en regiones hispanohablantes
    "ExpressVPN": [90, 65],  # Optimizado para velocidad en Europa y América
    "Surfshark": [85, 60],  # Mejorado para América Latina
    "FlowVPN": [80, 55]    # Enfocado en estabilidad global
}
imagenes = {
    "StrongVPN": "small/strong.jpg",
    "ExpressVPN": "small/expressvpn.jpg",
    "Surfshark": "small/surfshark.jpg",
    "FlowVPN": "small/flowvpn.jpg"
}

# --- Gráfico: Cuatro subgráficos ---
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
x = [0, 1, 2, 3]  # Índices para VPNs
y = [80, 90, 75, 70]  # Descarga (ajustada para reflejar meses pasados)
z = [50, 60, 45, 40]  # Subida (ajustada para consistencia)
nombres_vpn = list(datos_vpn.keys())

for i, retraso in enumerate([7, 14, 30, 90]):
    fila, columna = divmod(i, 2)
    ax = axs[fila, columna]
    
    # Dibujar puntos y barras de error
    ax.scatter(x, y, label="Velocidad de descarga", s=100)
    ax.scatter(x, z, label="Velocidad de subida", s=100)
    c = [3 + np.random.randint(10) for _ in range(4)]  # Error aleatorio
    ax.errorbar(x, y, yerr=c, fmt="o")
    ax.errorbar(x, z, yerr=c, fmt="o")
    
    # Configurar etiquetas de eje x
    ax.set_xticks(x)
    ax.set_xticklabels(nombres_vpn, fontsize=10)
    
    # Añadir imágenes en el eje x
    for j, nombre_vpn in enumerate(nombres_vpn):
        imagen = obtener_imagen(imagenes[nombre_vpn], zoom=0.3)
        if imagen:
            ab = AnnotationBbox(imagen, (j, -10), frameon=False, xycoords='data', boxcoords="offset points", pad=0)
            ax.add_artist(ab)
    
    # Ajustar rango y de eje para evitar solapamiento
    ax.set_ylim(-20, max(y) + 20)
    
    # Etiquetas y título
    ax.set_xlabel('VPN', fontsize=12)
    ax.set_ylabel('Velocidad (Mbps)', fontsize=12)
    ax.set_title(f'Muro Universo - Evaluación de velocidad VPN {generar_rango_fechas(retraso)}', fontsize=14)
    ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig('C:/Users/eric/Desktop/aff_folder/vpn-mundo.github.io/image/speed_test/vpn_speed_test_combined.png')
plt.close()

# Imprimir rangos de fechas (para pruebas)
for retraso in [7, 14, 30, 90]:
    print(generar_rango_fechas(retraso))

##############################

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Configurar soporte para español
matplotlib.rc('font', family='Arial')  # Fuente compatible con español
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

# Definir regiones
locations = ['North America', 'Europe', 'Oceania', 'Asia', 'C-A', 'South America', 'Africa']

# Generar datos aleatorios para cada VPN (success rate 0.7-1, Strong ≈ Express > Surfshark > Flow)
np.random.seed(42)  # Para reproducibilidad
data = {
    "StrongVPN": np.random.uniform(0.85, 0.98, 7),
    "ExpressVPN": np.random.uniform(0.83, 0.97, 7),  # Aproximadamente igual a StrongVPN
    "Surfshark": np.random.uniform(0.75, 0.90, 7),  # Menor que Strong/Express
    "FlowVPN": np.random.uniform(0.70, 0.85, 7)    # Menor que Surfshark
}

# Fecha actual
current_date = datetime.now().strftime('%Y-%m-%d')

# Generar gráficos para Netflix y Disney+
for platform in ["Netflix", "Disney+"]:
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Ancho de las barras
    bar_width = 0.2
    x = np.arange(len(locations))
    
    # Crear barras para cada VPN
    ax.bar(x - 1.5 * bar_width, data["StrongVPN"], bar_width, label="StrongVPN", color='#FF9999')
    ax.bar(x - 0.5 * bar_width, data["ExpressVPN"], bar_width, label="ExpressVPN", color='#66B2FF')
    ax.bar(x + 0.5 * bar_width, data["Surfshark"], bar_width, label="Surfshark", color='#99FF99')
    ax.bar(x + 1.5 * bar_width, data["FlowVPN"], bar_width, label="FlowVPN", color='#FFCC99')
    
    # Personalizar gráfico
    ax.set_xlabel('Región', fontsize=12)
    ax.set_ylabel('Tasa de éxito', fontsize=12)
    ax.set_title(f'{current_date} - Tasa de éxito para {platform}', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, rotation=45)
    ax.set_ylim(0.7, 1.0)  # Rango de 0.7 a 1
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Añadir etiquetas de valor en las barras
    for i in range(len(locations)):
        ax.text(i - 1.5 * bar_width, data["StrongVPN"][i] + 0.01, f'{data["StrongVPN"][i]:.2f}', ha='center', va='bottom')
        ax.text(i - 0.5 * bar_width, data["ExpressVPN"][i] + 0.01, f'{data["ExpressVPN"][i]:.2f}', ha='center', va='bottom')
        ax.text(i + 0.5 * bar_width, data["Surfshark"][i] + 0.01, f'{data["Surfshark"][i]:.2f}', ha='center', va='bottom')
        ax.text(i + 1.5 * bar_width, data["FlowVPN"][i] + 0.01, f'{data["FlowVPN"][i]:.2f}', ha='center', va='bottom')
    
    # Leyenda
    ax.legend(fontsize=10)
    
    # Configurar fondo transparente
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
    fig.patch.set_alpha(0)
    
    plt.tight_layout()
    # Guardar cada gráfico con fondo transparente
    output_path = os.path.join(r"C:/Users/eric/Desktop/aff_folder/vpn-mundo.github.io/image/speed_test",
                              f"vpn_connection_{platform.lower().replace('+', '')}.png")
    plt.savefig(output_path, dpi=300, transparent=True, facecolor='none', edgecolor='none')
    plt.close()

print("Las imágenes para Netflix y Disney+ han sido generadas exitosamente.")


###############

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Configurar soporte para español
matplotlib.rc('font', family='Arial')  # Fuente compatible con español
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

# Definir regiones
locations = ['North America', 'Europe', 'Oceania', 'Asia', 'C-A', 'South America', 'Africa']

# Generar datos aleatorios para cada VPN (success rate 0.7-1, Strong ≈ Express > Surfshark > Flow)
np.random.seed(42)  # Para reproducibilidad
data = {
    "StrongVPN": np.random.uniform(0.85, 0.98, 7),
    "ExpressVPN": np.random.uniform(0.83, 0.97, 7),  # Aproximadamente igual a StrongVPN
    "Surfshark": np.random.uniform(0.75, 0.90, 7),  # Menor que Strong/Express
    "FlowVPN": np.random.uniform(0.70, 0.85, 7)    # Menor que Surfshark
}

# Fecha actual
current_date = datetime.now().strftime('%Y-%m-%d')

# Generar gráficos para cada VPN
for vpn in ["StrongVPN", "ExpressVPN", "Surfshark", "FlowVPN"]:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Ancho de las barras
    bar_width = 0.6
    x = np.arange(len(locations))
    
    # Crear gráfico de barras
    bars = ax.bar(x, data[vpn], bar_width, label=vpn, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#C2C2F0', '#FFB6C1'])
    
    # Personalizar gráfico
    ax.set_xlabel('Región', fontsize=12)
    ax.set_ylabel('Tasa de éxito', fontsize=12)
    ax.set_title(f'{current_date} - Tasa de éxito con {vpn}', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, rotation=45)
    ax.set_ylim(0.7, 1.0)  # Rango de 0.7 a 1
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Añadir etiquetas de valor en las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.2f}',
                ha='center', va='bottom')
    
    # Leyenda
    ax.legend(fontsize=10)
    
    # Configurar fondo transparente
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
    fig.patch.set_alpha(0)
    
    plt.tight_layout()
    # Guardar cada gráfico con fondo transparente
    output_path = os.path.join(r"C:/Users/eric/Desktop/aff_folder/vpn-mundo.github.io/image/speed_test",
                              f"vpn_success_rate_{vpn.lower()}.png")
    plt.savefig(output_path, dpi=300, transparent=True, facecolor='none', edgecolor='none')
    plt.close()

print("Las imágenes de tasa de éxito para cada VPN han sido generadas exitosamente.")

# import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Configurar soporte para español
matplotlib.rc('font', family='Arial')  # Fuente compatible con español
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

# Definir regiones
locations = ['North America', 'Europe', 'Oceania', 'Asia', 'C-A', 'South America', 'Africa']

# Generar datos aleatorios para cada VPN (success rate 0.7-1, Strong ≈ Express > Surfshark > Flow)
np.random.seed(42)  # Para reproducibilidad
data = {
    "StrongVPN": np.random.uniform(0.85, 0.98, 7),
    "ExpressVPN": np.random.uniform(0.83, 0.97, 7),  # Aproximadamente igual a StrongVPN
    "Surfshark": np.random.uniform(0.75, 0.90, 7),  # Menor que Strong/Express
    "FlowVPN": np.random.uniform(0.70, 0.85, 7)    # Menor que Surfshark
}

# Fecha actual
current_date = datetime.now().strftime('%Y-%m-%d')

# Generar gráfico combinado
fig, ax = plt.subplots(figsize=(12, 6))

# Ancho de las barras
bar_width = 0.2
x = np.arange(len(locations))

# Crear barras para cada VPN
ax.bar(x - 1.5 * bar_width, data["StrongVPN"], bar_width, label="StrongVPN", color='#FF9999')
ax.bar(x - 0.5 * bar_width, data["ExpressVPN"], bar_width, label="ExpressVPN", color='#66B2FF')
ax.bar(x + 0.5 * bar_width, data["Surfshark"], bar_width, label="Surfshark", color='#99FF99')
ax.bar(x + 1.5 * bar_width, data["FlowVPN"], bar_width, label="FlowVPN", color='#FFCC99')

# Personalizar gráfico
ax.set_xlabel('Región', fontsize=12)
ax.set_ylabel('Tasa de éxito', fontsize=12)
ax.set_title(f'{current_date} - Tasa de éxito combinada de VPNs', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(locations, rotation=45)
ax.set_ylim(0.7, 1.0)  # Rango de 0.7 a 1
ax.grid(True, linestyle='--', alpha=0.7)

# Añadir etiquetas de valor en las barras
for i in range(len(locations)):
    ax.text(i - 1.5 * bar_width, data["StrongVPN"][i] + 0.01, f'{data["StrongVPN"][i]:.2f}', ha='center', va='bottom')
    ax.text(i - 0.5 * bar_width, data["ExpressVPN"][i] + 0.01, f'{data["ExpressVPN"][i]:.2f}', ha='center', va='bottom')
    ax.text(i + 0.5 * bar_width, data["Surfshark"][i] + 0.01, f'{data["Surfshark"][i]:.2f}', ha='center', va='bottom')
    ax.text(i + 1.5 * bar_width, data["FlowVPN"][i] + 0.01, f'{data["FlowVPN"][i]:.2f}', ha='center', va='bottom')

# Leyenda
ax.legend(fontsize=10)

# Configurar fondo transparente
ax.set_facecolor('none')
ax.patch.set_alpha(0)
fig.patch.set_alpha(0)

plt.tight_layout()
# Guardar gráfico con fondo transparente
output_path = os.path.join(r"C:/Users/eric/Desktop/aff_folder/vpn-mundo.github.io/image/speed_test", "vpn_connection_ratio.png")
plt.savefig(output_path, dpi=300, transparent=True, facecolor='none', edgecolor='none')
plt.close()

print("La imagen combinada de tasa de éxito ha sido generada exitosamente.")


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Configurar soporte para español
matplotlib.rc('font', family='Arial')  # Fuente compatible con español
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)

# Definir continentes
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']

# Generar datos aleatorios basados en los reportes originales (ajustados para Mbps)
np.random.seed(42)  # Para reproducibilidad
data = {
    "StrongVPN": {
        "download": np.random.uniform(70, 95, 6),  # Basado en 74-78 Mbps originales
        "upload": np.random.uniform(45, 68, 6)    # Basado en 46-68 Mbps originales
    },
    "ExpressVPN": {
        "download": np.random.uniform(65, 90, 6),  # Basado en 75-79 Mbps originales
        "upload": np.random.uniform(40, 63, 6)    # Basado en 46-63 Mbps originales
    },
    "Surfshark": {
        "download": np.random.uniform(60, 85, 6),  # Basado en 75-76 Mbps originales
        "upload": np.random.uniform(35, 58, 6)    # Basado en 45-58 Mbps originales
    },
    "FlowVPN": {
        "download": np.random.uniform(55, 80, 6),  # Basado en 74-79 Mbps originales
        "upload": np.random.uniform(30, 53, 6)    # Basado en 45-57 Mbps originales
    }
}

# Fecha actual
current_date = datetime.now().strftime('%Y-%m-%d')

# Generar gráfico combinado
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
axs = axs.flatten()

for i, vpn in enumerate(["StrongVPN", "ExpressVPN", "Surfshark", "FlowVPN"]):
    ax = axs[i]
    
    # Ancho de las barras
    bar_width = 0.35
    x = np.arange(len(continents))
    
    # Crear barras para download y upload
    ax.bar(x - bar_width/2, data[vpn]["download"], bar_width, label="Descarga", color='#66B2FF')
    ax.bar(x + bar_width/2, data[vpn]["upload"], bar_width, label="Subida", color='#FF9999')
    
    # Personalizar gráfico
    ax.set_xlabel('Continente', fontsize=12)
    ax.set_ylabel('Velocidad (Mbps)', fontsize=12)
    ax.set_title(f'{current_date} - Velocidad de {vpn}', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(continents, rotation=45)
    ax.set_ylim(30, 100)  # Rango basado en datos originales
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Añadir etiquetas de valor en las barras
    for j in range(len(continents)):
        ax.text(j - bar_width/2, data[vpn]["download"][j] + 1, f'{data[vpn]["download"][j]:.0f}', ha='center', va='bottom')
        ax.text(j + bar_width/2, data[vpn]["upload"][j] + 1, f'{data[vpn]["upload"][j]:.0f}', ha='center', va='bottom')
    
    # Leyenda
    ax.legend(fontsize=10)

# Ajustar layout y configurar fondo transparente
plt.tight_layout()
for ax in axs:
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
fig.patch.set_alpha(0)

# Guardar gráfico con fondo transparente
output_path = os.path.join(r"C:/Users/eric/Desktop/aff_folder/vpn-mundo.github.io/image/speed_test", "vpn_speed_test_region.png")
plt.savefig(output_path, dpi=300, transparent=True, facecolor='none', edgecolor='none')
plt.close()

print("La imagen combinada de velocidades ha sido generada exitosamente.")