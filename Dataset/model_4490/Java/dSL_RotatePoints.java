





import java.util.List;
import java.util.ArrayList;

public class dSL_RotatePoints extends RotateMovementAction {

    private int degrees;



    public dSL_RotatePoints(
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