





import java.util.List;
import java.util.ArrayList;

public class cart  {

    private None product2;
    private int id;
    private None product1;
    private String price;
    private int NumberOfProduct;
    private String total;
    private None productn;





    private customer customer;


    public cart(
        None product2,        int id,        None product1,        String price,        int NumberOfProduct,        String total,        None productn    ) {
        this.product2 = product2;
        this.id = id;
        this.product1 = product1;
        this.price = price;
        this.NumberOfProduct = NumberOfProduct;
        this.total = total;
        this.productn = productn;
    }


    public None getProduct2() {
        return product2;
    }

    public void setProduct2(None product2) {
        this.product2 = product2;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getProduct1() {
        return product1;
    }

    public void setProduct1(None product1) {
        this.product1 = product1;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getNumberofproduct() {
        return NumberOfProduct;
    }

    public void setNumberofproduct(int NumberOfProduct) {
        this.NumberOfProduct = NumberOfProduct;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }
    public None getProductn() {
        return productn;
    }

    public void setProductn(None productn) {
        this.productn = productn;
    }

    public customer getCustomer() {
        return customer;
    }

    public void setCustomer(customer customer) {
        this.customer = customer;
    }

}