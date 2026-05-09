





import java.util.List;
import java.util.ArrayList;

public class statemodel_TransitionBlock extends Activity {

    private String event;



    public statemodel_TransitionBlock(
        String event    ) {
        super(
        );
        this.event = event;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }


}