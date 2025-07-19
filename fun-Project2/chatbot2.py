import streamlit as st
import requests
import json
from datetime import datetime
from PIL import Image

# ===========================
# SYSTEM MESSAGE CONFIGURATION
# ===========================
def get_system_message():
    """Return the system message that defines the AI assistant's personality"""
    user_info = st.session_state.get("user_info", {})
    nama_panggilan = user_info.get("nama_panggilan", "")
    job = user_info.get("job", "")
    
    # Personalisasi system message berdasarkan user info
    personal_context = f"Nama pengguna adalah {nama_panggilan}." if nama_panggilan else ""
    job_context = f" Pekerjaan/profesi mereka adalah {job}." if job else ""
    
    return {
        "role": "system",
        "content": f"""Kamu adalah asisten AI yang bertugas membantu menjawab pertanyaan, memberikan ide kreatif, serta memecahkan masalah pengguna secara sopan, jelas, dan profesional. {personal_context}{job_context} Panggil mereka dengan nama panggilan mereka dalam percakapan untuk menciptakan interaksi yang personal dan hangat. Gunakan bahasa yang ramah dan mudah dipahami. Tambahkan emote secara alami untuk menciptakan suasana hangat dan bersahabat. Jangan terburu-buru, dengarkan dengan baik, dan berikan respons yang relevan serta menenangkan. Jaga konsistensi nada bicara—tenang, suportif, dan humanis. Jika pengguna bingung atau tidak spesifik, bantu arahkan dengan pertanyaan klarifikasi. Jadilah teman digital yang bisa diandalkan, bukan sekadar mesin penjawab."""
    }

