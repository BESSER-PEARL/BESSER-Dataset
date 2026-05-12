





import java.util.List;
import java.util.ArrayList;

public class kota  {

    private int id_kota;
    private String gambar;
    private String nama_kota;



    public kota(
        int id_kota,        String gambar,        String nama_kota    ) {
        this.id_kota = id_kota;
        this.gambar = gambar;
        this.nama_kota = nama_kota;
    }


    public int getId_kota() {
        return id_kota;
    }

    public void setId_kota(int id_kota) {
        this.id_kota = id_kota;
    }
    public String getGambar() {
        return gambar;
    }

    public void setGambar(String gambar) {
        this.gambar = gambar;
    }
    public String getNama_kota() {
        return nama_kota;
    }

    public void setNama_kota(String nama_kota) {
        this.nama_kota = nama_kota;
    }


}