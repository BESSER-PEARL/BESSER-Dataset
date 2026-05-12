





import java.util.List;
import java.util.ArrayList;

public class Kategori  {

    private String idkategori;
    private String name;
    private String desc;
    private String productid;





    private Produk produk;


    public Kategori(
        String idkategori,        String name,        String desc,        String productid    ) {
        this.idkategori = idkategori;
        this.name = name;
        this.desc = desc;
        this.productid = productid;
    }


    public String getIdkategori() {
        return idkategori;
    }

    public void setIdkategori(String idkategori) {
        this.idkategori = idkategori;
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
    public String getProductid() {
        return productid;
    }

    public void setProductid(String productid) {
        this.productid = productid;
    }

    public Produk getProduk() {
        return produk;
    }

    public void setProduk(Produk produk) {
        this.produk = produk;
    }

}