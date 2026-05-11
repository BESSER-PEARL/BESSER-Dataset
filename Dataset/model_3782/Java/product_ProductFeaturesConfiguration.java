





import java.util.List;
import java.util.ArrayList;

public class product_ProductFeaturesConfiguration  {

    private String attribute;
    private String name;





    private product_Product product_product;


    public product_ProductFeaturesConfiguration(
        String attribute,        String name    ) {
        this.attribute = attribute;
        this.name = name;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public product_Product getProduct_product() {
        return product_product;
    }

    public void setProduct_product(product_Product product_product) {
        this.product_product = product_product;
    }

}