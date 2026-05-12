





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String expiry;
    private int price;
    private String manufecturedDate;
    private String color;
    private String pID;
    private String name;
    private String manufecturer;



    public Product(
        String expiry,        int price,        String manufecturedDate,        String color,        String pID,        String name,        String manufecturer    ) {
        this.expiry = expiry;
        this.price = price;
        this.manufecturedDate = manufecturedDate;
        this.color = color;
        this.pID = pID;
        this.name = name;
        this.manufecturer = manufecturer;
    }


    public String getExpiry() {
        return expiry;
    }

    public void setExpiry(String expiry) {
        this.expiry = expiry;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getManufectureddate() {
        return manufecturedDate;
    }

    public void setManufectureddate(String manufecturedDate) {
        this.manufecturedDate = manufecturedDate;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getPid() {
        return pID;
    }

    public void setPid(String pID) {
        this.pID = pID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getManufecturer() {
        return manufecturer;
    }

    public void setManufecturer(String manufecturer) {
        this.manufecturer = manufecturer;
    }


}