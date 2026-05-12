





import java.util.List;
import java.util.ArrayList;

public class role  {

    private String nama_role;
    private int id;
    private String deskripsi_role;





    private user user;


    public role(
        String nama_role,        int id,        String deskripsi_role    ) {
        this.nama_role = nama_role;
        this.id = id;
        this.deskripsi_role = deskripsi_role;
    }


    public String getNama_role() {
        return nama_role;
    }

    public void setNama_role(String nama_role) {
        this.nama_role = nama_role;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDeskripsi_role() {
        return deskripsi_role;
    }

    public void setDeskripsi_role(String deskripsi_role) {
        this.deskripsi_role = deskripsi_role;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}