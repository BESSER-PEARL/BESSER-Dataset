





import java.util.List;
import java.util.ArrayList;

public class company_Addressable  {

    private String name;
    private String city;
    private String street;



    public company_Addressable(
        String name,        String city,        String street    ) {
        this.name = name;
        this.city = city;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}