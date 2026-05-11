





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_WaterHeater  {

    private boolean on;
    private String temp;
    private boolean boost;





    private SmartHouse_House smarthouse_house;




    private SmartHouse_House smarthouse_house;


    public SmartHouse_WaterHeater(
        boolean on,        String temp,        boolean boost    ) {
        this.on = on;
        this.temp = temp;
        this.boost = boost;
    }


    public boolean getOn() {
        return on;
    }

    public void setOn(boolean on) {
        this.on = on;
    }
    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
    public boolean getBoost() {
        return boost;
    }

    public void setBoost(boolean boost) {
        this.boost = boost;
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