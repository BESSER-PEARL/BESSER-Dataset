





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Light  {

    private String level;





    private SmartHouse_Room smarthouse_room;


    public SmartHouse_Light(
        String level    ) {
        this.level = level;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public SmartHouse_Room getSmarthouse_room() {
        return smarthouse_room;
    }

    public void setSmarthouse_room(SmartHouse_Room smarthouse_room) {
        this.smarthouse_room = smarthouse_room;
    }

}