





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String nama;
    private String id;
    private String alamat;
    private int no_tlp;





    private Login_Admin login_admin;


    public Admin(
        String nama,        String id,        String alamat,        int no_tlp    ) {
        this.nama = nama;
        this.id = id;
        this.alamat = alamat;
        this.no_tlp = no_tlp;
    }


    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }
    public int getNo_tlp() {
        return no_tlp;
    }

    public void setNo_tlp(int no_tlp) {
        this.no_tlp = no_tlp;
    }

    public Login_Admin getLogin_admin() {
        return login_admin;
    }

    public void setLogin_admin(Login_Admin login_admin) {
        this.login_admin = login_admin;
    }

}