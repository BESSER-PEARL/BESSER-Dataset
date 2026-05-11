





import java.util.List;
import java.util.ArrayList;

public class room_SubStateTrPointTerminal extends TransitionTerminal {






    private room_State room_state;




    private room_TrPoint room_trpoint;


    public room_SubStateTrPointTerminal(
    ) {
        super(
        );
    }



    public room_State getRoom_state() {
        return room_state;
    }

    public void setRoom_state(room_State room_state) {
        this.room_state = room_state;
    }
    public room_TrPoint getRoom_trpoint() {
        return room_trpoint;
    }

    public void setRoom_trpoint(room_TrPoint room_trpoint) {
        this.room_trpoint = room_trpoint;
    }

}