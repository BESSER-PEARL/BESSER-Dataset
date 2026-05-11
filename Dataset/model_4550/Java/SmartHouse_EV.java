





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_EV  {

    private boolean charging;
    private String name;
    private String level;
    private boolean pluged;





    private SmartHouse_House smarthouse_house;




    private SmartHouse_House smarthouse_house;


    public SmartHouse_EV(
        boolean charging,        String name,        String level,        boolean pluged    ) {
        this.charging = charging;
        this.name = name;
        this.level = level;
        this.pluged = pluged;
    }


    public boolean getCharging() {
        return charging;
    }

    public void setCharging(boolean charging) {
        this.charging = charging;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public boolean getPluged() {
        return pluged;
    }

    public void setPluged(boolean pluged) {
        this.pluged = pluged;
    }

    public SmartHouse_House getSmarthouse_house() {
        return smarthouse_house;
    }

    public void setSmarthouse_house(SmartHouse_House smarthouse_house) {
        this.smarthouse_house = smarthouse_house;
    }
    public SmartHouse_House getSmarthouse_house() {
        return smarthouse_house;
    }

    public void setSmarthouse_house(SmartHouse_House smarthouse_house) {
        this.smarthouse_house = smarthouse_house;
    }

}