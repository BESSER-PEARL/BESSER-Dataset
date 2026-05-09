





import java.util.List;
import java.util.ArrayList;

public class errorstm_Transition  {

    private String guard;
    private String name;
    private String event;



    public errorstm_Transition(
        String guard,        String name,        String event    ) {
        this.guard = guard;
        this.name = name;
        this.event = event;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
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