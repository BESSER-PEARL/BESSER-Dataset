





import java.util.List;
import java.util.ArrayList;

public class mvc_Event extends Annotable {

    private String name;





    private mvc_EventAction mvc_eventaction;


    public mvc_Event(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_EventAction getMvc_eventaction() {
        return mvc_eventaction;
    }

    public void setMvc_eventaction(mvc_EventAction mvc_eventaction) {
        this.mvc_eventaction = mvc_eventaction;
    }

}