





import java.util.List;
import java.util.ArrayList;

public class cstat1_Transition  {

    private String event;
    private String guard;



    public cstat1_Transition(
        String event,        String guard    ) {
        this.event = event;
        this.guard = guard;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }


}