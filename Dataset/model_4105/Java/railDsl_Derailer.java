





import java.util.List;
import java.util.ArrayList;

public class railDsl_Derailer extends SegmentObject {

    private boolean active;



    public railDsl_Derailer(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }


}