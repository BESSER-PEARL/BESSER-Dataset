





import java.util.List;
import java.util.ArrayList;

public class shop_PriceCategory  {

    private String name;
    private float prices;





    private shop_Product shop_product;


    public shop_PriceCategory(
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

    public shop_Product getShop_product() {
        return shop_product;
    }

    public void setShop_product(shop_Product shop_product) {
        this.shop_product = shop_product;
    }

}