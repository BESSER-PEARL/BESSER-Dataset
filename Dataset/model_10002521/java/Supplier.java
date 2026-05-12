





import java.util.List;
import java.util.ArrayList;

public class Supplier  {

    private String suppID;
    private String suppName;
    private String address;





    private Product product;


    public Supplier(
        String suppID,        String suppName,        String address    ) {
        this.suppID = suppID;
        this.suppName = suppName;
        this.address = address;
    }


    public String getSuppid() {
        return suppID;
    }

    public void setSuppid(String suppID) {
        this.suppID = suppID;
    }
    public String getSuppname() {
        return suppName;
    }

    public void setSuppname(String suppName) {
        this.suppName = suppName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}