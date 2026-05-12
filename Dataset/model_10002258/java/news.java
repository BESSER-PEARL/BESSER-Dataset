





import java.util.List;
import java.util.ArrayList;

public class news  {

    private String foto_news;
    private String isi_news;
    private int id_news;
    private String judul_news;



    public news(
        String foto_news,        String isi_news,        int id_news,        String judul_news    ) {
        this.foto_news = foto_news;
        this.isi_news = isi_news;
        this.id_news = id_news;
        this.judul_news = judul_news;
    }


    public String getFoto_news() {
        return foto_news;
    }

    public void setFoto_news(String foto_news) {
        this.foto_news = foto_news;
    }
    public String getIsi_news() {
        return isi_news;
    }

    public void setIsi_news(String isi_news) {
        this.isi_news = isi_news;
    }
    public int getId_news() {
        return id_news;
    }

    public void setId_news(int id_news) {
        this.id_news = id_news;
    }
    public String getJudul_news() {
        return judul_news;
    }

    public void setJudul_news(String judul_news) {
        this.judul_news = judul_news;
    }


}