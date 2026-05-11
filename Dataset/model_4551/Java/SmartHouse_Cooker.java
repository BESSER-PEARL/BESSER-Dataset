





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Cooker  {

    private boolean on;





    private SmartHouse_Room smarthouse_room;


    public SmartHouse_Cooker(
        boolean on    ) {
        this.on = on;
    }


    public boolean getOn() {
        return on;
    }

    public void setOn(boolean on) {
        this.on = on;
    }

    public SmartHouse_Room getSmarthouse_room() {
        return smarthouse_room;
    }

    public void setSmarthouse_room(SmartHouse_Room smarthouse_room) {
        this.smarthouse_room = smarthouse_room;
    }

}