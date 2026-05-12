





import java.util.List;
import java.util.ArrayList;

public class Pelanggan  {

    private String nama;
    private String alamat;
    private String kode_pelanggan;





    private List<Admin> admins;


    public Pelanggan(
        String nama,        String alamat,        String kode_pelanggan    ) {
        this.nama = nama;
        this.alamat = alamat;
        this.kode_pelanggan = kode_pelanggan;
        this.admins = new ArrayList<>();
    }

    public Pelanggan(
        String nama,        String alamat,        String kode_pelanggan        ArrayList<Admin> admins    ) {
        this.nama = nama;
        this.alamat = alamat;
        this.kode_pelanggan = kode_pelanggan;
        this.admins = admins;
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }
    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }
    public String getKode_pelanggan() {
        return kode_pelanggan;
    }

    public void setKode_pelanggan(String kode_pelanggan) {
        this.kode_pelanggan = kode_pelanggan;
    }

    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}