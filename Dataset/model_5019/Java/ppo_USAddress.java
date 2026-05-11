





import java.util.List;
import java.util.ArrayList;

public class ppo_USAddress  {

    private String name;
    private String city;
    private int zip;
    private String country;
    private String state;
    private String street;





    private ppo_PurchaseOrder ppo_purchaseorder;




    private ppo_PurchaseOrder ppo_purchaseorder;


    public ppo_USAddress(
        String name,        String city,        int zip,        String country,        String state,        String street    ) {
        this.name = name;
        this.city = city;
        this.zip = zip;
        this.country = country;
        this.state = state;
        this.street = street;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
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