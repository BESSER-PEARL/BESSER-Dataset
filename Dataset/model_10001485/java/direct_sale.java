





import java.util.List;
import java.util.ArrayList;

public class direct_sale  {

    private String saled_products;
    private String username;
    private String attribute;





    private the_product the_product;


    public direct_sale(
        String saled_products,        String username,        String attribute    ) {
        this.saled_products = saled_products;
        this.username = username;
        this.attribute = attribute;
    }


    public String getSaled_products() {
        return saled_products;
    }

    public void setSaled_products(String saled_products) {
        this.saled_products = saled_products;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public the_product getThe_product() {
        return the_product;
    }

    public void setThe_product(the_product the_product) {
        this.the_product = the_product;
    }

}