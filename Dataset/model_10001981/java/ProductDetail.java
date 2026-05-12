





import java.util.List;
import java.util.ArrayList;

public class ProductDetail  {

    private int sex;
    private String productId;
    private float priceCost;
    private String brand;
    private String category;
    private String productName;



    public ProductDetail(
        int sex,        String productId,        float priceCost,        String brand,        String category,        String productName    ) {
        this.sex = sex;
        this.productId = productId;
        this.priceCost = priceCost;
        this.brand = brand;
        this.category = category;
        this.productName = productName;
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
    public float getPricecost() {
        return priceCost;
    }

    public void setPricecost(float priceCost) {
        this.priceCost = priceCost;
    }
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }


}