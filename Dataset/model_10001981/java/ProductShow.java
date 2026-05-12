





import java.util.List;
import java.util.ArrayList;

public class ProductShow  {

    private int sex;
    private String productId;
    private String productName;
    private String brand;
    private String image;
    private String category;
    private float priceSale;



    public ProductShow(
        int sex,        String productId,        String productName,        String brand,        String image,        String category,        float priceSale    ) {
        this.sex = sex;
        this.productId = productId;
        this.productName = productName;
        this.brand = brand;
        this.image = image;
        this.category = category;
        this.priceSale = priceSale;
    }


    public int getSex() {
        return sex;
    }

    public void setSex(int sex) {
        this.sex = sex;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public float getPricesale() {
        return priceSale;
    }

    public void setPricesale(float priceSale) {
        this.priceSale = priceSale;
    }


}