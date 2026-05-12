





import java.util.List;
import java.util.ArrayList;

public class register_admin  {

    private String nik;
    private String nama_lengkap;
    private int id_user;
    private String email;
    private String password;





    private admin admin;


    public register_admin(
        String nik,        String nama_lengkap,        int id_user,        String email,        String password    ) {
        this.nik = nik;
        this.nama_lengkap = nama_lengkap;
        this.id_user = id_user;
        this.email = email;
        this.password = password;
    }


    public String getNik() {
        return nik;
    }

    public void setNik(String nik) {
        this.nik = nik;
    }
    public String getNama_lengkap() {
        return nama_lengkap;
    }

    public void setNama_lengkap(String nama_lengkap) {
        this.nama_lengkap = nama_lengkap;
    }
    public int getId_user() {
        return id_user;
    }

    public void setId_user(int id_user) {
        this.id_user = id_user;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public admin getAdmin() {
        return admin;
    }

    public void setAdmin(admin admin) {
        this.admin = admin;
    }

}