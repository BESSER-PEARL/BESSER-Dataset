





import java.util.List;
import java.util.ArrayList;

public class ProductShow2  {

    private int sex;
    private String brand;
    private String productId;
    private String category;
    private String productName;
    private float priceCost;



    public ProductShow2(
        int sex,        String brand,        String productId,        String category,        String productName,        float priceCost    ) {
        this.sex = sex;
        this.brand = brand;
        this.productId = productId;
        this.category = category;
        this.productName = productName;
        this.priceCost = priceCost;
    }


    public int getSex() {
        return sex;
    }

    public void setSex(int sex) {
        this.sex = sex;
    }
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
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
    public float getPricecost() {
        return priceCost;
    }

    public void setPricecost(float priceCost) {
        this.priceCost = priceCost;
    }


}