





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String streetnumber;
    private String country;
    private String street;
    private String city;
    private String zipCode;





    private ContentPage contentpage;


    public Address(
        String streetnumber,        String country,        String street,        String city,        String zipCode    ) {
        this.streetnumber = streetnumber;
        this.country = country;
        this.street = street;
        this.city = city;
        this.zipCode = zipCode;
    }


    public String getStreetnumber() {
        return streetnumber;
    }

    public void setStreetnumber(String streetnumber) {
        this.streetnumber = streetnumber;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }

    public ContentPage getContentpage() {
        return contentpage;
    }

    public void setContentpage(ContentPage contentpage) {
        this.contentpage = contentpage;
    }

}