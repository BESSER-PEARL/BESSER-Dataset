





import java.util.List;
import java.util.ArrayList;

public class ppo_USAddress  {

    private String city;
    private String country;
    private String state;
    private String street;
    private int zip;
    private String name;





    private ppo_PurchaseOrder ppo_purchaseorder;




    private ppo_PurchaseOrder ppo_purchaseorder;


    public ppo_USAddress(
        String city,        String country,        String state,        String street,        int zip,        String name    ) {
        this.city = city;
        this.country = country;
        this.state = state;
        this.street = street;
        this.zip = zip;
        this.name = name;
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
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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