





import java.util.List;
import java.util.ArrayList;

public class Pesan  {

    private int NoPesan;
    private String TanggalRental;
    private String TanggalKembali;
    private int IdPelanggan;





    private Admin admin;




    private Administrasi administrasi;




    private Pelanggan pelanggan;


    public Pesan(
        int NoPesan,        String TanggalRental,        String TanggalKembali,        int IdPelanggan    ) {
        this.NoPesan = NoPesan;
        this.TanggalRental = TanggalRental;
        this.TanggalKembali = TanggalKembali;
        this.IdPelanggan = IdPelanggan;
    }


    public int getNopesan() {
        return NoPesan;
    }

    public void setNopesan(int NoPesan) {
        this.NoPesan = NoPesan;
    }
    public String getTanggalrental() {
        return TanggalRental;
    }

    public void setTanggalrental(String TanggalRental) {
        this.TanggalRental = TanggalRental;
    }
    public String getTanggalkembali() {
        return TanggalKembali;
    }

    public void setTanggalkembali(String TanggalKembali) {
        this.TanggalKembali = TanggalKembali;
    }
    public int getIdpelanggan() {
        return IdPelanggan;
    }

    public void setIdpelanggan(int IdPelanggan) {
        this.IdPelanggan = IdPelanggan;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Administrasi getAdministrasi() {
        return administrasi;
    }

    public void setAdministrasi(Administrasi administrasi) {
        this.administrasi = administrasi;
    }
    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    public void setPelanggan(Pelanggan pelanggan) {
        this.pelanggan = pelanggan;
    }

}