# ===========================
# LOGIN SYSTEM
# ===========================
def render_login_form():
    """Tampilkan form login untuk user baru"""
    st.markdown("""
    <div style="max-width: 500px; margin: 0 auto; padding: 2rem;">
        <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem; text-align: center;">
            <h1 style="color: white; font-size: 2.5rem; margin: 0;">🤖 Selamat Datang!</h1>
            <p style="color: #f0f0f0; font-size: 1.2rem; margin: 0.5rem 0 0 0;">Silakan perkenalkan diri Anda terlebih dahulu</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("login_form"):
            st.markdown("### 👋 Perkenalan")
            
            nama_lengkap = st.text_input(
                "Nama Lengkap *",
                placeholder="Contoh: Ismail bin Mail",
                help="Masukkan nama lengkap Anda"
            )
            
            nama_panggilan = st.text_input(
                "Nama Panggilan *",
                placeholder="Contoh: Mail atau Ucup",
                help="Nama yang ingin Anda gunakan dalam percakapan"
            )
            
            job = st.text_input(
                "Pekerjaan/Profesi (Opsional)",
                placeholder="Contoh: Mahasiswa, Developer, Teacher, dll",
                help="Informasi ini akan membantu AI memberikan respons yang lebih relevan"
            )
            
            st.markdown("---")
            
            col_a, col_b = st.columns(2)
            with col_a:
                submit = st.form_submit_button("🚀 Mulai Chat", type="primary", use_container_width=True)
            with col_b:
                if st.form_submit_button("ℹ️ Info", type="secondary", use_container_width=True):
                    st.info("""
                    **Mengapa perlu perkenalan?**
                    
                    Dengan mengetahui nama dan profesi Anda, AI dapat:
                    - 🎯 Memberikan respons yang lebih personal
                    - 💬 Menggunakan nama Anda dalam percakapan
                    - 🔧 Menyesuaikan jawaban sesuai bidang pekerjaan
                    - 🤝 Menciptakan pengalaman chat yang lebih hangat
                    """)
            
            if submit:
                if nama_lengkap.strip() and nama_panggilan.strip():
                    # Simpan informasi user ke session state
                    st.session_state.user_info = {
                        "nama_lengkap": nama_lengkap.strip(),
                        "nama_panggilan": nama_panggilan.strip(),
                        "job": job.strip() if job.strip() else None,
                        "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.session_state.is_logged_in = True
                    st.success(f"✅ Halo {nama_panggilan}! Selamat datang di Asisten Chatbot AI!")
                    st.rerun()
                else:
                    st.error("❌ Nama lengkap dan nama panggilan wajib diisi!")

def render_user_profile_sidebar():
    """Tampilkan profil user di sidebar"""
    if st.session_state.get("is_logged_in", False):
        user_info = st.session_state.get("user_info", {})
        
        st.markdown("### 👤 Profil Pengguna")
        st.markdown(f"""
        <div style="background: #2d3748; color: #e2e8f0; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border: 1px solid #4a5568;">
            <p><strong>📝 Nama:</strong> {user_info.get('nama_lengkap', 'N/A')}</p>
            <p><strong>🏷️ Panggilan:</strong> {user_info.get('nama_panggilan', 'N/A')}</p>
            <p><strong>💼 Profesi:</strong> {user_info.get('job', 'Tidak disebutkan')}</p>
            <p><small>🕐 Login: {user_info.get('login_time', 'N/A')}</small></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Ganti User", type="secondary", use_container_width=True):
            # Reset session untuk login ulang
            for key in ["user_info", "is_logged_in", "messages"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
        
        st.markdown("---")

# ===========================
# PAGE CONFIGURATION
# ===========================
def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="Fael Chatbot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# ===========================
# STYLING AND CSS
# ===========================
def load_custom_css():
    """Load custom CSS styling for the application"""
    st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .main-header h1 {
            color: white;
            font-size: 2.5rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .main-header p {
            color: #f0f0f0;
            font-size: 1.2rem;
            margin: 0.5rem 0 0 0;
        }
        
        .chat-container {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            min-height: 400px;
            margin-bottom: 1rem;
        }
        
        .stats-container {
            background: white;
            border-radius: 10px;
            padding: 1rem;
            border: 1px solid #e0e0e0;
            margin-bottom: 1rem;
        }
        
        .stChatMessage {
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        
        .sidebar-info {
            background: #2d3748;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border: 1px solid #4a5568;
        }
        
        .sidebar-info h4 {
            color: #63b3ed;
            margin-bottom: 0.5rem;
        }
        
        .sidebar-info p {
            color: #cbd5e0;
            margin-bottom: 0.3rem;
        }
        
        .sidebar-info ul {
            color: #cbd5e0;
        }
        
        .sidebar-info li {
            margin-bottom: 0.3rem;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 0.75rem;
            border-radius: 5px;
            border: 1px solid #c3e6cb;
            margin: 0.5rem 0;
        }
        
        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 0.75rem;
            border-radius: 5px;
            border: 1px solid #f5c6cb;
            margin: 0.5rem 0;
        }
        
        .system-message-info {
            background: #e8f4fd;
            color: #1565c0;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #2196f3;
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

# ===========================
# UI COMPONENTS
# ===========================
def render_header():
    """Render the main header section"""
    user_info = st.session_state.get("user_info", {})
    nama_panggilan = user_info.get("nama_panggilan", "")
    
    st.markdown(f"""
    <div class="main-header">
        <h1>🤖 Asisten Chatbot AI</h1>
        <p>Didukung oleh berbagai model AI via OpenRouter</p>
    </div>
    """, unsafe_allow_html=True)

def render_welcome_message():
    """Tampilkan pesan selamat datang untuk pengguna baru"""
    if not st.session_state.messages:
        user_info = st.session_state.get("user_info", {})
        nama_panggilan = user_info.get("nama_panggilan", "")
        job = user_info.get("job", "")
        
        with st.chat_message("assistant", avatar="🤖"):
            welcome_msg = f"""
👋 Halo {nama_panggilan if nama_panggilan else ""}!
            
Senang berkenalan dengan Anda{f", seorang {job}" if job else ""}. 
Saya adalah Asisten AI yang diprogram untuk membantu, mendampingi, dan mempermudah aktivitas Anda dalam berbagai hal.

Saya dapat menjawab pertanyaan, menghasilkan ide, memberi solusi, dan menjadi teman berpikir Anda kapan pun dibutuhkan.

Dengan mengetahui nama dan{f" profesi" if job else ""} Anda, saya bisa memberikan respons yang lebih personal dan sesuai dengan kebutuhan Anda.

Silakan ajukan pertanyaan Anda, {nama_panggilan if nama_panggilan else ""}!
Saya siap menemani Kamu 😊
---
*💡 Chatbot ini dibuat oleh **M. Hanif** sebagai project dari AI-Python Bootcamp*
            """
            st.markdown(welcome_msg)

def render_chat_history():
    """Tampilkan riwayat pesan chat"""
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])

def render_footer():
    """Tampilkan footer aplikasi"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🚀 Dibuat oleh <strong>M. Hanif</strong> | Chatbot ini Didukung oleh Berbagai Model AI via OpenRouter</p>
        <p><small>🎓 Project dari AI-Python Bootcamp | Student ID: REAPYTHON3WVTDF</small></p>
    </div>
    """, unsafe_allow_html=True)

# ===========================
# API FUNCTIONS
# ===========================
def get_api_key():
    """Mendapatkan API key dari input pengguna atau secrets"""
    # Prioritas: input pengguna > secrets
    if "api_key" in st.session_state and st.session_state.api_key:
        return st.session_state.api_key
    
    try:
        return st.secrets["openrouter_api_key"]
    except KeyError:
        return None

def prepare_messages_with_system(chat_history):
    """Prepare messages array with system message at the beginning"""
    # Start with system message
    messages = [get_system_message()]
    
    # Add chat history (excluding any existing system messages)
    for message in chat_history:
        if message["role"] != "system":
            messages.append(message)
    
    return messages

def get_ai_response(user_input, chat_history):
    """Mendapatkan respons AI dari OpenRouter API"""
    api_key = get_api_key()
    if not api_key:
        st.error("🔑 API key tidak ditemukan. Silakan masukkan API key di sidebar.")
        return None
    
    # Ambil model yang dipilih dari session state
    selected_model = st.session_state.get("selected_model", "mistralai/mistral-7b-instruct:free")
    
    # Prepare messages with system message
    messages = prepare_messages_with_system(chat_history)
    # Add current user input
    messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            data=json.dumps({
                "model": selected_model,
                "messages": messages,
                "max_tokens": st.session_state.get("max_tokens", 1000),
                "temperature": st.session_state.get("temperature", 0.7),
            })
        )

        response.raise_for_status() 
        ai_message = response.json()["choices"][0]["message"]["content"]
        return ai_message
        
    except requests.exceptions.RequestException as e:
        st.error(f"🌐 Terjadi kesalahan jaringan: {e}")
        return None
    except Exception as e:
        st.error(f"⚠️ Terjadi kesalahan yang tidak terduga: {e}")
        return None

