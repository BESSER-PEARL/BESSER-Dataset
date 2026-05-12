





import java.util.List;
import java.util.ArrayList;

public class produk  {

    private int id_produk;
    private String foto_produk;
    private String website;



    public produk(
        int id_produk,        String foto_produk,        String website    ) {
        this.id_produk = id_produk;
        this.foto_produk = foto_produk;
        this.website = website;
    }


    public int getId_produk() {
        return id_produk;
    }

    public void setId_produk(int id_produk) {
        this.id_produk = id_produk;
    }
    public String getFoto_produk() {
        return foto_produk;
    }

    public void setFoto_produk(String foto_produk) {
        this.foto_produk = foto_produk;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }


}