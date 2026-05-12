





import java.util.List;
import java.util.ArrayList;

public class Setting  {

    private String email;
    private int user_id;
    private String no_faximile;
    private int id;
    private String nama;
    private String alamat;
    private String logo_kampus;
    private String no_telepon;



    public Setting(
        String email,        int user_id,        String no_faximile,        int id,        String nama,        String alamat,        String logo_kampus,        String no_telepon    ) {
        this.email = email;
        this.user_id = user_id;
        this.no_faximile = no_faximile;
        this.id = id;
        this.nama = nama;
        this.alamat = alamat;
        this.logo_kampus = logo_kampus;
        this.no_telepon = no_telepon;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public String getNo_faximile() {
        return no_faximile;
    }

    public void setNo_faximile(String no_faximile) {
        this.no_faximile = no_faximile;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
    public String getLogo_kampus() {
        return logo_kampus;
    }

    public void setLogo_kampus(String logo_kampus) {
        this.logo_kampus = logo_kampus;
    }
    public String getNo_telepon() {
        return no_telepon;
    }

    public void setNo_telepon(String no_telepon) {
        this.no_telepon = no_telepon;
    }


}