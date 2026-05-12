





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String pID;
    private String manufecturedDate;
    private int price;
    private String expiry;
    private String manufecturer;
    private String name;
    private String color;





    private Person person;


    public Product(
        String pID,        String manufecturedDate,        int price,        String expiry,        String manufecturer,        String name,        String color    ) {
        this.pID = pID;
        this.manufecturedDate = manufecturedDate;
        this.price = price;
        this.expiry = expiry;
        this.manufecturer = manufecturer;
        this.name = name;
        this.color = color;
    }


    public String getPid() {
        return pID;
    }

    public void setPid(String pID) {
        this.pID = pID;
    }
    public String getManufectureddate() {
        return manufecturedDate;
    }

    public void setManufectureddate(String manufecturedDate) {
        this.manufecturedDate = manufecturedDate;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getExpiry() {
        return expiry;
    }

    public void setExpiry(String expiry) {
        this.expiry = expiry;
    }
    public String getManufecturer() {
        return manufecturer;
    }

    public void setManufecturer(String manufecturer) {
        this.manufecturer = manufecturer;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}