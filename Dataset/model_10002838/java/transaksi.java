





import java.util.List;
import java.util.ArrayList;

public class transaksi  {

    private int total;
    private String tanggal;
    private None nama_barang;
    private int id_transaksi;





    private pelanggan pelanggan;




    private supplier supplier;


    public transaksi(
        int total,        String tanggal,        None nama_barang,        int id_transaksi    ) {
        this.total = total;
        this.tanggal = tanggal;
        this.nama_barang = nama_barang;
        this.id_transaksi = id_transaksi;
    }


    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
    public String getTanggal() {
        return tanggal;
    }

    public void setTanggal(String tanggal) {
        this.tanggal = tanggal;
    }
    public None getNama_barang() {
        return nama_barang;
    }

    public void setNama_barang(None nama_barang) {
        this.nama_barang = nama_barang;
    }
    public int getId_transaksi() {
        return id_transaksi;
    }

    public void setId_transaksi(int id_transaksi) {
        this.id_transaksi = id_transaksi;
    }

    public pelanggan getPelanggan() {
        return pelanggan;
    }

    public void setPelanggan(pelanggan pelanggan) {
        this.pelanggan = pelanggan;
    }
    public supplier getSupplier() {
        return supplier;
    }

    public void setSupplier(supplier supplier) {
        this.supplier = supplier;
    }

}