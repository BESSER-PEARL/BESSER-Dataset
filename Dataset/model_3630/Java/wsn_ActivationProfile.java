





import java.util.List;
import java.util.ArrayList;

public class wsn_ActivationProfile  {

    private String specific;
    private String actuator;
    private String dongle;
    private String sensor;
    private String battery;
    private int value;
    private String ch;
    private String neighbors;





    private wsn_Task wsn_task;


    public wsn_ActivationProfile(
        String specific,        String actuator,        String dongle,        String sensor,        String battery,        int value,        String ch,        String neighbors    ) {
        this.specific = specific;
        this.actuator = actuator;
        this.dongle = dongle;
        this.sensor = sensor;
        this.battery = battery;
        this.value = value;
        this.ch = ch;
        this.neighbors = neighbors;
    }


    public String getSpecific() {
        return specific;
    }

    public void setSpecific(String specific) {
        this.specific = specific;
    }
    public String getActuator() {
        return actuator;
    }

    public void setActuator(String actuator) {
        this.actuator = actuator;
    }
    public String getDongle() {
        return dongle;
    }

    public void setDongle(String dongle) {
        this.dongle = dongle;
    }
    public String getSensor() {
        return sensor;
    }

    public void setSensor(String sensor) {
        this.sensor = sensor;
    }
    public String getBattery() {
        return battery;
    }

    public void setBattery(String battery) {
        this.battery = battery;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getCh() {
        return ch;
    }

    public void setCh(String ch) {
        this.ch = ch;
    }
    public String getNeighbors() {
        return neighbors;
    }

    public void setNeighbors(String neighbors) {
        this.neighbors = neighbors;
    }

    public wsn_Task getWsn_task() {
        return wsn_task;
    }

    public void setWsn_task(wsn_Task wsn_task) {
        this.wsn_task = wsn_task;
    }

}