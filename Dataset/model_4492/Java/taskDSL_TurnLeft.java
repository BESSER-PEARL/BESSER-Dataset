





import java.util.List;
import java.util.ArrayList;

public class taskDSL_TurnLeft extends DriveAction {

    private int degrees;



    public taskDSL_TurnLeft(
        int degrees    ) {
        super(
        );
        this.degrees = degrees;
    }


    public int getDegrees() {
        return degrees;
    }

    public void setDegrees(int degrees) {
        this.degrees = degrees;
    }


}