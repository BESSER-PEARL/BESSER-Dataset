





import java.util.List;
import java.util.ArrayList;

public class sexec_TimeEvent extends Event {

    private boolean periodic;



    public sexec_TimeEvent(
        boolean periodic    ) {
        super(
        );
        this.periodic = periodic;
    }


    public boolean getPeriodic() {
        return periodic;
    }

    public void setPeriodic(boolean periodic) {
        this.periodic = periodic;
    }


}