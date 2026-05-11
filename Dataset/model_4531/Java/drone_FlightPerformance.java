





import java.util.List;
import java.util.ArrayList;

public class drone_FlightPerformance  {

    private float maxOperatingTemperature;
    private int minAcceleration;
    private int maxAcceleration;
    private int maxFlightTime;
    private float maxTurnRate;
    private float minTurnRate;
    private int minSpeed;
    private int maxAltitude;
    private float minOperatingTemperature;
    private int maxPayload;
    private int maxSpeed;
    private float maxDescendRate;
    private int maxFlightTimeWithMaxPayload;
    private String launchType;
    private float positionHold;
    private float maxClimbRate;





    private drone_Drone drone_drone;


    public drone_FlightPerformance(
        float maxOperatingTemperature,        int minAcceleration,        int maxAcceleration,        int maxFlightTime,        float maxTurnRate,        float minTurnRate,        int minSpeed,        int maxAltitude,        float minOperatingTemperature,        int maxPayload,        int maxSpeed,        float maxDescendRate,        int maxFlightTimeWithMaxPayload,        String launchType,        float positionHold,        float maxClimbRate    ) {
        this.maxOperatingTemperature = maxOperatingTemperature;
        this.minAcceleration = minAcceleration;
        this.maxAcceleration = maxAcceleration;
        this.maxFlightTime = maxFlightTime;
        this.maxTurnRate = maxTurnRate;
        this.minTurnRate = minTurnRate;
        this.minSpeed = minSpeed;
        this.maxAltitude = maxAltitude;
        this.minOperatingTemperature = minOperatingTemperature;
        this.maxPayload = maxPayload;
        this.maxSpeed = maxSpeed;
        this.maxDescendRate = maxDescendRate;
        this.maxFlightTimeWithMaxPayload = maxFlightTimeWithMaxPayload;
        this.launchType = launchType;
        this.positionHold = positionHold;
        this.maxClimbRate = maxClimbRate;
    }


    public float getMaxoperatingtemperature() {
        return maxOperatingTemperature;
    }

    public void setMaxoperatingtemperature(float maxOperatingTemperature) {
        this.maxOperatingTemperature = maxOperatingTemperature;
    }
    public int getMinacceleration() {
        return minAcceleration;
    }

    public void setMinacceleration(int minAcceleration) {
        this.minAcceleration = minAcceleration;
    }
    public int getMaxacceleration() {
        return maxAcceleration;
    }

    public void setMaxacceleration(int maxAcceleration) {
        this.maxAcceleration = maxAcceleration;
    }
    public int getMaxflighttime() {
        return maxFlightTime;
    }

    public void setMaxflighttime(int maxFlightTime) {
        this.maxFlightTime = maxFlightTime;
    }
    public float getMaxturnrate() {
        return maxTurnRate;
    }

    public void setMaxturnrate(float maxTurnRate) {
        this.maxTurnRate = maxTurnRate;
    }
    public float getMinturnrate() {
        return minTurnRate;
    }

    public void setMinturnrate(float minTurnRate) {
        this.minTurnRate = minTurnRate;
    }
    public int getMinspeed() {
        return minSpeed;
    }

    public void setMinspeed(int minSpeed) {
        this.minSpeed = minSpeed;
    }
    public int getMaxaltitude() {
        return maxAltitude;
    }

    public void setMaxaltitude(int maxAltitude) {
        this.maxAltitude = maxAltitude;
    }
    public float getMinoperatingtemperature() {
        return minOperatingTemperature;
    }

    public void setMinoperatingtemperature(float minOperatingTemperature) {
        this.minOperatingTemperature = minOperatingTemperature;
    }
    public int getMaxpayload() {
        return maxPayload;
    }

    public void setMaxpayload(int maxPayload) {
        this.maxPayload = maxPayload;
    }
    public int getMaxspeed() {
        return maxSpeed;
    }

    public void setMaxspeed(int maxSpeed) {
        this.maxSpeed = maxSpeed;
    }
    public float getMaxdescendrate() {
        return maxDescendRate;
    }

    public void setMaxdescendrate(float maxDescendRate) {
        this.maxDescendRate = maxDescendRate;
    }
    public int getMaxflighttimewithmaxpayload() {
        return maxFlightTimeWithMaxPayload;
    }

    public void setMaxflighttimewithmaxpayload(int maxFlightTimeWithMaxPayload) {
        this.maxFlightTimeWithMaxPayload = maxFlightTimeWithMaxPayload;
    }
    public String getLaunchtype() {
        return launchType;
    }

    public void setLaunchtype(String launchType) {
        this.launchType = launchType;
    }
    public float getPositionhold() {
        return positionHold;
    }

    public void setPositionhold(float positionHold) {
        this.positionHold = positionHold;
    }
    public float getMaxclimbrate() {
        return maxClimbRate;
    }

    public void setMaxclimbrate(float maxClimbRate) {
        this.maxClimbRate = maxClimbRate;
    }

    public drone_Drone getDrone_drone() {
        return drone_drone;
    }

    public void setDrone_drone(drone_Drone drone_drone) {
        this.drone_drone = drone_drone;
    }

}