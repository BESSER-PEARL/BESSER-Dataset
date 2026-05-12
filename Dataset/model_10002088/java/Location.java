





import java.util.List;
import java.util.ArrayList;

public class Location  {

    private String Latitude;
    private String Longitude;



    public Location(
        String Latitude,        String Longitude    ) {
        this.Latitude = Latitude;
        this.Longitude = Longitude;
    }


    public String getLatitude() {
        return Latitude;
    }

    public void setLatitude(String Latitude) {
        this.Latitude = Latitude;
    }
    public String getLongitude() {
        return Longitude;
    }

    public void setLongitude(String Longitude) {
        this.Longitude = Longitude;
    }


}