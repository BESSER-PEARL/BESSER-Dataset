





import java.util.List;
import java.util.ArrayList;

public class mission_Coordinate  {

    private float altitude;
    private float latitude;
    private float longitude;





    private mission_Drone mission_drone;


    public mission_Coordinate(
        float altitude,        float latitude,        float longitude    ) {
        this.altitude = altitude;
        this.latitude = latitude;
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
    public float getLongitude() {
        return longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }

    public mission_Drone getMission_drone() {
        return mission_drone;
    }

    public void setMission_drone(mission_Drone mission_drone) {
        this.mission_drone = mission_drone;
    }

}