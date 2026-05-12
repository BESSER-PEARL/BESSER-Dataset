





import java.util.List;
import java.util.ArrayList;

public class Pembayarans  {

    private int jumlah;
    private String prefix;
    private int semester_id;
    private int biaya_kuliah_id;
    private String keterangan;
    private String no_pembayaran;
    private int pembayaran_tipe;
    private int mahasiswa_id;
    private String tanggal_pembayaran;
    private int user_id;
    private int id;
    private int status;



    public Pembayarans(
        int jumlah,        String prefix,        int semester_id,        int biaya_kuliah_id,        String keterangan,        String no_pembayaran,        int pembayaran_tipe,        int mahasiswa_id,        String tanggal_pembayaran,        int user_id,        int id,        int status    ) {
        this.jumlah = jumlah;
        this.prefix = prefix;
        this.semester_id = semester_id;
        this.biaya_kuliah_id = biaya_kuliah_id;
        this.keterangan = keterangan;
        this.no_pembayaran = no_pembayaran;
        this.pembayaran_tipe = pembayaran_tipe;
        this.mahasiswa_id = mahasiswa_id;
        this.tanggal_pembayaran = tanggal_pembayaran;
        this.user_id = user_id;
        this.id = id;
        this.status = status;
    }


    public int getJumlah() {
        return jumlah;
    }

    public void setJumlah(int jumlah) {
        this.jumlah = jumlah;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public int getSemester_id() {
        return semester_id;
    }

    public void setSemester_id(int semester_id) {
        this.semester_id = semester_id;
    }
    public int getBiaya_kuliah_id() {
        return biaya_kuliah_id;
    }

    public void setBiaya_kuliah_id(int biaya_kuliah_id) {
        this.biaya_kuliah_id = biaya_kuliah_id;
    }
    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
    public String getNo_pembayaran() {
        return no_pembayaran;
    }

    public void setNo_pembayaran(String no_pembayaran) {
        this.no_pembayaran = no_pembayaran;
    }
    public int getPembayaran_tipe() {
        return pembayaran_tipe;
    }

    public void setPembayaran_tipe(int pembayaran_tipe) {
        this.pembayaran_tipe = pembayaran_tipe;
    }
    public int getMahasiswa_id() {
        return mahasiswa_id;
    }

    public void setMahasiswa_id(int mahasiswa_id) {
        this.mahasiswa_id = mahasiswa_id;
    }
    public String getTanggal_pembayaran() {
        return tanggal_pembayaran;
    }

    public void setTanggal_pembayaran(String tanggal_pembayaran) {
        this.tanggal_pembayaran = tanggal_pembayaran;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }


}