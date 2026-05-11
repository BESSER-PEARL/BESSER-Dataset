





import java.util.List;
import java.util.ArrayList;

public class RobotWork_GoForward extends Action {

    private int cm;



    public RobotWork_GoForward(
        int cm    ) {
        super(
        );
        this.cm = cm;
    }


    public int getCm() {
        return cm;
    }

    public void setCm(int cm) {
        this.cm = cm;
    }


}