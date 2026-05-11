





import java.util.List;
import java.util.ArrayList;

public class events_ComplexEventPattern extends EventPattern {

    private String eventContext;



    public events_ComplexEventPattern(
        String eventContext    ) {
        super(
        );
        this.eventContext = eventContext;
    }


    public String getEventcontext() {
        return eventContext;
    }

    public void setEventcontext(String eventContext) {
        this.eventContext = eventContext;
    }


}