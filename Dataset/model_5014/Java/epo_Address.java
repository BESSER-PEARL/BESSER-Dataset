





import java.util.List;
import java.util.ArrayList;

public class epo_Address  {

    private String name;
    private String country;



    public epo_Address(
        String name,        String country    ) {
        this.name = name;
        this.country = country;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }


}