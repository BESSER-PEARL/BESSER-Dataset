





import java.util.List;
import java.util.ArrayList;

public class robochart_Event extends NamedElement {

    private boolean broadcast;





    private robochart_Type robochart_type;


    public robochart_Event(
        boolean broadcast    ) {
        super(
        );
        this.broadcast = broadcast;
    }


    public boolean getBroadcast() {
        return broadcast;
    }

    public void setBroadcast(boolean broadcast) {
        this.broadcast = broadcast;
    }

    public robochart_Type getRobochart_type() {
        return robochart_type;
    }

    public void setRobochart_type(robochart_Type robochart_type) {
        this.robochart_type = robochart_type;
    }

}