# ===========================
# SESSION STATE MANAGEMENT
# ===========================
def initialize_session_state():
    """Inisialisasi variabel session state"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "mistralai/mistral-7b-instruct:free"
    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 1000
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
    if "user_info" not in st.session_state:
        st.session_state.user_info = {}

def clear_chat_history():
    """Hapus riwayat chat dari session state"""
    st.session_state.messages = []
    st.rerun()

# ===========================
# MODEL CONFIGURATIONS
# ===========================
def get_available_models():
    """Daftar model AI yang tersedia"""
    return {
        # Gratis
        "mistralai/mistral-7b-instruct:free": "Mistral 7B Instruct (Gratis)",
        "google/gemma-7b-it:free": "Google Gemma 7B IT (Gratis)",
        "meta-llama/llama-3-8b-instruct:free": "Llama 3 8B Instruct (Gratis)",
        "microsoft/phi-3-mini-128k-instruct:free": "Phi-3 Mini 128K (Gratis)",
        
        # Premium - OpenAI
        "openai/gpt-4o": "GPT-4o (OpenAI)",
        "openai/gpt-4o-mini": "GPT-4o Mini (OpenAI)",
        "openai/gpt-3.5-turbo": "GPT-3.5 Turbo (OpenAI)",
        
        # Premium - Anthropic
        "anthropic/claude-3.5-sonnet": "Claude 3.5 Sonnet (Anthropic)",
        "anthropic/claude-3-haiku": "Claude 3 Haiku (Anthropic)",
        
        # Premium - Google
        "google/gemini-pro": "Gemini Pro (Google)",
        "google/gemini-pro-vision": "Gemini Pro Vision (Google)",
        
        # Premium - Meta
        "meta-llama/llama-3-70b-instruct": "Llama 3 70B Instruct (Meta)",
        "meta-llama/llama-3-405b-instruct": "Llama 3 405B Instruct (Meta)",
        
        # Premium - Mistral
        "mistralai/mistral-large": "Mistral Large (Mistral AI)",
        "mistralai/mistral-medium": "Mistral Medium (Mistral AI)",
        "mistralai/codestral": "Codestral (Mistral AI)",
    }

# ===========================
# CHAT FUNCTIONALITY
# ===========================
def handle_user_input():
    """Tangani input pengguna dan buat respons AI"""
    if prompt := st.chat_input("💬 Ketik pesan Anda di sini...", key="chat_input"):
        # Tambah pesan pengguna ke riwayat chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Tampilkan pesan pengguna
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Dapatkan dan tampilkan respons AI
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("🧠 Sedang berpikir..."):
                ai_response = get_ai_response(prompt, st.session_state.messages)
                if ai_response:
                    st.markdown(ai_response)
                    # Tambah respons AI ke riwayat chat
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                    
                    # Feedback sukses
                    st.success("✅ Respons berhasil dibuat!")
                else:
                    st.error("❌ Gagal mendapatkan respons dari AI. Silakan coba lagi.")

# ===========================
# STATISTICS FUNCTIONS
# ===========================
def get_chat_statistics():
    """Hitung dan kembalikan statistik chat"""
    if "messages" not in st.session_state:
        return {"total": 0, "user": 0, "ai": 0}
    
    total_messages = len(st.session_state.messages)
    user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
    ai_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    
    return {
        "total": total_messages,
        "user": user_messages,
        "ai": ai_messages
    }

# ===========================
# MAIN APPLICATION
# ===========================
def main():
    """Fungsi aplikasi utama"""
    # Inisialisasi aplikasi
    configure_page()
    load_custom_css()
    initialize_session_state()
    
    # Cek status login
    if not st.session_state.get("is_logged_in", False):
        render_login_form()
        return
    
    # Tampilkan konten utama jika sudah login
    render_header()
    render_welcome_message()
    render_chat_history()
    handle_user_input()
    render_footer()

# ===========================
# SIDEBAR CONFIGURATION
# ===========================
def render_sidebar():
    """Tampilkan sidebar dengan pengaturan dan informasi"""
    # Hanya tampilkan sidebar jika sudah login
    if not st.session_state.get("is_logged_in", False):
        return
        
    with st.sidebar:
        # Developer Identity Section - PINDAH KE ATAS
        st.markdown("### 👨‍💻 ABOUT DEVELOPER")
        try:
            image = Image.open("fael.jpg")
            st.image(image, width=200)
        except FileNotFoundError:
            st.info("📷 Foto profil tidak ditemukan (fael.jpg)")
        
        st.write("**Nama** : M. Hanif")
        st.write("**Student ID** : REAPYTHON3WVTDF")
        st.write("**Class** : AI-python Bootcamp")
        st.write("_________________________________")
        
        # User Profile Section - SEKARANG DI BAWAH DEVELOPER
        render_user_profile_sidebar()
        
        # System Message Information
        with st.expander("🎯 System Message Configuration", expanded=False):
            st.markdown("""
            <div class="system-message-info">
                <strong>🤖 Kepribadian AI:</strong><br>
                AI ini dirancang dengan kepribadian yang ramah, suportif, dan humanis. 
                Menggunakan bahasa Indonesia yang hangat dengan emoji natural untuk 
                menciptakan pengalaman chat yang menyenangkan dan membantu! 😊
                
                <br><br><strong>🎯 Personalisasi:</strong><br>
                AI akan menggunakan nama panggilan Anda dalam percakapan dan 
                menyesuaikan respons berdasarkan profesi yang Anda berikan.
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 🎛️ Pengaturan")
        
        # API Key Input
        st.markdown("#### 🔑 API Key OpenRouter")
        api_key_input = st.text_input(
            "Masukkan API Key Anda:",
            type="password",
            value=st.session_state.api_key,
            placeholder="sk-or-..."
        )
        if api_key_input != st.session_state.api_key:
            st.session_state.api_key = api_key_input
        
        if not st.session_state.api_key:
            st.warning("⚠️ Silakan masukkan API Key untuk mulai menggunakan chatbot.")
            st.info("💡 Dapatkan API Key gratis di: https://openrouter.ai/keys")
        else:
            st.success("✅ API Key telah diatur!")
        
        st.markdown("---")
        
        # Model Selection
        st.markdown("#### 🤖 Pilih Model AI")
        available_models = get_available_models()
        selected_model = st.selectbox(
            "Model:",
            options=list(available_models.keys()),
            format_func=lambda x: available_models[x],
            index=list(available_models.keys()).index(st.session_state.selected_model)
        )
        if selected_model != st.session_state.selected_model:
            st.session_state.selected_model = selected_model
        
        st.markdown("---")
        
        # Parameters
        st.markdown("#### ⚙️ Parameter Model")
        max_tokens = st.slider(
            "Max Tokens:",
            min_value=100,
            max_value=4000,
            value=st.session_state.max_tokens,
            step=100
        )
        if max_tokens != st.session_state.max_tokens:
            st.session_state.max_tokens = max_tokens
        
        temperature = st.slider(
            "Temperature (Kreativitas):",
            min_value=0.0,
            max_value=2.0,
            value=st.session_state.temperature,
            step=0.1
        )
        if temperature != st.session_state.temperature:
            st.session_state.temperature = temperature
        
        st.markdown("---")
        
        # Model information
        st.markdown("""
        <div class="sidebar-info">
            <h4>🧠 Informasi Model Aktif</h4>
            <p><strong>Model:</strong> {}</p>
            <p><strong>Max Tokens:</strong> {}</p>
            <p><strong>Temperature:</strong> {}</p>
        </div>
        """.format(
            available_models.get(st.session_state.selected_model, "Unknown"),
            st.session_state.max_tokens,
            st.session_state.temperature
        ), unsafe_allow_html=True)
        
        # Chat statistics
        stats = get_chat_statistics()
        if stats["total"] > 0:
            st.markdown(f"""
            <div class="sidebar-info">
                <h4>📊 Statistik Chat</h4>
                <p><strong>Total Pesan:</strong> {stats['total']}</p>
                <p><strong>Pesan Anda:</strong> {stats['user']}</p>
                <p><strong>Respons AI:</strong> {stats['ai']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Clear chat button
        if st.button("🗑️ Hapus Riwayat Chat", type="secondary", use_container_width=True):
            clear_chat_history()
        
        # Tips section
        user_info = st.session_state.get("user_info", {})
        nama_panggilan = user_info.get("nama_panggilan", "Anda")
        
        st.markdown(f"""
        <div class="sidebar-info">
            <h4>💡 Tips Penggunaan untuk {nama_panggilan}</h4>
            <ul>
                <li>Sampaikan pertanyaan dengan jelas dan spesifik</li>
                <li>Gunakan bahasa yang sederhana dan mudah dipahami</li>
                <li>Jangan ragu mencoba berbagai topik</li>
                <li>AI akan memanggil Anda dengan nama panggilan dalam percakapan</li>
                <li>AI telah disesuaikan dengan profil Anda untuk respons yang lebih relevan</li>
                <li>Perlu diingat, versi gratis memiliki batasan tertentu</li>
                <li>AI ini dirancang untuk bersikap ramah dan suportif 😊</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ===========================
# APPLICATION ENTRY POINT
# ===========================
if __name__ == "__main__":
    main()
    configure_page()
    load_custom_css()
    render_sidebar()  # Sidebar ditampilkan di bagian bawah sesuai permintaan
