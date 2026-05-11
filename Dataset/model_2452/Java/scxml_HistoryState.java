





import java.util.List;
import java.util.ArrayList;

public class scxml_HistoryState extends TransitionTarget, InitialState {

    private String type;





    private scxml_State scxml_state;


    public scxml_HistoryState(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public scxml_State getScxml_state() {
        return scxml_state;
    }

    public void setScxml_state(scxml_State scxml_state) {
        this.scxml_state = scxml_state;
    }

}