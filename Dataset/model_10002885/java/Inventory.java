





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String SuperMarket;
    private String list;





    private List<Product> products;


    public Inventory(
        String SuperMarket,        String list    ) {
        this.SuperMarket = SuperMarket;
        this.list = list;
        this.products = new ArrayList<>();
    }

    public Inventory(
        String SuperMarket,        String list        ArrayList<Product> products    ) {
        this.SuperMarket = SuperMarket;
        this.list = list;
        this.products = products;
    }

    public String getSupermarket() {
        return SuperMarket;
    }

    public void setSupermarket(String SuperMarket) {
        this.SuperMarket = SuperMarket;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}