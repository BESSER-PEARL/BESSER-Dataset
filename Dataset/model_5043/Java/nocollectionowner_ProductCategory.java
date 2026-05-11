





import java.util.List;
import java.util.ArrayList;

public class nocollectionowner_ProductCategory  {

    private String name;





    private nocollectionowner_ProductCategory nocollectionowner_productcategory;




    private List<nocollectionowner_ProductCategory> nocollectionowner_productcategorys;




    private List<nocollectionowner_Product> nocollectionowner_products;




    private nocollectionowner_Product nocollectionowner_product;


    public nocollectionowner_ProductCategory(
        String name    ) {
        this.name = name;
        this.nocollectionowner_productcategorys = new ArrayList<>();
        this.nocollectionowner_products = new ArrayList<>();
    }

    public nocollectionowner_ProductCategory(
        String name        ArrayList<nocollectionowner_ProductCategory> nocollectionowner_productcategorys,        ArrayList<nocollectionowner_Product> nocollectionowner_products    ) {
        this.name = name;
        this.nocollectionowner_productcategorys = nocollectionowner_productcategorys;
        this.nocollectionowner_products = nocollectionowner_products;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nocollectionowner_ProductCategory getNocollectionowner_productcategory() {
        return nocollectionowner_productcategory;
    }

    public void setNocollectionowner_productcategory(nocollectionowner_ProductCategory nocollectionowner_productcategory) {
        this.nocollectionowner_productcategory = nocollectionowner_productcategory;
    }
    public List<nocollectionowner_ProductCategory> getNocollectionowner_productcategorys() {
        return nocollectionowner_productcategorys;
    }

    public void addNocollectionowner_productcategory(Nocollectionowner_productcategory nocollectionowner_productcategory) {
        this.nocollectionowner_productcategorys.add(nocollectionowner_productcategory);
    }
    public List<nocollectionowner_Product> getNocollectionowner_products() {
        return nocollectionowner_products;
    }

    public void addNocollectionowner_product(Nocollectionowner_product nocollectionowner_product) {
        this.nocollectionowner_products.add(nocollectionowner_product);
    }
    public nocollectionowner_Product getNocollectionowner_product() {
        return nocollectionowner_product;
    }

    public void setNocollectionowner_product(nocollectionowner_Product nocollectionowner_product) {
        this.nocollectionowner_product = nocollectionowner_product;
    }

}