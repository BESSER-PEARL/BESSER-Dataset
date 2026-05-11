





import java.util.List;
import java.util.ArrayList;

public class behaviour_Coordinate  {

    private float altitude;
    private float heading;
    private float latitude;
    private float longitude;





    private behaviour_Drone behaviour_drone;


    public behaviour_Coordinate(
        float altitude,        float heading,        float latitude,        float longitude    ) {
        this.altitude = altitude;
        this.heading = heading;
        this.latitude = latitude;
        this.longitude = longitude;
    }


    public float getAltitude() {
        return altitude;
    }

    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }
    public float getHeading() {
        return heading;
    }

    public void setHeading(float heading) {
        this.heading = heading;
    }
    public float getLatitude() {
        return latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }
    public float getLongitude() {
        return longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }

    public behaviour_Drone getBehaviour_drone() {
        return behaviour_drone;
    }

    public void setBehaviour_drone(behaviour_Drone behaviour_drone) {
        this.behaviour_drone = behaviour_drone;
    }

}