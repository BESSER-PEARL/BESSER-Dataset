





import java.util.List;
import java.util.ArrayList;

public class Produk  {

    private String idkategori;
    private String name;
    private String price;
    private String desc;
    private String productid;





    private Orderdetail orderdetail;


    public Produk(
        String idkategori,        String name,        String price,        String desc,        String productid    ) {
        this.idkategori = idkategori;
        this.name = name;
        this.price = price;
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
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
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

    public Orderdetail getOrderdetail() {
        return orderdetail;
    }

    public void setOrderdetail(Orderdetail orderdetail) {
        this.orderdetail = orderdetail;
    }

}