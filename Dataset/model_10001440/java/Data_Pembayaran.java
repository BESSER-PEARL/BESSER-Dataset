





import java.util.List;
import java.util.ArrayList;

public class Data_Pembayaran  {

    private String kode_bayar;
    private String kode_kredit;
    private int angsuranke;
    private String tanggal_bayar;
    private String keterangan;
    private int angsuran;





    private List<Admin> admins;




    private Pelanggan pelanggan;


    public Data_Pembayaran(
        String kode_bayar,        String kode_kredit,        int angsuranke,        String tanggal_bayar,        String keterangan,        int angsuran    ) {
        this.kode_bayar = kode_bayar;
        this.kode_kredit = kode_kredit;
        this.angsuranke = angsuranke;
        this.tanggal_bayar = tanggal_bayar;
        this.keterangan = keterangan;
        this.angsuran = angsuran;
        this.admins = new ArrayList<>();
    }

    public Data_Pembayaran(
        String kode_bayar,        String kode_kredit,        int angsuranke,        String tanggal_bayar,        String keterangan,        int angsuran        ArrayList<Admin> admins    ) {
        this.kode_bayar = kode_bayar;
        this.kode_kredit = kode_kredit;
        this.angsuranke = angsuranke;
        this.tanggal_bayar = tanggal_bayar;
        this.keterangan = keterangan;
        this.angsuran = angsuran;
        this.admins = admins;
    }

    public String getKode_bayar() {
        return kode_bayar;
    }

    public void setKode_bayar(String kode_bayar) {
        this.kode_bayar = kode_bayar;
    }
    public String getKode_kredit() {
        return kode_kredit;
    }

    public void setKode_kredit(String kode_kredit) {
        this.kode_kredit = kode_kredit;
    }
    public int getAngsuranke() {
        return angsuranke;
    }

    public void setAngsuranke(int angsuranke) {
        this.angsuranke = angsuranke;
    }
    public String getTanggal_bayar() {
        return tanggal_bayar;
    }

    public void setTanggal_bayar(String tanggal_bayar) {
        this.tanggal_bayar = tanggal_bayar;
    }
    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
    public int getAngsuran() {
        return angsuran;
    }

    public void setAngsuran(int angsuran) {
        this.angsuran = angsuran;
    }

    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    public void setPelanggan(Pelanggan pelanggan) {
        this.pelanggan = pelanggan;
    }

}