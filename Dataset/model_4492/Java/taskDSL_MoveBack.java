





import java.util.List;
import java.util.ArrayList;

public class taskDSL_MoveBack extends DriveAction {

    private int meters;



    public taskDSL_MoveBack(
        int meters    ) {
        super(
        );
        this.meters = meters;
    }


    public int getMeters() {
        return meters;
    }

    public void setMeters(int meters) {
        this.meters = meters;
    }


}