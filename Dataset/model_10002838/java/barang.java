





import java.util.List;
import java.util.ArrayList;

public class barang  {

    private String id_barang;
    private String satuan;
    private None nama_barang;
    private String kategori;
    private int harga;
    private int stok;



    public barang(
        String id_barang,        String satuan,        None nama_barang,        String kategori,        int harga,        int stok    ) {
        this.id_barang = id_barang;
        this.satuan = satuan;
        this.nama_barang = nama_barang;
        this.kategori = kategori;
        this.harga = harga;
        this.stok = stok;
    }


    public String getId_barang() {
        return id_barang;
    }

    public void setId_barang(String id_barang) {
        this.id_barang = id_barang;
    }
    public String getSatuan() {
        return satuan;
    }

    public void setSatuan(String satuan) {
        this.satuan = satuan;
    }
    public None getNama_barang() {
        return nama_barang;
    }

    public void setNama_barang(None nama_barang) {
        this.nama_barang = nama_barang;
    }
    public String getKategori() {
        return kategori;
    }

    public void setKategori(String kategori) {
        this.kategori = kategori;
    }
    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        this.harga = harga;
    }
    public int getStok() {
        return stok;
    }

    public void setStok(int stok) {
        this.stok = stok;
    }


}