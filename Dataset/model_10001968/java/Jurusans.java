





import java.util.List;
import java.util.ArrayList;

public class Jurusans  {

    private int id;
    private String jurusan_name;
    private int prodi_id;



    public Jurusans(
        int id,        String jurusan_name,        int prodi_id    ) {
        this.id = id;
        this.jurusan_name = jurusan_name;
        this.prodi_id = prodi_id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getJurusan_name() {
        return jurusan_name;
    }

    public void setJurusan_name(String jurusan_name) {
        this.jurusan_name = jurusan_name;
    }
    public int getProdi_id() {
        return prodi_id;
    }

    public void setProdi_id(int prodi_id) {
        this.prodi_id = prodi_id;
    }


}