





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends AbstractState {

    private String stateColor;



    public statemachine_State(
        String stateColor    ) {
        super(
        );
        this.stateColor = stateColor;
    }


    public String getStatecolor() {
        return stateColor;
    }

    public void setStatecolor(String stateColor) {
        this.stateColor = stateColor;
    }


}