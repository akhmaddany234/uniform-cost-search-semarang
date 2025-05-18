from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.messagebox import *
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import colors
import matplotlib.pyplot as plt


class Sicepet:
#______________________________ TAMPILAN awal ___________________________________
    def __init__(self, tampilanAplikasi):
        self.tampilanAplikasi = tampilanAplikasi
        tampilanAplikasi.title("Selamat datang di Sicepet")
        tampilanAplikasi.attributes('-fullscreen', True) 
        tampilanAplikasi.geometry("1280x720")
    
        self.TampilanHome()

    def TampilanHome(self):
        self.clear_widgets()

        self.img = Image.open("GAMBAR SICEPAT/Sicepet 1.png")  
        self.resize7 = self.img.resize((1280,720), Image.LANCZOS)
        self.Img= ImageTk.PhotoImage(self.resize7)
        self.Window = Label(self.tampilanAplikasi, image=self.Img)
        self.Window.place(x=0, y=0, relwidth=1, relheight=1)

        self.buttonabout = PhotoImage(file = r"GAMBAR SICEPAT/Tombol About Us.png") 
        self.aboutus = Button(self.tampilanAplikasi,image=self.buttonabout,command=self.Tampilan_AboutUs,width=100,height=30,borderwidth=0,bg='white',activebackground='white',cursor='hand2').place(x=609, y=17)

        self.buttonadmin = PhotoImage(file = r"GAMBAR SICEPAT/Tombol Masuk.png") 
        self.Masuk = Button(self.tampilanAplikasi,image=self.buttonadmin,command=self.Tampilan_InputUser,width=470,height=70,borderwidth=0,bg='white',activebackground='white',cursor='hand2').place(x=200, y=518)

        self.buttonExit = PhotoImage(file = r"GAMBAR SICEPAT/Tombol Exit.png") 
        self.tombolxixi = Button(self.tampilanAplikasi,image=self.buttonExit,command=self.Exit,width=50,height=45,borderwidth=0,bg='white',activebackground='white',cursor='hand2').place(x=20, y=15)


    def Tampilan_AboutUs(self):
        self.clear_widgets()

        self.Img_Tampilan_AboutUs = Image.open("GAMBAR SICEPAT/Sicepet 2.png")
        self.resize3 = self.Img_Tampilan_AboutUs.resize((1280,720), Image.LANCZOS)
        self.Img_Tampilan_AboutUs_read = ImageTk.PhotoImage(self.resize3)
        self.Window_AboutUs = Label(self.tampilanAplikasi, image=self.Img_Tampilan_AboutUs_read)
        self.Window_AboutUs.place(x=0, y=0, relwidth=1, relheight=1)

        self.ImgButton_Home = PhotoImage(file = r"GAMBAR SICEPAT/Tombol Homee.png") 
        Button_Home = Button(self.tampilanAplikasi,image=self.ImgButton_Home,command=self.TampilanHome,width=70,height=30,borderwidth=0,bg='white',activebackground='white',cursor='hand2').place(x=510, y=17)


    def Tampilan_InputUser(self):
        self.clear_widgets()

        self.Input_User = Image.open("GAMBAR SICEPAT/Sicepet 3.png")
        self.resize4 = self.Input_User.resize((1280,720), Image.LANCZOS)
        self.Input_User_read = ImageTk.PhotoImage(self.resize4)
        self.Label_InputUser = Label(self.tampilanAplikasi, image=self.Input_User_read)
        self.Label_InputUser.place(x=0, y=0, relwidth=1, relheight=1)

        self.df = pd.read_csv("Data Set/Data Rute AI.csv")

        self.graph = {}
        self.road_names = {}

        self.input_username = StringVar()
        self.username1_entry = Entry(self.tampilanAplikasi,textvariable=self.input_username, border=0, width=25, font=("Georgia", 21), fg="gray", bg="#eef5ff")
        self.username1_entry.place(x=410, y=285)
        self.username1_entry.insert(0, "Masukan Nama")
        self.username1_entry.bind("<FocusIn>", self.clear_placeholder_username1)
        self.username1_entry.bind("<FocusOut>", self.add_placeholder_username1) 

        self.input_kecamatan = StringVar()
        self.kecamatan_entry = Entry(self.tampilanAplikasi,textvariable=self.input_kecamatan,border=0, width=25, font=("Georgia", 21), fg="grey", bg="#eef5ff")
        self.kecamatan_entry.place(x=410, y=415)

        self.kecamatan_entry.insert(0, "Masukan Kecamatan")
        self.kecamatan_entry.bind("<FocusIn>", self.clear_placeholder_kecamatan)
        self.kecamatan_entry.bind("<FocusOut>", self.add_placeholder_kecamatan)

        self.ImgCariRute = PhotoImage(file = r"GAMBAR SICEPAT/Tombol Cari Rute.png") 
        Button_CariRute = Button(self.tampilanAplikasi,image=self.ImgCariRute,command=self.cek_input_kecamatan,width=260,height=40,borderwidth=0,bg='white',activebackground='white',cursor='hand2').place(x=500, y=495)

        self.ImgButton_Kembali = PhotoImage(file = r"GAMBAR SICEPAT/Tombol Kembali.png") 
        Button_Kembali = Button(self.tampilanAplikasi,image=self.ImgButton_Kembali,command=self.TampilanHome,width=140,height=40,borderwidth=0,bg='white',activebackground='white',cursor='hand2').place(x=1068, y=640)

    def clear_placeholder_username1(self, event):
        if self.username1_entry.get() == "Masukan Nama":
            self.username1_entry.delete(0, END)
            self.username1_entry.config(fg='black')
    def add_placeholder_username1(self, event):
        if self.username1_entry.get() == "":
            self.username1_entry.insert(0, "Masukan Nama")
            self.username1_entry.config(fg='grey')
    def clear_placeholder_kecamatan(self, event):
        if self.kecamatan_entry.get() == "Masukan Kecamatan":
            self.kecamatan_entry.delete(0, END)
            self.kecamatan_entry.config(fg='black')
    def add_placeholder_kecamatan(self, event):
        if self.kecamatan_entry.get() == "":
            self.kecamatan_entry.insert(0, "Masukan Kecamatan")
            self.kecamatan_entry.config(fg='grey')

