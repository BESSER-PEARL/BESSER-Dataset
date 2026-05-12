





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Configuration  {

    private String temp;
    private String location;



    public sourcecleaner_Configuration(
        String temp,        String location    ) {
        this.temp = temp;
        this.location = location;
    }


    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}