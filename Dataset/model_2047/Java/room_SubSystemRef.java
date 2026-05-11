





import java.util.List;
import java.util.ArrayList;

public class room_SubSystemRef extends ActorContainerRef {






    private room_SubSystemClass room_subsystemclass;




    private room_LogicalSystem room_logicalsystem;


    public room_SubSystemRef(
    ) {
        super(
        );
    }



    public room_SubSystemClass getRoom_subsystemclass() {
        return room_subsystemclass;
    }

    public void setRoom_subsystemclass(room_SubSystemClass room_subsystemclass) {
        this.room_subsystemclass = room_subsystemclass;
    }
    public room_LogicalSystem getRoom_logicalsystem() {
        return room_logicalsystem;
    }

    public void setRoom_logicalsystem(room_LogicalSystem room_logicalsystem) {
        this.room_logicalsystem = room_logicalsystem;
    }

}