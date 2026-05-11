





import java.util.List;
import java.util.ArrayList;

public class extendedPO2_Address  {

    private String country;
    private String name;



    public extendedPO2_Address(
        String country,        String name    ) {
        this.country = country;
        this.name = name;
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


}