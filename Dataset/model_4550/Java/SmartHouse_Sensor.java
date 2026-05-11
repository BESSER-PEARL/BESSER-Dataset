





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Sensor  {

    private String battery;
    private boolean air;
    private boolean temp;
    private boolean brightness;
    private String circle;





    private SmartHouse_Room smarthouse_room;


    public SmartHouse_Sensor(
        String battery,        boolean air,        boolean temp,        boolean brightness,        String circle    ) {
        this.battery = battery;
        this.air = air;
        this.temp = temp;
        this.brightness = brightness;
        this.circle = circle;
    }


    public String getBattery() {
        return battery;
    }

    public void setBattery(String battery) {
        this.battery = battery;
    }
    public boolean getAir() {
        return air;
    }

    public void setAir(boolean air) {
        this.air = air;
    }
    public boolean getTemp() {
        return temp;
    }

    public void setTemp(boolean temp) {
        this.temp = temp;
    }
    public boolean getBrightness() {
        return brightness;
    }

    public void setBrightness(boolean brightness) {
        this.brightness = brightness;
    }
    public String getCircle() {
        return circle;
    }

    public void setCircle(String circle) {
        this.circle = circle;
    }

    public SmartHouse_Room getSmarthouse_room() {
        return smarthouse_room;
    }

    public void setSmarthouse_room(SmartHouse_Room smarthouse_room) {
        this.smarthouse_room = smarthouse_room;
    }

}