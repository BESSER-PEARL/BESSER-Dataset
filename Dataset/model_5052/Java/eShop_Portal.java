





import java.util.List;
import java.util.ArrayList;

public class eShop_Portal  {

    private String url;
    private String name;





    private List<eShop_Customer> eshop_customers;




    private eShop_Customer eshop_customer;


    public eShop_Portal(
        String url,        String name    ) {
        this.url = url;
        this.name = name;
        this.eshop_customers = new ArrayList<>();
    }

    public eShop_Portal(
        String url,        String name        ArrayList<eShop_Customer> eshop_customers    ) {
        this.url = url;
        this.name = name;
        this.eshop_customers = eshop_customers;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eShop_Customer> getEshop_customers() {
        return eshop_customers;
    }

    public void addEshop_customer(Eshop_customer eshop_customer) {
        this.eshop_customers.add(eshop_customer);
    }
    public eShop_Customer getEshop_customer() {
        return eshop_customer;
    }

    public void setEshop_customer(eShop_Customer eshop_customer) {
        this.eshop_customer = eshop_customer;
    }

}