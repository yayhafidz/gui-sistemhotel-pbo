import tkinter as tk
from tkinter import ttk, messagebox

class PemesananHotel:
    def __init__(self):
        self.kelas_hotel = {
            'Kamar Standar': 100000,
            'Kamar Superior': 150000,
            'Kamar Deluxe': 200000,
            'Suite Kamar': 300000
        }
        self.data_pemesanan_list = []  
        self.window = tk.Tk()
        self.window.title("Pemesanan Hotel")
        self.window.configure(bg='lightblue') 
        self.buat_widget()

    def buat_widget(self):
        # Membuat frame untuk input
        frame_input = tk.Frame(self.window, padx=10, pady=10, bg='lightblue') 
        frame_input.pack()

        tk.Label(frame_input, text="Tanggal Check-in (format: DD-MM-YYYY):", bg='lightblue').grid(row=0, column=0, sticky=tk.W)
        self.tanggal_checkin_entry = tk.Entry(frame_input)
        self.tanggal_checkin_entry.grid(row=0, column=1)

        tk.Label(frame_input, text="Jumlah Malam:", bg='lightblue').grid(row=1, column=0, sticky=tk.W)
        self.jumlah_malam_entry = tk.Entry(frame_input)
        self.jumlah_malam_entry.grid(row=1, column=1)

        tk.Label(frame_input, text="Kelas Kamar:", bg='lightblue').grid(row=2, column=0, sticky=tk.W)
        self.kelas_hotel_var = tk.StringVar(self.window)
        self.kelas_hotel_var.set("Kamar Standar")
        self.kelas_hotel_optionmenu = tk.OptionMenu(frame_input, self.kelas_hotel_var, *self.kelas_hotel.keys())
        self.kelas_hotel_optionmenu.grid(row=2, column=1)

        tk.Label(frame_input, text="Nama Lengkap:", bg='lightblue').grid(row=3, column=0, sticky=tk.W)
        self.nama_entry = tk.Entry(frame_input)
        self.nama_entry.grid(row=3, column=1)

        tk.Label(frame_input, text="Nomor Kamar:", bg='lightblue').grid(row=4, column=0, sticky=tk.W)
        self.nomor_kamar_entry = tk.Entry(frame_input)
        self.nomor_kamar_entry.grid(row=4, column=1)

        tk.Label(frame_input, text="Alamat Email:", bg='lightblue').grid(row=5, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(frame_input)
        self.email_entry.grid(row=5, column=1)

        tk.Label(frame_input, text="Nomor Telepon:", bg='lightblue').grid(row=6, column=0, sticky=tk.W)
        self.telepon_entry = tk.Entry(frame_input)
        self.telepon_entry.grid(row=6, column=1)

        # Membuat frame untuk tombol
        frame_tombol = tk.Frame(self.window, pady=10, bg='lightblue')  
        frame_tombol.pack()

        self.tombol_submit = tk.Button(frame_tombol, text="Submit", command=self.submit_data_pemesanan, bg='green', fg='white') 
        self.tombol_submit.pack(side=tk.LEFT)

        self.tombol_tampilkan = tk.Button(frame_tombol, text="Tampilkan Data Pemesanan", command=self.tampilkan_data_pemesanan, bg='blue', fg='white')  
        self.tombol_tampilkan.pack(side=tk.LEFT)

        # Tombol Hapus Data Pemesanan
        self.tombol_hapus = tk.Button(frame_tombol, text="Hapus Data Pemesanan", command=self.hapus_data_pemesanan, bg='red', fg='white')  
        self.tombol_hapus.pack(side=tk.LEFT)
        
    def submit_data_pemesanan(self):
        if not all(entry.get() for entry in [self.tanggal_checkin_entry, self.jumlah_malam_entry, self.nama_entry, self.nomor_kamar_entry, self.email_entry, self.telepon_entry]):
            messagebox.showwarning("Kolom Kosong", "Harap isi semua kolom yang diperlukan.")
            return

        data_pemesanan = {
            'Tanggal Check-in': self.tanggal_checkin_entry.get(),
            'Jumlah Malam': int(self.jumlah_malam_entry.get()),
            'Kelas Kamar': self.kelas_hotel_var.get(),
            'Nama Lengkap': self.nama_entry.get(),
            'Nomor Kamar': self.nomor_kamar_entry.get(),
            'Alamat Email': self.email_entry.get(),
            'Nomor Telepon': self.telepon_entry.get()
        }
        self.data_pemesanan_list.append(data_pemesanan)

        self.pembayaran(data_pemesanan)

    def tampilkan_data_pemesanan(self):
        if not self.data_pemesanan_list:
            messagebox.showinfo("Data Tidak Ada", "Belum ada data pemesanan yang tersedia.")
            return

        jendela_data_pemesanan = tk.Toplevel(self.window)
        jendela_data_pemesanan.title("Data Pemesanan")

        tree = ttk.Treeview(jendela_data_pemesanan, columns=['', *list(self.data_pemesanan_list[0].keys())], show="headings")
        
        # Add checkboxes to the tree
        tree.heading('', text='', anchor='w')
        tree.column('', stretch=tk.NO, width=30)

        for col in tree["columns"]:
            tree.heading(col, text=col.capitalize())

        for idx, data_pemesanan in enumerate(self.data_pemesanan_list, start=1):
            values = [f"Pemesanan {idx}", *list(data_pemesanan.values())]
            tree.insert("", idx, values=values)

        tree.pack()

    def hapus_data_pemesanan(self):
        if not self.data_pemesanan_list:
            messagebox.showinfo("Data Tidak Ada", "Belum ada data pemesanan yang tersedia.")
            return

        jendela_hapus = tk.Toplevel(self.window)
        jendela_hapus.title("Hapus Data Pemesanan")

        tk.Label(jendela_hapus, text="Pilih Data Pemesanan untuk Dihapus:").pack()

        tree = ttk.Treeview(jendela_hapus, columns=['', *list(self.data_pemesanan_list[0].keys())], show="headings")
        tree.heading('', text='', anchor='w')
        tree.column('', stretch=tk.NO, width=30)

        for col in tree["columns"]:
            tree.heading(col, text=col.capitalize())

        for idx, data_pemesanan in enumerate(self.data_pemesanan_list, start=1):
            values = [f"Pemesanan {idx}", *list(data_pemesanan.values())]
            tree.insert("", idx, values=values)

        tree.pack()

        tombol_hapus = tk.Button(jendela_hapus, text="Hapus", command=lambda: self.konfirmasi_hapus(tree))
        tombol_hapus.pack()

    def konfirmasi_hapus(self, tree):
        item_terpilih = tree.selection()

        if item_terpilih:
            idx_terpilih = int(tree.item(item_terpilih, "values")[0].split()[1]) - 1
            pemesanan_dihapus = self.data_pemesanan_list.pop(idx_terpilih)
            messagebox.showinfo("Pemesanan Dihapus", f"Pemesanan {idx_terpilih + 1} telah dihapus.")
            tree.delete(item_terpilih)
        else:
            messagebox.showwarning("Tidak Ada Pilihan", "Harap pilih pemesanan untuk dihapus.")

    def pembayaran(self, data_pemesanan):
        jendela_pembayaran = tk.Toplevel(self.window)
        jendela_pembayaran.title("Pembayaran")

        harga_per_malam = self.kelas_hotel[data_pemesanan['Kelas Kamar']]
        total = harga_per_malam * data_pemesanan['Jumlah Malam']

        tk.Label(jendela_pembayaran, text="Detail Pemesanan:").pack()

        for key, value in data_pemesanan.items():
            tk.Label(jendela_pembayaran, text=f"{key.capitalize()}: {value}").pack()

        tk.Label(jendela_pembayaran, text=f"\nTotal Harga: {total:,} Rupiah").pack()

        tk.Label(jendela_pembayaran, text="Jumlah Bayar:").pack()
        self.uang_bayar_entry = tk.Entry(jendela_pembayaran)
        self.uang_bayar_entry.pack()

        tk.Label(jendela_pembayaran, text="Metode Pembayaran:").pack()
        self.metode_pembayaran_var = tk.StringVar(jendela_pembayaran)
        self.metode_pembayaran_var.set("Kartu Kredit")
        metode_pembayaran_optionmenu = tk.OptionMenu(jendela_pembayaran, self.metode_pembayaran_var, "Kartu Kredit", "Tunai")
        metode_pembayaran_optionmenu.pack()

        self.tombol_submit_pembayaran = tk.Button(jendela_pembayaran, text="Submit", command=lambda: self.proses_pembayaran(total, jendela_pembayaran))
        self.tombol_submit_pembayaran.pack()

    def proses_pembayaran(self, total_pembayaran, jendela_pembayaran):
        uang_bayar = self.uang_bayar_entry.get()

        if not uang_bayar.isdigit():
            messagebox.showerror("Error", "Input tidak valid. Harap masukkan angka yang valid.")
        else:
            uang_bayar = int(uang_bayar)

            if uang_bayar < total_pembayaran:
                messagebox.showerror("Error", "Pembayaran tidak mencukupi.")
            else:
                kembalian = uang_bayar - total_pembayaran
                metode_pembayaran = self.metode_pembayaran_var.get()
                messagebox.showinfo("Pembayaran Berhasil", f"Jumlah Bayar: {uang_bayar:,} Rupiah\nKembalian: {kembalian:,} Rupiah\nMetode Pembayaran: {metode_pembayaran}")
                jendela_pembayaran.destroy()

    def jalankan(self):
        self.window.mainloop()

# Instantiate and run the application
pemesanan = PemesananHotel()
pemesanan.jalankan()
