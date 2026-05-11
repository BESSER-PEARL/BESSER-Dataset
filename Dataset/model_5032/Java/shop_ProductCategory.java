





import java.util.List;
import java.util.ArrayList;

public class shop_ProductCategory  {

    private String name;





    private List<shop_Product> shop_products;




    private shop_ProductCategory shop_productcategory;




    private shop_Product shop_product;




    private shop_ProductCategory shop_productcategory;


    public shop_ProductCategory(
        String name    ) {
        this.name = name;
        this.shop_products = new ArrayList<>();
    }

    public shop_ProductCategory(
        String name        ArrayList<shop_Product> shop_products    ) {
        this.name = name;
        this.shop_products = shop_products;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<shop_Product> getShop_products() {
        return shop_products;
    }

    public void addShop_product(Shop_product shop_product) {
        this.shop_products.add(shop_product);
    }
    public shop_ProductCategory getShop_productcategory() {
        return shop_productcategory;
    }

    public void setShop_productcategory(shop_ProductCategory shop_productcategory) {
        this.shop_productcategory = shop_productcategory;
    }
    public shop_Product getShop_product() {
        return shop_product;
    }

    public void setShop_product(shop_Product shop_product) {
        this.shop_product = shop_product;
    }
    public shop_ProductCategory getShop_productcategory() {
        return shop_productcategory;
    }

    public void setShop_productcategory(shop_ProductCategory shop_productcategory) {
        this.shop_productcategory = shop_productcategory;
    }

}