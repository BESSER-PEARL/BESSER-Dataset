





import java.util.List;
import java.util.ArrayList;

public class commons_Geolocation  {

    private String longitude;
    private String latitude;
    private String elevation;



    public commons_Geolocation(
        String longitude,        String latitude,        String elevation    ) {
        this.longitude = longitude;
        this.latitude = latitude;
        this.elevation = elevation;
    }


    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getElevation() {
        return elevation;
    }

    public void setElevation(String elevation) {
        this.elevation = elevation;
    }


}