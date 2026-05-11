





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_EV  {

    private boolean charging;
    private boolean pluged;
    private String level;
    private String name;



    public SmartHouse_EV(
        boolean charging,        boolean pluged,        String level,        String name    ) {
        this.charging = charging;
        this.pluged = pluged;
        this.level = level;
        this.name = name;
    }


    public boolean getCharging() {
        return charging;
    }

    public void setCharging(boolean charging) {
        this.charging = charging;
    }
    public boolean getPluged() {
        return pluged;
    }

    public void setPluged(boolean pluged) {
        this.pluged = pluged;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}