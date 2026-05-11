





import java.util.List;
import java.util.ArrayList;

public class schemaprimerpo_USAddress  {

    private String zip;
    private String state;
    private String street;
    private String country;
    private String name;
    private String city;





    private schemaprimerpo_PurchaseOrder schemaprimerpo_purchaseorder;




    private schemaprimerpo_PurchaseOrder schemaprimerpo_purchaseorder;


    public schemaprimerpo_USAddress(
        String zip,        String state,        String street,        String country,        String name,        String city    ) {
        this.zip = zip;
        this.state = state;
        this.street = street;
        this.country = country;
        this.name = name;
        this.city = city;
    }


    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
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
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public schemaprimerpo_PurchaseOrder getSchemaprimerpo_purchaseorder() {
        return schemaprimerpo_purchaseorder;
    }

    public void setSchemaprimerpo_purchaseorder(schemaprimerpo_PurchaseOrder schemaprimerpo_purchaseorder) {
        this.schemaprimerpo_purchaseorder = schemaprimerpo_purchaseorder;
    }
    public schemaprimerpo_PurchaseOrder getSchemaprimerpo_purchaseorder() {
        return schemaprimerpo_purchaseorder;
    }

    public void setSchemaprimerpo_purchaseorder(schemaprimerpo_PurchaseOrder schemaprimerpo_purchaseorder) {
        this.schemaprimerpo_purchaseorder = schemaprimerpo_purchaseorder;
    }

}