#-------------------------------------------------------------------------------------------------
            
    def cek_input_kecamatan(self):
        nama = self.input_username.get()
        kecamatan = self.input_kecamatan.get().lower()
        if not nama or not kecamatan:
            showerror("Mohon Maaf🙏","Nama dan Kecamatan tidak boleh kosong")
            return

        start_nodes = {"banyumanik": "A1", "candisari": "B1", "gajahmungkur": "C1", "gayamsari": "D1", 
               "genuk": "E1", "gunungpati": "F1", "mijen": "G1", "ngaliyan": "H1", "pedurungan": "I1", 
               "semarang barat": "J1", "semarang selatan": "K1", "semarang tengah": "L1", 
               "semarang timur": "M1", "semarang utara": "N1", "tembalang": "O1", "tugu": "P1"}

        self.start_node = start_nodes.get(kecamatan, "Tidak ditemukan titik awal untuk Kecamatan ini.")

        if self.start_node == "Tidak ditemukan titik awal untuk Kecamatan ini.":
            showwarning("Peringatan", self.start_node)
            return
        self.filtered_data = self.df[
            self.df['Kecamatan'].str.contains(kecamatan, case=False, na=False)
        ]

        self.Tampilan_output(self.start_node, kecamatan)
        self.Tampilan_graff(kecamatan)
    
    def kondisi_ke_biaya(self, kondisi):
        if kondisi == "Baik":
            return 1
        elif kondisi == "Sedang":
            return 1.2
        elif kondisi == "Rusak Ringan":
            return 1.5
        elif kondisi == "Rusak Berat":
            return 1.7
        return 1
    
    def uniform_cost_search(self, start, goal):
        queue = [(0, start, [])]
        visited = set()
        explored = {}

        while queue:
            queue.sort(key=lambda x: x[0])
            biaya_sekarang, node, jalur = queue.pop(0)

            if node == goal:
                self.jalan_dilewati = [jalan for node, jalan, next_node in jalur]
                return biaya_sekarang, self.jalan_dilewati

            if node in visited:
                continue
            
            visited.add(node)
            explored[node] = biaya_sekarang

            for tetangga, data in self.G[node].items():
                if tetangga not in visited:
                    biaya = data['weight']
                    jalan = data['namajalan']
                    self.total_biaya = biaya_sekarang + biaya

                    if tetangga not in explored or self.total_biaya < explored[tetangga]:
                        queue.append((self.total_biaya, tetangga, jalur + [(node, jalan, tetangga)]))

        return float("inf"), []
    
    def Tampilan_output(self, start_node, kecamatan):
        def submit_goal():
            goal_node = self.node_tujuan.get()
            tanggal = self.input_tanggal.get() 

            if self.node_tujuan.get():
                self.combobox_tujuan.config(state="disabled") 
            else:
                self.combobox_tujuan.config(state="normal")
            
            #------------------------------- Menentukan Rute yang di lewati dengan UCS ------------------------------------
            biaya, jalan_dilewati = self.uniform_cost_search(self.start_node, goal_node)

            if biaya != float("inf"):
                jalan_dilewati_terformat = []
                for i in range(0, len(jalan_dilewati), 3):  # Menggunakan 3 sebagai pemisah
                    jalan_dilewati_terformat.append(" --> ".join(jalan_dilewati[i:i+3]))
                result = "\n".join(jalan_dilewati_terformat)
            else:
                result = f"Tidak ada jalur yang ditemukan dari {start_node} ke {goal_node}"

            label_result.config(text=result)
            #-------------------------------------------------------------------------------------------------------------

            #-------------------------------------------- DESKRIPSI ------------------------------------------------------
            def get_comparison_date(input_date, input_year):
                comparison_mapping = {
                    "2023": {"15 April": "3 April", "16 April": "4 April", "17 April": "5 April", "18 April": "6 April", "19 April": "7 April",
                            "20 April": "8 April", "21 April": "9 April", "22 April": "10 April", "23 April": "11 April", "24 April": "12 April",
                            "25 April": "13 April", "26 April": "14 April", "27 April": "15 April", "28 April": "16 April", "29 April": "17 April"},
                    "2024": {"3 April": "15 April", "4 April": "16 April", "5 April": "17 April", "6 April": "18 April", "7 April": "19 April",
                            "8 April": "20 April", "9 April": "21 April", "10 April": "22 April", "11 April": "23 April", "12 April": "24 April",
                            "13 April": "25 April", "14 April": "26 April", "15 April": "27 April", "16 April": "28 April", "17 April": "29 April"}
                }

                if input_year == "2023":
                    return comparison_mapping["2023"].get(input_date, None)
                elif input_year == "2024":
                    return comparison_mapping["2024"].get(input_date, None)
                else:
                    return None

            def compare_traffic_conditions(nama_jalan, input_date, input_year):
                comparison_date = get_comparison_date(input_date, input_year)
                if not comparison_date:
                    return f"Tidak ditemukan tanggal pembanding untuk {input_date} di tahun {input_year}."

                file_2023 = "Data Set/Data Jalan 2023.csv"
                file_2024 = "Data Set/Data Jalan 2024.csv"

                data_2023 = pd.read_csv(file_2023)
                data_2024 = pd.read_csv(file_2024)

                if input_year == "2023":
                    input_data = data_2023
                    comparison_data = data_2024
                    tanggal_tahun = f'{comparison_date} 2024'
                else:
                    input_data = data_2024
                    comparison_data = data_2023
                    tanggal_tahun = f'{comparison_date} 2023'

                input_jalan = input_data[input_data['Nama_Ruas'].str.contains(nama_jalan, case=False, na=False)]
                comparison_jalan = comparison_data[comparison_data['Nama_Ruas'].str.contains(nama_jalan, case=False, na=False)]

                if input_jalan.empty or comparison_jalan.empty:
                    return "Nama jalan tidak ditemukan di salah satu dataset."

                if input_date not in input_jalan.columns or comparison_date not in comparison_jalan.columns:
                    return f"Kolom tanggal tidak ditemukan untuk {input_date} atau {comparison_date}."

                kondisi_input = input_jalan[input_date].iloc[0]
                kondisi_comparison = comparison_jalan[comparison_date].iloc[0]

                prioritas = {"lancar": 1, "sedang": 2, "macet": 3}

                if kondisi_input not in prioritas or kondisi_comparison not in prioritas:
                    return "Data kondisi lalu lintas tidak valid pada salah satu dataset."

                if prioritas[kondisi_input] < prioritas[kondisi_comparison]:
                    return f"Kondisi lalu lintas pada {input_date} tahun\n{input_year} lebih lancar dibandingkan dengan {tanggal_tahun}."
                elif prioritas[kondisi_input] > prioritas[kondisi_comparison]:
                    return f"Kondisi lalu lintas pada {input_date} tahun\n{input_year} lebih macet dibandingkan dengan {tanggal_tahun}."
                else:
                    return f"Kondisi lalu lintas pada {input_date} tahun\n{input_year} dan {tanggal_tahun} sama-sama {kondisi_input}."
                
            nama_jalan = self.jalan_yang_dipilih.get()
            input_date = self.input_tanggal.get()
            input_year = self.input_tahun.get()

            if not nama_jalan or not input_date or not input_year:
                showwarning("Peringatan", "Harap isi semua kolom input!")
                return

            hasilperbandingan = compare_traffic_conditions(nama_jalan, input_date, input_year)


            #======================================== ESTIMASI WAKTU ===================================================
            kecamatan_input = kecamatan  

            tanggal_input = self.input_tanggal.get().split()[0]  
            jalan_dilalui_input = jalan_dilewati
            
            if self.input_tahun.get() == '2023':
                datacsv = pd.read_csv('Data Set/Data Jalan 2023.csv')
            elif self.input_tahun.get() == '2024':
                datacsv = pd.read_csv('Data Set/Data Jalan 2024.csv')
            else:
                showinfo('data tidak di temukan')
            estimasi, rata_waktu = self.estimasi_lalu_lintas(datacsv, kecamatan_input, tanggal_input, jalan_dilalui_input)

            def format_deskripsi(deskripsi):
                words = deskripsi.split() 
                formatted_words = []
                
                for i in range(0, len(words), 9):
                    formatted_words.append(" ".join(words[i:i+9])) 

                return "\n".join(formatted_words)
        
            estimasi_output = "Estimasi: "
            if estimasi == "lancar":
                estimasi_output += "Tepat waktu"
                deskripsi_output = "Paket Anda akan tiba tepat waktu karena kondisi rata-rata jalur\npengiriman paket lancar."
            elif estimasi == "sedang":
                estimasi_output += "Kemungkinan terlambat"
                deskripsi_output = "Paket Anda kemungkinan terlambat karena kondisi rata-rata jalur\npengiriman paket sedang."
            elif estimasi == "macet":
                estimasi_output += "Terlambat"
                deskripsi_output = "Paket Anda kemungkinan terlambat karena kondisi rata rata jalur\npengiriman paket sedang macet."
            else:
                estimasi_output += "Data tidak tersedia"
                deskripsi_output = "Tidak ada informasi yang tersedia mengenai kondisi jalur\npengiriman paket."

            if rata_waktu is not None:
                estimasi_output += f"\nEstimasi waktu rata-rata: {int(rata_waktu)} menit"
            else:
                estimasi_output += "\nTidak ada data waktu yang valid."

            formatted_deskripsi = format_deskripsi(deskripsi_output)
            label_result_estimasi.config(text=estimasi_output)
            label_deskripsi.config(text=formatted_deskripsi+hasilperbandingan)

        self.clear_widgets()

        self.Output = Image.open("GAMBAR SICEPAT/Sicepet 4.png")
        self.resize6 = self.Output.resize((1280, 720), Image.LANCZOS)
        self.Output_read = ImageTk.PhotoImage(self.resize6)
        self.Label_Output = Label(self.tampilanAplikasi, image=self.Output_read)
        self.Label_Output.place(x=0, y=0, relwidth=1, relheight=1)

        Nama_User = Label(self.tampilanAplikasi, text=f'Haii, Selamat datang {self.input_username.get().capitalize()}😍',
                        font=("Canva Sans", 18, 'bold'), background='#131f40', fg='white', borderwidth=0, anchor="w")
        Nama_User.place(x=80, y=29)

        Label_Kecamatan = Label(self.tampilanAplikasi, text=f'{kecamatan}', font=("T Lakes Neue", 22), background='#123753', fg='white')
        Label_Kecamatan.place(x=875, y=199)

        baris_pertama = self.filtered_data.iloc[0]
        titik_awal = baris_pertama['Nama_Ruas']
        Label_TitikAwal = Label(self.tampilanAplikasi, text=f'{titik_awal}', font=("T Lakes Neue", 12), background='#123753', fg='white')
        Label_TitikAwal.place(x=883, y=161)

        # ---------------- Tujuan -------------------
        self.node_tujuan = StringVar()
        self.jalan_yang_dipilih = StringVar()
        self.combobox_tujuan = ttk.Combobox(self.tampilanAplikasi, textvariable=self.jalan_yang_dipilih, state="readonly", font=("TT Lakes Neue", 25), width=18)
        self.combobox_tujuan['values'] = self.filtered_data['Nama_Ruas'].tolist()
        self.combobox_tujuan.place(x=135, y=97)
        self.combobox_tujuan.bind("<<ComboboxSelected>>", self.cari_node_tujuan)

        # ----------------- Tahun --------------------
        self.input_tahun = StringVar()
        self.tahun_combo = ttk.Combobox(self.tampilanAplikasi, textvariable=self.input_tahun, state="readonly", font=("TT Lakes Neue", 25), width=18)
        self.tahun_combo['values'] = ["2023", "2024"]  # Daftar tahun yang tersedia
        self.tahun_combo.place(x=505, y=97)

        # ------------------ Tanggal ------------------
        self.input_tanggal = StringVar()
        self.tanggal_combo = ttk.Combobox(self.tampilanAplikasi, textvariable=self.input_tanggal, state="readonly", font=("TT Lakes Neue", 25), width=18)
        self.tanggal_combo['values'] = []
        self.tanggal_combo.place(x=873, y=97)

        # ------------------ Fungsi untuk mengatur tanggal dan load CSV ------------------
        def on_tahun_selected(event):
            tahun = self.input_tahun.get()

            if tahun == "2023":
                self.tanggal_combo.config(values=["15 April", "16 April", "17 April", "18 April", "19 April", "20 April", "21 April", "22 April", "23 April", "24 April", "25 April", "26 April", "27 April", "28 April", "29 April"])
            elif tahun == "2024":
                self.tanggal_combo.config(values=["3 April", "4 April", "5 April", "6 April", "7 April", "8 April", "9 April", "10 April", "11 April", "12 April", "13 April", "14 April", "15 April", "16 April", "17 April"])
            else:
                self.tanggal_combo.config(values=[])

            # Memuat file CSV berdasarkan tahun yang dipilih
            if tahun == "2023":
                self.df = pd.read_csv("Data Set/Data Jalan 2023.csv")
            elif tahun == "2024":
                self.df = pd.read_csv("Data Set/Data Jalan 2024.csv")
            else:
                showwarning("Peringatan", "Tahun tidak valid")

        self.tahun_combo.bind("<<ComboboxSelected>>", on_tahun_selected)

        # ------------- Tombol Kembali -------------
        Button_Kembali = Button(self.tampilanAplikasi, image=self.ImgButton_Kembali, command=self.Tampilan_InputUser, width=140, height=40, borderwidth=0, bg='white', activebackground='white', cursor='hand2')
        Button_Kembali.place(x=1068, y=640)

        # ---------- Tombol Submit ------------
        self.ImgButton_Search = PhotoImage(file=r"GAMBAR SICEPAT/Tombol Search.png")
        submit_button = Button(self.tampilanAplikasi, image=self.ImgButton_Search, command=submit_goal, width=50, height=50, borderwidth=0, bg='white', activebackground='white', cursor='hand2')
        submit_button.place(x=62, y=100)


        # ==== Hasil UCS rute yang dilewati ======
        label_result = Label(self.tampilanAplikasi, text="", justify="left", background='#123753', font=("TT Lakes Neue", 13), fg='white')
        label_result.place(x=670, y=315)

        # ==== Hasil ESTIMASI ======
        label_result_estimasi = Label(self.tampilanAplikasi, text="", justify="left", background='#123753', font=("TT Lakes Neue", 13), fg='white')
        label_result_estimasi.place(x=670, y=587)

        # =========== deskripsi ===========
        label_deskripsi = Label(self.tampilanAplikasi, text="",justify="left", background='#123753', font=("TT Lakes Neue", 13), fg='white')
        label_deskripsi.place(x=670, y=472)

        # ---------- Tombol Visualisasi Cluster ------------
        self.ImgButton_clustering = PhotoImage(file=r"GAMBAR SICEPAT/Tombol Clustering.png")
        cluster_button = Button(self.tampilanAplikasi, image=self.ImgButton_clustering,command=lambda: self.Clustering(kecamatan), width=425, height=42, borderwidth=0, bg='white', activebackground='white', cursor='hand2')
        cluster_button.place(x=115, y=625)
        # ----------- Tombol Lihat Graf -------------
        self.ImgButton_LihatGraff = PhotoImage(file=r"GAMBAR SICEPAT/Tombol Lihat Graf.png")
        Button_LihatGraff = Button(self.tampilanAplikasi, image=self.ImgButton_LihatGraff, command=lambda: self.Tampilan_graff(kecamatan), width=440, height=340, borderwidth=0, bg='white', activebackground='white', cursor='hand2')
        Button_LihatGraff.place(x=105, y=278)
    
    def estimasi_lalu_lintas(self, datacsv, kecamatan_input, tanggal_input, jalan_dilalui_input):
        def bersihkan_menit(waktu_list):
            try:
                return int(waktu_list.split()[0])
            except:
                return None
            
        def estimasi_kondisi(kondisi_list):
            kondisi_terbanyak = max(set(kondisi_list), key=kondisi_list.count)
            return kondisi_terbanyak
            
        def rata_rata_waktu(waktu_list):
            waktu_valid = [w for w in waktu_list if w is not None]
            if waktu_valid:
                return sum(waktu_valid) / len(waktu_valid)
            else:
                return None

        if isinstance(tanggal_input, int):
            tanggal_kolom = str(tanggal_input)
        else:
            tanggal_kolom = str(tanggal_input.split()[0])
        
        #out 28 April == 28
        waktu_kolom = tanggal_kolom

        kecamatan_data = datacsv[datacsv['Kecamatan'] == kecamatan_input]

        jalan_dilalui = kecamatan_data[kecamatan_data['Nama_Ruas'].isin(jalan_dilalui_input)]

        if tanggal_kolom not in kecamatan_data.columns:
            raise KeyError(f"Kolom {tanggal_kolom} tidak ditemukan dalam data. Pastikan kolom tanggal sesuai dengan format.")
 
        kondisi_lalu_lintas = jalan_dilalui[f'{tanggal_kolom} April'].tolist()

        waktu_lalu_lintas = [bersihkan_menit(waktu) for waktu in jalan_dilalui[waktu_kolom].tolist()]

        estimasi = estimasi_kondisi(kondisi_lalu_lintas)

        rata_waktu = rata_rata_waktu(waktu_lalu_lintas)

        return estimasi, rata_waktu

    def cari_node_tujuan(self, event):
        self.node_tujuan.set("")
        selected_jalan = self.jalan_yang_dipilih.get()
        if selected_jalan:
            hasil = self.df[self.df['Nama_Ruas'] == selected_jalan]
            if not hasil.empty:
                self.node_tujuan.set(hasil.iloc[0]['Node_Akhir'])

    def Tampilan_graff(self, kecamatan):
        self.G = nx.Graph()
        data = pd.read_csv("Data Set/Data Rute AI.csv")  
        filtered_data = data[data['Kecamatan'] == kecamatan]

        for _, row in filtered_data.iterrows():
            biaya = row['Cost'] * self.kondisi_ke_biaya(row['Kondisi'])  
            self.G.add_node(row['Node_Awal'])
            self.G.add_node(row['Node_Akhir'])
            self.G.add_edge(row['Node_Awal'], row['Node_Akhir'], weight=biaya, namajalan=row['Nama_Ruas'])

        jalan_dilewati_edges = []
        total_cost = 0
        nodes_dilalui = set()

        for jalan in self.jalan_dilewati:
            found = False
            for _, row in filtered_data.iterrows():
                if row['Nama_Ruas'] == jalan:
                    biaya = row['Cost'] * self.kondisi_ke_biaya(row['Kondisi'])
                    jalan_dilewati_edges.append((row['Node_Awal'], row['Node_Akhir']))
                    total_cost += biaya
                    nodes_dilalui.add(row['Node_Awal'])
                    nodes_dilalui.add(row['Node_Akhir'])
                    found = True
                    break
            if not found:
                raise ValueError(f"Nama jalan '{jalan}' tidak ditemukan di data CSV.")

        pos = nx.spring_layout(self.G, seed=50, scale=15)  
        fig, ax = plt.subplots(figsize=(16, 14))
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.2)

        def draw_graph(highlight=False):
            ax.clear()
            edge_labels = nx.get_edge_attributes(self.G, 'weight')
            edge_info = nx.get_edge_attributes(self.G, 'namajalan')

            # Menggabungkan nama jalan dan bobot untuk ditampilkan di atas jalur
            full_edge_labels = {
                (u, v): f"{edge_info[(u, v)]} ({edge_labels[(u, v)]:.2f})"
                for u, v in edge_info
            }

            # Warna node: hijau jika node dilalui, biru untuk yang lainnya
            node_colors = ['green' if node in nodes_dilalui else 'lightblue' for node in self.G.nodes]

            # Menggambar graf
            nx.draw(
                self.G, pos, with_labels=True, node_color=node_colors, edge_color='grey',
                node_size=550, font_size=10, font_weight='bold', ax=ax)

            for (u, v), label in full_edge_labels.items():
                x = (pos[u][0] + pos[v][0]) / 2
                y = (pos[u][1] + pos[v][1]) / 2 + 0.2  
                ax.text(x, y, label, fontsize=8, color='black', ha='center', va='center')

            if highlight:
                nx.draw_networkx_edges(self.G, pos, edgelist=jalan_dilewati_edges, edge_color='blue', width=2, ax=ax)

            plt.draw()
        draw_graph(highlight=True)

        info_text = f"Node yang dilalui: {', '.join(sorted(nodes_dilalui))}\nTotal Bobot: {total_cost:.2f}"
        fig.text(0.5, 0.05, info_text, ha='center', fontsize=12, color='black')

        plt.show()
    

    def Clustering(self, kecamatan):
        self.clear_widgets()
        data = pd.read_csv("Data Set/Data Rute AI.csv")
        data_filtered = data[data['Kecamatan'] == kecamatan]

        cluster_map = {
            "Baik": 0,
            "Sedang": 1,
            "Rusak Ringan": 2,
            "Rusak Berat": 3
        }

        data_filtered['Cluster'] = data_filtered['Kondisi'].map(cluster_map)

        self.label_klaster = {}
        for cluster_id in range(4):
            self.label_klaster[cluster_id] = data_filtered[data_filtered['Cluster'] == cluster_id]['Nama_Ruas'].tolist()

        self.Output = Image.open("GAMBAR SICEPAT/Sicepet 5.png")
        self.resize6 = self.Output.resize((1280, 720), Image.LANCZOS)
        self.Output_read = ImageTk.PhotoImage(self.resize6)
        self.Label_Output = Label(self.tampilanAplikasi, image=self.Output_read)
        self.Label_Output.place(x=0, y=0, relwidth=1, relheight=1)

        posisi_klaster = {
            0: (65, 157),  
            1: (65, 288),
            2: (65, 423),
            3: (65, 560)
        }

        def bagi_daftar(lst, ukuran_potongan):
            return [lst[i:i + ukuran_potongan] for i in range(0, len(lst), ukuran_potongan)]

        for id_klaster, posisi in posisi_klaster.items():
            if not self.label_klaster.get(id_klaster):
                teks_klaster = f" Tidak ada jalan dengan kondisi tersebut pada kecamatan ini"
            else:
                potongan = bagi_daftar(self.label_klaster[id_klaster], 9)
                teks_klaster = ""
                for bagian in potongan:
                    teks_klaster += f"{', '.join(bagian)}\n"

            label_klaster_display = Label(self.tampilanAplikasi, text=teks_klaster, background='#123753', font=("TT Lakes Neue", 13), fg="white", justify='left')
            label_klaster_display.place(x=posisi[0], y=posisi[1]) 

        Label_Kecamatan2 = Label(self.tampilanAplikasi, text=f'{kecamatan}', font=("T Lakes Neue", 21), background='#123753', fg='white')
        Label_Kecamatan2.place(x=677, y=26)

        total_jalan = len(data_filtered)
        jumlah_per_cluster = [len(self.label_klaster[i]) for i in range(4)]

        teks_jumlah_klaster = f"Jumlah jalan = {total_jalan}           Cluster 0= {jumlah_per_cluster[0]}           Cluster 1 = {jumlah_per_cluster[1]}           Cluster 2 = {jumlah_per_cluster[2]}           Cluster 3 = {jumlah_per_cluster[3]}"
        
        label_jumlah_klaster = Label(self.tampilanAplikasi, text=teks_jumlah_klaster, background='#123753', font=("TT Lakes Neue", 13), fg="orange")
        label_jumlah_klaster.place(x=120, y=81)

        Button_Kembali = Button(self.tampilanAplikasi, image=self.ImgButton_Kembali, command=self.Tampilan_InputUser, width=140, height=40, borderwidth=0, bg='white', activebackground='white', cursor='hand2')
        Button_Kembali.place(x=1068, y=640)


    def clear_widgets(self):
        for widget in self.tampilanAplikasi.winfo_children():
            widget.destroy()
    def Exit(self):
        self.tampilanAplikasi.quit()


root = Tk()
aplikasi = Sicepet(root)
root.mainloop()