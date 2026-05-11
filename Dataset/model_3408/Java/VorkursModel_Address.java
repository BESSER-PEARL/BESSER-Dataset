





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Address  {

    private String state;
    private String city;
    private String street;
    private String zip;





    private VorkursModel_Contact vorkursmodel_contact;


    public VorkursModel_Address(
        String state,        String city,        String street,        String zip    ) {
        this.state = state;
        this.city = city;
        this.street = street;
        this.zip = zip;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }

    public VorkursModel_Contact getVorkursmodel_contact() {
        return vorkursmodel_contact;
    }

    public void setVorkursmodel_contact(VorkursModel_Contact vorkursmodel_contact) {
        this.vorkursmodel_contact = vorkursmodel_contact;
    }

}