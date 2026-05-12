




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Transaksi_Peminjaman  {

    private String Namakaryawan;
    private int Nopeminjaman;
    private int NIK;
    private String keterangan;
    private LocalDate Tanggalpinjam;
    private String jumlahpinjam;
    private int NPK;



    public Transaksi_Peminjaman(
        String Namakaryawan,        int Nopeminjaman,        int NIK,        String keterangan,        LocalDate Tanggalpinjam,        String jumlahpinjam,        int NPK    ) {
        this.Namakaryawan = Namakaryawan;
        this.Nopeminjaman = Nopeminjaman;
        this.NIK = NIK;
        this.keterangan = keterangan;
        this.Tanggalpinjam = Tanggalpinjam;
        this.jumlahpinjam = jumlahpinjam;
        this.NPK = NPK;
    }


    public String getNamakaryawan() {
        return Namakaryawan;
    }

    public void setNamakaryawan(String Namakaryawan) {
        this.Namakaryawan = Namakaryawan;
    }
    public int getNopeminjaman() {
        return Nopeminjaman;
    }

    public void setNopeminjaman(int Nopeminjaman) {
        this.Nopeminjaman = Nopeminjaman;
    }
    public int getNik() {
        return NIK;
    }

    public void setNik(int NIK) {
        this.NIK = NIK;
    }
    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
    public LocalDate getTanggalpinjam() {
        return Tanggalpinjam;
    }

    public void setTanggalpinjam(LocalDate Tanggalpinjam) {
        this.Tanggalpinjam = Tanggalpinjam;
    }
    public String getJumlahpinjam() {
        return jumlahpinjam;
    }

    public void setJumlahpinjam(String jumlahpinjam) {
        this.jumlahpinjam = jumlahpinjam;
    }
    public int getNpk() {
        return NPK;
    }

    public void setNpk(int NPK) {
        this.NPK = NPK;
    }


}