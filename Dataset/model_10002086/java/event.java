





import java.util.List;
import java.util.ArrayList;

public class event  {

    private int id_kota;
    private String tanggal;
    private String nama_event;
    private String gambar;
    private int harga_reguler;
    private String detail;
    private String longitude;
    private int id_admin;
    private int id_event;
    private int harga_premium;
    private String deskripsi;
    private String latitude;
    private String lokasi;





    private kota kota;




    private e_ticket e_ticket;




    private List<transaksi> transaksis;


    public event(
        int id_kota,        String tanggal,        String nama_event,        String gambar,        int harga_reguler,        String detail,        String longitude,        int id_admin,        int id_event,        int harga_premium,        String deskripsi,        String latitude,        String lokasi    ) {
        this.id_kota = id_kota;
        this.tanggal = tanggal;
        this.nama_event = nama_event;
        this.gambar = gambar;
        this.harga_reguler = harga_reguler;
        this.detail = detail;
        this.longitude = longitude;
        this.id_admin = id_admin;
        this.id_event = id_event;
        this.harga_premium = harga_premium;
        this.deskripsi = deskripsi;
        this.latitude = latitude;
        this.lokasi = lokasi;
        this.transaksis = new ArrayList<>();
    }

    public event(
        int id_kota,        String tanggal,        String nama_event,        String gambar,        int harga_reguler,        String detail,        String longitude,        int id_admin,        int id_event,        int harga_premium,        String deskripsi,        String latitude,        String lokasi        ArrayList<transaksi> transaksis    ) {
        this.id_kota = id_kota;
        this.tanggal = tanggal;
        this.nama_event = nama_event;
        this.gambar = gambar;
        this.harga_reguler = harga_reguler;
        this.detail = detail;
        this.longitude = longitude;
        this.id_admin = id_admin;
        this.id_event = id_event;
        this.harga_premium = harga_premium;
        this.deskripsi = deskripsi;
        this.latitude = latitude;
        this.lokasi = lokasi;
        this.transaksis = transaksis;
    }

    public int getId_kota() {
        return id_kota;
    }

    public void setId_kota(int id_kota) {
        this.id_kota = id_kota;
    }
    public String getTanggal() {
        return tanggal;
    }

    public void setTanggal(String tanggal) {
        this.tanggal = tanggal;
    }
    public String getNama_event() {
        return nama_event;
    }

    public void setNama_event(String nama_event) {
        this.nama_event = nama_event;
    }
    public String getGambar() {
        return gambar;
    }

    public void setGambar(String gambar) {
        this.gambar = gambar;
    }
    public int getHarga_reguler() {
        return harga_reguler;
    }

    public void setHarga_reguler(int harga_reguler) {
        this.harga_reguler = harga_reguler;
    }
    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
    public int getId_admin() {
        return id_admin;
    }

    public void setId_admin(int id_admin) {
        this.id_admin = id_admin;
    }
    public int getId_event() {
        return id_event;
    }

    public void setId_event(int id_event) {
        this.id_event = id_event;
    }
    public int getHarga_premium() {
        return harga_premium;
    }

    public void setHarga_premium(int harga_premium) {
        this.harga_premium = harga_premium;
    }
    public String getDeskripsi() {
        return deskripsi;
    }

    public void setDeskripsi(String deskripsi) {
        this.deskripsi = deskripsi;
    }
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getLokasi() {
        return lokasi;
    }

    public void setLokasi(String lokasi) {
        this.lokasi = lokasi;
    }

    public kota getKota() {
        return kota;
    }

    public void setKota(kota kota) {
        this.kota = kota;
    }
    public e_ticket getE_ticket() {
        return e_ticket;
    }

    public void setE_ticket(e_ticket e_ticket) {
        this.e_ticket = e_ticket;
    }
    public List<transaksi> getTransaksis() {
        return transaksis;
    }

    public void addTransaksi(Transaksi transaksi) {
        this.transaksis.add(transaksi);
    }

}