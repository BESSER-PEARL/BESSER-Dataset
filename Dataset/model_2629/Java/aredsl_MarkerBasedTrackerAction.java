





import java.util.List;
import java.util.ArrayList;

public class aredsl_MarkerBasedTrackerAction extends TrackerAction {

    private int markerId;



    public aredsl_MarkerBasedTrackerAction(
        int markerId    ) {
        super(
        );
        this.markerId = markerId;
    }


    public int getMarkerid() {
        return markerId;
    }

    public void setMarkerid(int markerId) {
        this.markerId = markerId;
    }


}