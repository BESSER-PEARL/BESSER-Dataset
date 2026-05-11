





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Sensor  {

    private boolean brightness;
    private boolean air;
    private String circle;
    private boolean temp;
    private String battery;





    private SmartHouse_Room smarthouse_room;


    public SmartHouse_Sensor(
        boolean brightness,        boolean air,        String circle,        boolean temp,        String battery    ) {
        this.brightness = brightness;
        this.air = air;
        this.circle = circle;
        this.temp = temp;
        this.battery = battery;
    }


    public boolean getBrightness() {
        return brightness;
    }

    public void setBrightness(boolean brightness) {
        this.brightness = brightness;
    }
    public boolean getAir() {
        return air;
    }

    public void setAir(boolean air) {
        this.air = air;
    }
    public String getCircle() {
        return circle;
    }

    public void setCircle(String circle) {
        this.circle = circle;
    }
    public boolean getTemp() {
        return temp;
    }

    public void setTemp(boolean temp) {
        this.temp = temp;
    }
    public String getBattery() {
        return battery;
    }

    public void setBattery(String battery) {
        this.battery = battery;
    }

    public SmartHouse_Room getSmarthouse_room() {
        return smarthouse_room;
    }

    public void setSmarthouse_room(SmartHouse_Room smarthouse_room) {
        this.smarthouse_room = smarthouse_room;
    }

}