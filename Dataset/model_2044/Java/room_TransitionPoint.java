





import java.util.List;
import java.util.ArrayList;

public class room_TransitionPoint extends TrPoint {

    private boolean handler;



    public room_TransitionPoint(
        boolean handler    ) {
        super(
        );
        this.handler = handler;
    }


    public boolean getHandler() {
        return handler;
    }

    public void setHandler(boolean handler) {
        this.handler = handler;
    }


}