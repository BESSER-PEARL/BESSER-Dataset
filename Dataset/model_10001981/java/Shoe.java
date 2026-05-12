





import java.util.List;
import java.util.ArrayList;

public class Shoe  {

    private String color;
    private String productId;
    private int size;
    private String brand2;
    private float priceCost;
    private String brand;
    private int sex;
    private String description;
    private String productName;
    private String category;



    public Shoe(
        String color,        String productId,        int size,        String brand2,        float priceCost,        String brand,        int sex,        String description,        String productName,        String category    ) {
        this.color = color;
        this.productId = productId;
        this.size = size;
        this.brand2 = brand2;
        this.priceCost = priceCost;
        this.brand = brand;
        this.sex = sex;
        this.description = description;
        this.productName = productName;
        this.category = category;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getBrand2() {
        return brand2;
    }

    public void setBrand2(String brand2) {
        this.brand2 = brand2;
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
    public int getSex() {
        return sex;
    }

    public void setSex(int sex) {
        this.sex = sex;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}