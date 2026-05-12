





import java.util.List;
import java.util.ArrayList;

public class masterBiaya  {

    private int jml_bayar;
    private int user_id;
    private int jumlah_biaya;
    private int status;
    private String nama_biaya;
    private int id;
    private int kategori_id;



    public masterBiaya(
        int jml_bayar,        int user_id,        int jumlah_biaya,        int status,        String nama_biaya,        int id,        int kategori_id    ) {
        this.jml_bayar = jml_bayar;
        this.user_id = user_id;
        this.jumlah_biaya = jumlah_biaya;
        this.status = status;
        this.nama_biaya = nama_biaya;
        this.id = id;
        this.kategori_id = kategori_id;
    }


    public int getJml_bayar() {
        return jml_bayar;
    }

    public void setJml_bayar(int jml_bayar) {
        this.jml_bayar = jml_bayar;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getJumlah_biaya() {
        return jumlah_biaya;
    }

    public void setJumlah_biaya(int jumlah_biaya) {
        this.jumlah_biaya = jumlah_biaya;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public String getNama_biaya() {
        return nama_biaya;
    }

    public void setNama_biaya(String nama_biaya) {
        this.nama_biaya = nama_biaya;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getKategori_id() {
        return kategori_id;
    }

    public void setKategori_id(int kategori_id) {
        this.kategori_id = kategori_id;
    }


}