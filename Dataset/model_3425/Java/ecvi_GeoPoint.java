





import java.util.List;
import java.util.ArrayList;

public class ecvi_GeoPoint  {

    private String lng;
    private String lat;



    public ecvi_GeoPoint(
        String lng,        String lat    ) {
        this.lng = lng;
        this.lat = lat;
    }


    public String getLng() {
        return lng;
    }

    public void setLng(String lng) {
        this.lng = lng;
    }
    public String getLat() {
        return lat;
    }

    public void setLat(String lat) {
        this.lat = lat;
    }


}