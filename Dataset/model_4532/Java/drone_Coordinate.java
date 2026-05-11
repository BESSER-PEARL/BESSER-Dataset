





import java.util.List;
import java.util.ArrayList;

public class drone_Coordinate  {

    private float longitude;
    private float altitude;
    private float latitude;





    private drone_Position drone_position;


    public drone_Coordinate(
        float longitude,        float altitude,        float latitude    ) {
        this.longitude = longitude;
        this.altitude = altitude;
        this.latitude = latitude;
    }


    public float getLongitude() {
        return longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }
    public float getAltitude() {
        return altitude;
    }

    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }
    public float getLatitude() {
        return latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }

    public drone_Position getDrone_position() {
        return drone_position;
    }

    public void setDrone_position(drone_Position drone_position) {
        this.drone_position = drone_position;
    }

}