





import java.util.List;
import java.util.ArrayList;

public class Company_Organisation  {

    private String name;
    private String city;
    private String completeAddress;



    public Company_Organisation(
        String name,        String city,        String completeAddress    ) {
        this.name = name;
        this.city = city;
        this.completeAddress = completeAddress;
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
    public String getCompleteaddress() {
        return completeAddress;
    }

    public void setCompleteaddress(String completeAddress) {
        this.completeAddress = completeAddress;
    }


}