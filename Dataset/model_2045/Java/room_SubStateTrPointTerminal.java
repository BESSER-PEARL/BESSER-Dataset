





import java.util.List;
import java.util.ArrayList;

public class room_SubStateTrPointTerminal extends TransitionTerminal {






    private room_BaseState room_basestate;




    private room_TrPoint room_trpoint;


    public room_SubStateTrPointTerminal(
    ) {
        super(
        );
    }



    public room_BaseState getRoom_basestate() {
        return room_basestate;
    }

    public void setRoom_basestate(room_BaseState room_basestate) {
        this.room_basestate = room_basestate;
    }
    public room_TrPoint getRoom_trpoint() {
        return room_trpoint;
    }

    public void setRoom_trpoint(room_TrPoint room_trpoint) {
        this.room_trpoint = room_trpoint;
    }

}