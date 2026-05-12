





import java.util.List;
import java.util.ArrayList;

public class barang  {

    private int harga_barang;
    private int id;
    private String nama_barang;
    private int id_kategori;
    private String deskripsi_barang;



    public barang(
        int harga_barang,        int id,        String nama_barang,        int id_kategori,        String deskripsi_barang    ) {
        this.harga_barang = harga_barang;
        this.id = id;
        this.nama_barang = nama_barang;
        this.id_kategori = id_kategori;
        this.deskripsi_barang = deskripsi_barang;
    }


    public int getHarga_barang() {
        return harga_barang;
    }

    public void setHarga_barang(int harga_barang) {
        this.harga_barang = harga_barang;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNama_barang() {
        return nama_barang;
    }

    public void setNama_barang(String nama_barang) {
        this.nama_barang = nama_barang;
    }
    public int getId_kategori() {
        return id_kategori;
    }

    public void setId_kategori(int id_kategori) {
        this.id_kategori = id_kategori;
    }
    public String getDeskripsi_barang() {
        return deskripsi_barang;
    }

    public void setDeskripsi_barang(String deskripsi_barang) {
        this.deskripsi_barang = deskripsi_barang;
    }


}