





import java.util.List;
import java.util.ArrayList;

public class model1_Address  {

    private String name;
    private String street;
    private String city;



    public model1_Address(
        String name,        String street,        String city    ) {
        this.name = name;
        this.street = street;
        this.city = city;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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


}