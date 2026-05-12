





import java.util.List;
import java.util.ArrayList;

public class LatLng  {

    private String latitude;
    private String longitude;



    public LatLng(
        String latitude,        String longitude    ) {
        this.latitude = latitude;
        this.longitude = longitude;
    }


    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }


}