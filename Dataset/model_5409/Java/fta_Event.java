





import java.util.List;
import java.util.ArrayList;

public class fta_Event extends Diagram {

    private boolean BaseEvent;



    public fta_Event(
        boolean BaseEvent    ) {
        super(
        );
        this.BaseEvent = BaseEvent;
    }


    public boolean getBaseevent() {
        return BaseEvent;
    }

    public void setBaseevent(boolean BaseEvent) {
        this.BaseEvent = BaseEvent;
    }


}