





import java.util.List;
import java.util.ArrayList;

public class Pemesan  {

    private String username;
    private String password;
    private String Nama;
    private String Alamat;
    private String phone_number;
    private String Emai;
    private int NIK;



    public Pemesan(
        String username,        String password,        String Nama,        String Alamat,        String phone_number,        String Emai,        int NIK    ) {
        this.username = username;
        this.password = password;
        this.Nama = Nama;
        this.Alamat = Alamat;
        this.phone_number = phone_number;
        this.Emai = Emai;
        this.NIK = NIK;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getNama() {
        return Nama;
    }

    public void setNama(String Nama) {
        this.Nama = Nama;
    }
    public String getAlamat() {
        return Alamat;
    }

    public void setAlamat(String Alamat) {
        this.Alamat = Alamat;
    }
    public String getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(String phone_number) {
        this.phone_number = phone_number;
    }
    public String getEmai() {
        return Emai;
    }

    public void setEmai(String Emai) {
        this.Emai = Emai;
    }
    public int getNik() {
        return NIK;
    }

    public void setNik(int NIK) {
        this.NIK = NIK;
    }


}