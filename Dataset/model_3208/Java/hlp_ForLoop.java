





import java.util.List;
import java.util.ArrayList;

public class hlp_ForLoop extends Loop {

    private boolean incrementing;



    public hlp_ForLoop(
        boolean incrementing    ) {
        super(
        );
        this.incrementing = incrementing;
    }


    public boolean getIncrementing() {
        return incrementing;
    }

    public void setIncrementing(boolean incrementing) {
        this.incrementing = incrementing;
    }


}