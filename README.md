# 🤖 Asisten Chatbot AI

Chatbot AI yang powerful dan user-friendly yang dibangun menggunakan Streamlit dan OpenRouter API. Mendukung berbagai model AI dari OpenAI, Anthropic, Google, Meta, dan Mistral dengan interface yang modern dan personalized.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Fitur Utama

### 🔐 Sistem Login Personal
- **User Authentication**: Login dengan nama lengkap dan nama panggilan
- **Profil Personal**: Simpan informasi profesi untuk personalisasi respons
- **Session Management**: Kelola sesi pengguna dengan aman

### 🤖 Multi-Model AI Support
- **Model Gratis**: Mistral 7B, Gemma 7B, Llama 3 8B, Phi-3 Mini
- **Model Premium**: GPT-4o, Claude 3.5 Sonnet, Gemini Pro, dan lainnya
- **15+ Model Tersedia**: Pilihan lengkap dari berbagai provider AI

### 🎨 Interface Modern
- **Responsive Design**: Tampilan yang menyesuaikan berbagai ukuran layar
- **Custom Styling**: Gradient background dan elemen UI yang menarik
- **Dark/Light Elements**: Kombinasi tema yang eye-friendly
- **Emoji Integration**: Penggunaan emoji yang natural untuk UX yang lebih menarik

### 🎯 Personalisasi Cerdas
- **Nama Personal**: AI menggunakan nama panggilan dalam percakapan
- **Context Awareness**: Mempertimbangkan profesi pengguna untuk respons yang relevan
- **System Message Dynamic**: Pesan sistem yang disesuaikan dengan profil pengguna

### ⚙️ Kontrol Parameter Advanced
- **Temperature Control**: Atur kreativitas respons AI (0.0 - 2.0)
- **Max Tokens**: Kontrol panjang respons (100 - 4000 tokens)
- **Model Selection**: Ganti model AI secara real-time

### 📊 Statistik & Monitoring
- **Chat Statistics**: Tracking jumlah pesan pengguna dan AI
- **Real-time Updates**: Statistik yang update secara otomatis
- **Session History**: Riwayat percakapan tersimpan selama sesi

## 🚀 Instalasi & Setup

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
```

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/chatbot-ai.git
cd chatbot-ai
```

### 2. Install Dependencies
```bash
pip install streamlit requests pillow python-dotenv
```

