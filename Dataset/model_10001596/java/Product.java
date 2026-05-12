





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int price;
    private String name;
    private String pID;
    private String color;
    private String manufecturer;
    private String manufecturedDate;
    private String expiry;





    private Person person;


    public Product(
        int price,        String name,        String pID,        String color,        String manufecturer,        String manufecturedDate,        String expiry    ) {
        this.price = price;
        this.name = name;
        this.pID = pID;
        this.color = color;
        this.manufecturer = manufecturer;
        this.manufecturedDate = manufecturedDate;
        this.expiry = expiry;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPid() {
        return pID;
    }

    public void setPid(String pID) {
        this.pID = pID;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getManufecturer() {
        return manufecturer;
    }

    public void setManufecturer(String manufecturer) {
        this.manufecturer = manufecturer;
    }
    public String getManufectureddate() {
        return manufecturedDate;
    }

    public void setManufectureddate(String manufecturedDate) {
        this.manufecturedDate = manufecturedDate;
    }
    public String getExpiry() {
        return expiry;
    }

    public void setExpiry(String expiry) {
        this.expiry = expiry;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}