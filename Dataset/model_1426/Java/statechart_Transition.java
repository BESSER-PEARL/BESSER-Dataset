





import java.util.List;
import java.util.ArrayList;

public class statechart_Transition extends ModelElement {

    private String event;
    private String guard;





    private statechart_CompositeState statechart_compositestate;


    public statechart_Transition(
        String event,        String guard    ) {
        super(
        );
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

    public statechart_CompositeState getStatechart_compositestate() {
        return statechart_compositestate;
    }

    public void setStatechart_compositestate(statechart_CompositeState statechart_compositestate) {
        this.statechart_compositestate = statechart_compositestate;
    }

}