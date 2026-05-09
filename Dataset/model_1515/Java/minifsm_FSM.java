





import java.util.List;
import java.util.ArrayList;

public class minifsm_FSM  {

    private String currentEvent;



    public minifsm_FSM(
        String currentEvent    ) {
        this.currentEvent = currentEvent;
    }


    public String getCurrentevent() {
        return currentEvent;
    }

    public void setCurrentevent(String currentEvent) {
        this.currentEvent = currentEvent;
    }


}