





import java.util.List;
import java.util.ArrayList;

public class masterKategori  {

    private int user_id;
    private String nama_kategori;
    private int status;
    private int id;



    public masterKategori(
        int user_id,        String nama_kategori,        int status,        int id    ) {
        this.user_id = user_id;
        this.nama_kategori = nama_kategori;
        this.status = status;
        this.id = id;
    }


    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public String getNama_kategori() {
        return nama_kategori;
    }

    public void setNama_kategori(String nama_kategori) {
        this.nama_kategori = nama_kategori;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}