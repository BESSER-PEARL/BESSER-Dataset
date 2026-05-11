





import java.util.List;
import java.util.ArrayList;

public class room_StateTerminal extends TransitionTerminal {






    private room_State room_state;


    public room_StateTerminal(
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

}