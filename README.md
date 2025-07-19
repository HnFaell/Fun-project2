# 🤖 Asisten Chatbot AI

Chatbot AI yang powerful dan user-friendly yang dibangun menggunakan Streamlit dan OpenRouter API. Mendukung berbagai model AI dari OpenAI, Anthropic, Google, Meta, dan Mistral dengan interface yang modern dan personalized.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)

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

## 👨‍💻 Developer

**M. Hanif**
- **Student ID**: REAPYTHON3WVTDF
- **Program**: AI-Python Bootcamp
- **Email**: .
- **LinkedIn**: .
- **GitHub**: .

---

⭐ **Jika project ini membantu Anda, jangan lupa untuk memberikan star!** ⭐

---
