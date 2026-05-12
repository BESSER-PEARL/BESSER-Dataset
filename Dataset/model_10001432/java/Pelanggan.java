





import java.util.List;
import java.util.ArrayList;

public class Pelanggan  {

    private String Pekerjaan;
    private String Username;
    private String NoKTP;
    private int IdPelanggan;
    private String JenisKelamin;
    private String Alamat;
    private int Umur;
    private String Telepon;
    private String Password;





    private Admin admin;


    public Pelanggan(
        String Pekerjaan,        String Username,        String NoKTP,        int IdPelanggan,        String JenisKelamin,        String Alamat,        int Umur,        String Telepon,        String Password    ) {
        this.Pekerjaan = Pekerjaan;
        this.Username = Username;
        this.NoKTP = NoKTP;
        this.IdPelanggan = IdPelanggan;
        this.JenisKelamin = JenisKelamin;
        this.Alamat = Alamat;
        this.Umur = Umur;
        this.Telepon = Telepon;
        this.Password = Password;
    }


    public String getPekerjaan() {
        return Pekerjaan;
    }

    public void setPekerjaan(String Pekerjaan) {
        this.Pekerjaan = Pekerjaan;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getNoktp() {
        return NoKTP;
    }

    public void setNoktp(String NoKTP) {
        this.NoKTP = NoKTP;
    }
    public int getIdpelanggan() {
        return IdPelanggan;
    }

    public void setIdpelanggan(int IdPelanggan) {
        this.IdPelanggan = IdPelanggan;
    }
    public String getJeniskelamin() {
        return JenisKelamin;
    }

    public void setJeniskelamin(String JenisKelamin) {
        this.JenisKelamin = JenisKelamin;
    }
    public String getAlamat() {
        return Alamat;
    }

    public void setAlamat(String Alamat) {
        this.Alamat = Alamat;
    }
    public int getUmur() {
        return Umur;
    }

    public void setUmur(int Umur) {
        this.Umur = Umur;
    }
    public String getTelepon() {
        return Telepon;
    }

    public void setTelepon(String Telepon) {
        this.Telepon = Telepon;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}