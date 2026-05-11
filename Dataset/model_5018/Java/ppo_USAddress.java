





import java.util.List;
import java.util.ArrayList;

public class ppo_USAddress  {

    private String street;
    private int zip;
    private String city;
    private String country;
    private String name;
    private String state;





    private ppo_PurchaseOrder ppo_purchaseorder;




    private ppo_PurchaseOrder ppo_purchaseorder;


    public ppo_USAddress(
        String street,        int zip,        String city,        String country,        String name,        String state    ) {
        this.street = street;
        this.zip = zip;
        this.city = city;
        this.country = country;
        this.name = name;
        this.state = state;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public ppo_PurchaseOrder getPpo_purchaseorder() {
        return ppo_purchaseorder;
    }

    public void setPpo_purchaseorder(ppo_PurchaseOrder ppo_purchaseorder) {
        this.ppo_purchaseorder = ppo_purchaseorder;
    }
    public ppo_PurchaseOrder getPpo_purchaseorder() {
        return ppo_purchaseorder;
    }

    public void setPpo_purchaseorder(ppo_PurchaseOrder ppo_purchaseorder) {
        this.ppo_purchaseorder = ppo_purchaseorder;
    }

}