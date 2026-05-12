




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Data_Peminjaman  {

    private LocalDate Tanggalpinjam;
    private int NPK;
    private int NIK;
    private String Namakaryawan;
    private String keterangan;
    private String jumlahpinjam;



    public Data_Peminjaman(
        LocalDate Tanggalpinjam,        int NPK,        int NIK,        String Namakaryawan,        String keterangan,        String jumlahpinjam    ) {
        this.Tanggalpinjam = Tanggalpinjam;
        this.NPK = NPK;
        this.NIK = NIK;
        this.Namakaryawan = Namakaryawan;
        this.keterangan = keterangan;
        this.jumlahpinjam = jumlahpinjam;
    }


    public LocalDate getTanggalpinjam() {
        return Tanggalpinjam;
    }

    public void setTanggalpinjam(LocalDate Tanggalpinjam) {
        this.Tanggalpinjam = Tanggalpinjam;
    }
    public int getNpk() {
        return NPK;
    }

    public void setNpk(int NPK) {
        this.NPK = NPK;
    }
    public int getNik() {
        return NIK;
    }

    public void setNik(int NIK) {
        this.NIK = NIK;
    }
    public String getNamakaryawan() {
        return Namakaryawan;
    }

    public void setNamakaryawan(String Namakaryawan) {
        this.Namakaryawan = Namakaryawan;
    }
    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
    public String getJumlahpinjam() {
        return jumlahpinjam;
    }

    public void setJumlahpinjam(String jumlahpinjam) {
        this.jumlahpinjam = jumlahpinjam;
    }


}