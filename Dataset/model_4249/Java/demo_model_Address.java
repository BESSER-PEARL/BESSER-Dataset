





import java.util.List;
import java.util.ArrayList;

public class demo_model_Address  {

    private String city;
    private String street;
    private String country;
    private String state;
    private int zipcode;





    private demo_model_Employee demo_model_employee;


    public demo_model_Address(
        String city,        String street,        String country,        String state,        int zipcode    ) {
        this.city = city;
        this.street = street;
        this.country = country;
        this.state = state;
        this.zipcode = zipcode;
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
    public int getZipcode() {
        return zipcode;
    }

    public void setZipcode(int zipcode) {
        this.zipcode = zipcode;
    }

    public demo_model_Employee getDemo_model_employee() {
        return demo_model_employee;
    }

    public void setDemo_model_employee(demo_model_Employee demo_model_employee) {
        this.demo_model_employee = demo_model_employee;
    }

}