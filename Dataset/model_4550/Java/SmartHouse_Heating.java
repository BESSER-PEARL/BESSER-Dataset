





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Heating  {

    private String name;
    private int level;





    private SmartHouse_Room smarthouse_room;


    public SmartHouse_Heating(
        String name,        int level    ) {
        this.name = name;
        this.level = level;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public SmartHouse_Room getSmarthouse_room() {
        return smarthouse_room;
    }

    public void setSmarthouse_room(SmartHouse_Room smarthouse_room) {
        this.smarthouse_room = smarthouse_room;
    }

}