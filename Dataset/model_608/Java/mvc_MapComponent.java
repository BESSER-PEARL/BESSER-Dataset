





import java.util.List;
import java.util.ArrayList;

public class mvc_MapComponent extends View {

    private boolean marker;
    private float longitude;
    private float latitude;



    public mvc_MapComponent(
        boolean marker,        float longitude,        float latitude    ) {
        super(
        );
        this.marker = marker;
        this.longitude = longitude;
        this.latitude = latitude;
    }


    public boolean getMarker() {
        return marker;
    }

    public void setMarker(boolean marker) {
        this.marker = marker;
    }
    public float getLongitude() {
        return longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }
    public float getLatitude() {
        return latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }


}