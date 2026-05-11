





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Window  {

    private String name;
    private boolean curtainOn;
    private boolean opened;





    private SmartHouse_Room smarthouse_room;


    public SmartHouse_Window(
        String name,        boolean curtainOn,        boolean opened    ) {
        this.name = name;
        this.curtainOn = curtainOn;
        this.opened = opened;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getCurtainon() {
        return curtainOn;
    }

    public void setCurtainon(boolean curtainOn) {
        this.curtainOn = curtainOn;
    }
    public boolean getOpened() {
        return opened;
    }

    public void setOpened(boolean opened) {
        this.opened = opened;
    }

    public SmartHouse_Room getSmarthouse_room() {
        return smarthouse_room;
    }

    public void setSmarthouse_room(SmartHouse_Room smarthouse_room) {
        this.smarthouse_room = smarthouse_room;
    }

}