





import java.util.List;
import java.util.ArrayList;

public class Prodis  {

    private int status;
    private int user_id;
    private String prodi_name;
    private int kapasitas_max;
    private int id;



    public Prodis(
        int status,        int user_id,        String prodi_name,        int kapasitas_max,        int id    ) {
        this.status = status;
        this.user_id = user_id;
        this.prodi_name = prodi_name;
        this.kapasitas_max = kapasitas_max;
        this.id = id;
    }


    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public String getProdi_name() {
        return prodi_name;
    }

    public void setProdi_name(String prodi_name) {
        this.prodi_name = prodi_name;
    }
    public int getKapasitas_max() {
        return kapasitas_max;
    }

    public void setKapasitas_max(int kapasitas_max) {
        this.kapasitas_max = kapasitas_max;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}