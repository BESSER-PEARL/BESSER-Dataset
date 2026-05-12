





import java.util.List;
import java.util.ArrayList;

public class transaksi  {

    private String nama_event;
    private int id_event;
    private int id_kota;
    private int harga;
    private String tipe_tiket;
    private int id_orders;





    private user user;


    public transaksi(
        String nama_event,        int id_event,        int id_kota,        int harga,        String tipe_tiket,        int id_orders    ) {
        this.nama_event = nama_event;
        this.id_event = id_event;
        this.id_kota = id_kota;
        this.harga = harga;
        this.tipe_tiket = tipe_tiket;
        this.id_orders = id_orders;
    }


    public String getNama_event() {
        return nama_event;
    }

    public void setNama_event(String nama_event) {
        this.nama_event = nama_event;
    }
    public int getId_event() {
        return id_event;
    }

    public void setId_event(int id_event) {
        this.id_event = id_event;
    }
    public int getId_kota() {
        return id_kota;
    }

    public void setId_kota(int id_kota) {
        this.id_kota = id_kota;
    }
    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        this.harga = harga;
    }
    public String getTipe_tiket() {
        return tipe_tiket;
    }

    public void setTipe_tiket(String tipe_tiket) {
        this.tipe_tiket = tipe_tiket;
    }
    public int getId_orders() {
        return id_orders;
    }

    public void setId_orders(int id_orders) {
        this.id_orders = id_orders;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}