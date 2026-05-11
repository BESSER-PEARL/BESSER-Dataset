





import java.util.List;
import java.util.ArrayList;

public class room_GuardedTransition extends TransitionChainStartTransition {






    private room_DetailCode room_detailcode;


    public room_GuardedTransition(
    ) {
        super(
        );
    }



    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }

}