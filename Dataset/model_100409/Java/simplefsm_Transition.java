





import java.util.List;
import java.util.ArrayList;

public class simplefsm_Transition  {

    private String name;
    private String event;



    public simplefsm_Transition(
        String name,        String event    ) {
        this.name = name;
        this.event = event;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }


}