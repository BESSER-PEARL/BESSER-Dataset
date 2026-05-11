





import java.util.List;
import java.util.ArrayList;

public class nocollectionowner_PriceCategory  {

    private String name;
    private float prices;





    private nocollectionowner_Product nocollectionowner_product;


    public nocollectionowner_PriceCategory(
        String name,        float prices    ) {
        this.name = name;
        this.prices = prices;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getPrices() {
        return prices;
    }

    public void setPrices(float prices) {
        this.prices = prices;
    }

    public nocollectionowner_Product getNocollectionowner_product() {
        return nocollectionowner_product;
    }

    public void setNocollectionowner_product(nocollectionowner_Product nocollectionowner_product) {
        this.nocollectionowner_product = nocollectionowner_product;
    }

}