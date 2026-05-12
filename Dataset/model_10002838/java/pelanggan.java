





import java.util.List;
import java.util.ArrayList;

public class pelanggan  {

    private int id_pelanggan;
    private None nama_pelanggan;
    private String no_telp_pelanggan;
    private String alamat;



    public pelanggan(
        int id_pelanggan,        None nama_pelanggan,        String no_telp_pelanggan,        String alamat    ) {
        this.id_pelanggan = id_pelanggan;
        this.nama_pelanggan = nama_pelanggan;
        this.no_telp_pelanggan = no_telp_pelanggan;
        this.alamat = alamat;
    }


    public int getId_pelanggan() {
        return id_pelanggan;
    }

    public void setId_pelanggan(int id_pelanggan) {
        this.id_pelanggan = id_pelanggan;
    }
    public None getNama_pelanggan() {
        return nama_pelanggan;
    }

    public void setNama_pelanggan(None nama_pelanggan) {
        this.nama_pelanggan = nama_pelanggan;
    }
    public String getNo_telp_pelanggan() {
        return no_telp_pelanggan;
    }

    public void setNo_telp_pelanggan(String no_telp_pelanggan) {
        this.no_telp_pelanggan = no_telp_pelanggan;
    }
    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }


}