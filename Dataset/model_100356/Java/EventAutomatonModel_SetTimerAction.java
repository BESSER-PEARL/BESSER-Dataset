





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_SetTimerAction extends TimerAction {

    private int toValue;



    public EventAutomatonModel_SetTimerAction(
        int toValue    ) {
        super(
        );
        this.toValue = toValue;
    }


    public int getTovalue() {
        return toValue;
    }

    public void setTovalue(int toValue) {
        this.toValue = toValue;
    }


}