





import java.util.List;
import java.util.ArrayList;

public class ioT_LEDAction extends Action {

    private String state;



    public ioT_LEDAction(
        String state    ) {
        super(
        );
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}