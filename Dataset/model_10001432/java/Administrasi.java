





import java.util.List;
import java.util.ArrayList;

public class Administrasi  {

    private int NoPesan;
    private int IdPelanggan;
    private String Bayar;
    private int IdAdmin;
    private String Kembali;
    private String HargaSewa;





    private Admin admin;


    public Administrasi(
        int NoPesan,        int IdPelanggan,        String Bayar,        int IdAdmin,        String Kembali,        String HargaSewa    ) {
        this.NoPesan = NoPesan;
        this.IdPelanggan = IdPelanggan;
        this.Bayar = Bayar;
        this.IdAdmin = IdAdmin;
        this.Kembali = Kembali;
        this.HargaSewa = HargaSewa;
    }


    public int getNopesan() {
        return NoPesan;
    }

    public void setNopesan(int NoPesan) {
        this.NoPesan = NoPesan;
    }
    public int getIdpelanggan() {
        return IdPelanggan;
    }

    public void setIdpelanggan(int IdPelanggan) {
        this.IdPelanggan = IdPelanggan;
    }
    public String getBayar() {
        return Bayar;
    }

    public void setBayar(String Bayar) {
        this.Bayar = Bayar;
    }
    public int getIdadmin() {
        return IdAdmin;
    }

    public void setIdadmin(int IdAdmin) {
        this.IdAdmin = IdAdmin;
    }
    public String getKembali() {
        return Kembali;
    }

    public void setKembali(String Kembali) {
        this.Kembali = Kembali;
    }
    public String getHargasewa() {
        return HargaSewa;
    }

    public void setHargasewa(String HargaSewa) {
        this.HargaSewa = HargaSewa;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}