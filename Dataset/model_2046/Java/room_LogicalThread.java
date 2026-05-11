





import java.util.List;
import java.util.ArrayList;

public class room_LogicalThread  {

    private int prio;
    private String name;





    private room_SubSystemClass room_subsystemclass;


    public room_LogicalThread(
        int prio,        String name    ) {
        this.prio = prio;
        this.name = name;
    }


    public int getPrio() {
        return prio;
    }

    public void setPrio(int prio) {
        this.prio = prio;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_SubSystemClass getRoom_subsystemclass() {
        return room_subsystemclass;
    }

    public void setRoom_subsystemclass(room_SubSystemClass room_subsystemclass) {
        this.room_subsystemclass = room_subsystemclass;
    }

}