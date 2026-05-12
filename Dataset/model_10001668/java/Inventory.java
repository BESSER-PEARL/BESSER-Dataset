





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String list;
    private String SuperMarket;





    private Payment payment;




    private List<Product> products;


    public Inventory(
        String list,        String SuperMarket    ) {
        this.list = list;
        this.SuperMarket = SuperMarket;
        this.products = new ArrayList<>();
    }

    public Inventory(
        String list,        String SuperMarket        ArrayList<Product> products    ) {
        this.list = list;
        this.SuperMarket = SuperMarket;
        this.products = products;
    }

    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }
    public String getSupermarket() {
        return SuperMarket;
    }

    public void setSupermarket(String SuperMarket) {
        this.SuperMarket = SuperMarket;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}