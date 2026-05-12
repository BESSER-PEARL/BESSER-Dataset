





import java.util.List;
import java.util.ArrayList;

public class Kategori  {

    private String idkategori;
    private String productid;
    private String name;
    private String desc;





    private Produk produk;


    public Kategori(
        String idkategori,        String productid,        String name,        String desc    ) {
        this.idkategori = idkategori;
        this.productid = productid;
        this.name = name;
        this.desc = desc;
    }


    public String getIdkategori() {
        return idkategori;
    }

    public void setIdkategori(String idkategori) {
        this.idkategori = idkategori;
    }
    public String getProductid() {
        return productid;
    }

    public void setProductid(String productid) {
        this.productid = productid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public Produk getProduk() {
        return produk;
    }

    public void setProduk(Produk produk) {
        this.produk = produk;
    }

}