### 3. Setup API Key
Dapatkan API Key dari [OpenRouter](https://openrouter.ai/keys) dan:

**Option 1: Masukkan via Interface**
- Jalankan aplikasi dan masukkan API key di sidebar

**Option 2: Environment Variable**
```bash
# Buat file .env
echo "OPENROUTER_API_KEY=your-api-key-here" > .env
```

**Option 3: Streamlit Secrets**
```toml
# .streamlit/secrets.toml
openrouter_api_key = "your-api-key-here"
```

### 4. Tambahkan Foto Profil (Opsional)
```bash
# Letakkan foto dengan nama 'fael.jpg' di root directory
cp your-photo.jpg fael.jpg
```

### 5. Jalankan Aplikasi
```bash
streamlit run chatbot2.py
```

## 🎯 Cara Penggunaan

### 1. **Login & Setup Profil**
- Masukkan nama lengkap dan nama panggilan
- Opsional: Tambahkan informasi profesi
- Klik "🚀 Mulai Chat"

### 2. **Konfigurasi Model**
- Pilih model AI di sidebar (gratis/premium)
- Atur parameter temperature dan max tokens
- Masukkan API key jika belum diatur

### 3. **Mulai Chatting**
- Ketik pertanyaan di chat input
- AI akan merespons dengan nama panggilan Anda
- Respons disesuaikan dengan profil dan konteks

### 4. **Kelola Sesi**
- Lihat statistik chat di sidebar
- Hapus riwayat chat jika diperlukan
- Ganti pengguna untuk login ulang

## 🏗️ Arsitektur Aplikasi

```
chatbot2.py
├── 🔐 Authentication System
│   ├── Login form dengan validasi
│   ├── User profile management
│   └── Session state handling
│
├── 🤖 AI Integration
│   ├── OpenRouter API integration
│   ├── Multi-model support
│   └── Dynamic system messages
│
├── 🎨 UI Components
│   ├── Modern CSS styling
│   ├── Responsive layout
│   └── Interactive sidebar
│
└── 📊 Features
    ├── Chat statistics
    ├── Message history
    └── Parameter controls
```

## 🌟 Kelebihan

### ✅ **Multi-Provider Support**
- Akses 15+ model AI dari berbagai provider
- Opsi gratis dan premium tersedia
- Switching model real-time tanpa restart

### ✅ **User Experience Unggul**
- Interface yang intuitif dan modern
- Personalisasi nama dalam percakapan
- Feedback visual yang jelas

### ✅ **Keamanan & Privacy**
- API key disimpan secara aman
- Session state management yang proper
- No data persistence di server

### ✅ **Customizable**
- Parameter AI yang dapat disesuaikan
- System message yang dinamis
- Tema dan styling yang dapat dimodifikasi

### ✅ **Developer Friendly**
- Code yang well-structured dan documented
- Modular architecture
- Easy to extend dan customize

## 🛠️ Teknologi yang Digunakan

| Teknologi | Versi | Fungsi |
|-----------|-------|--------|
| **Python** | 3.8+ | Backend logic |
| **Streamlit** | 1.28+ | Web framework |
| **OpenRouter API** | Latest | AI model access |
| **Requests** | Latest | HTTP client |
| **Pillow** | Latest | Image processing |
| **JSON** | Built-in | Data serialization |

## 📋 Model AI yang Didukung

### 🆓 **Model Gratis**
- Mistral 7B Instruct
- Google Gemma 7B IT
- Meta Llama 3 8B Instruct
- Microsoft Phi-3 Mini 128K

### 💎 **Model Premium**
- **OpenAI**: GPT-4o, GPT-4o Mini, GPT-3.5 Turbo
- **Anthropic**: Claude 3.5 Sonnet, Claude 3 Haiku
- **Google**: Gemini Pro, Gemini Pro Vision
- **Meta**: Llama 3 70B/405B Instruct
- **Mistral**: Mistral Large, Medium, Codestral

## 🔧 Konfigurasi Lanjutan

### Environment Variables
```bash
# .env file
OPENROUTER_API_KEY=your-api-key
STREAMLIT_THEME=light
STREAMLIT_SERVER_PORT=8501
```

### Streamlit Config
```toml
# .streamlit/config.toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#f0f0f0"
textColor = "#262730"
font = "sans serif"
```

## 📁 Struktur Proyek

```
chatbot-ai/
│
├── chatbot2.py              # Main application file
├── fael.jpg                 # Developer profile image (optional)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
├── .streamlit/
│   ├── config.toml         # Streamlit configuration
│   └── secrets.toml        # API keys (create this)
├── README.md               # This file
└── .gitignore             # Git ignore rules
```

## 🤝 Contributing

Kontribusi sangat welcome! Silakan:

1. **Fork** repository ini
2. **Create** feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** perubahan (`git commit -m 'Add some AmazingFeature'`)
4. **Push** ke branch (`git push origin feature/AmazingFeature`)
5. **Open** Pull Request

### 📝 Contribution Guidelines
- Ikuti PEP 8 untuk Python coding style
- Tambahkan docstring untuk function baru
- Update README jika menambah fitur baru
- Test aplikasi sebelum submit PR

## 🐛 Troubleshooting

### ❌ **API Key Error**
```bash
🔑 API key tidak ditemukan. Silakan masukkan API key di sidebar.
```
**Solusi**: Masukkan API key valid dari OpenRouter

### ❌ **Network Error**
```bash
🌐 Terjadi kesalahan jaringan
```
**Solusi**: Periksa koneksi internet dan status OpenRouter API

### ❌ **Model Not Available**
```bash
Model tidak tersedia atau limit tercapai
```
**Solusi**: Coba model lain atau upgrade ke plan berbayar

### ❌ **Import Error**
```bash
ModuleNotFoundError: No module named 'streamlit'
```
**Solusi**: Jalankan `pip install -r requirements.txt`

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Developer

**M. Hanif**
- **Student ID**: REAPYTHON3WVTDF
- **Program**: AI-Python Bootcamp
- **Email**: .
- **LinkedIn**: .
- **GitHub**: .

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Amazing web app framework
- [OpenRouter](https://openrouter.ai/) - Multi-model AI API platform  
- [AI-Python Bootcamp](https://bootcamp-link.com) - Learning program
- Open source community yang telah berkontribusi

## 🔮 Roadmap

### 🎯 **v2.0 (Planned)**
- [ ] Database integration untuk chat history
- [ ] Export chat ke PDF/TXT
- [ ] Voice input/output support
- [ ] Multi-language support

### 🎯 **v2.1 (Future)**
- [ ] File upload untuk document Q&A
- [ ] Image generation capabilities
- [ ] Plugin system untuk extensibility
- [ ] Team collaboration features

---

⭐ **Jika project ini membantu Anda, jangan lupa untuk memberikan star!** ⭐

![Footer](https://img.shields.io/badge/Made%20with-❤️-red.svg) ![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
