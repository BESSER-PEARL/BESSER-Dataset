





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_state_machines_CompositeState extends State {

    private String isConcurrent;



    public behavioral_elements_state_machines_CompositeState(
        String isConcurrent    ) {
        super(
        );
        this.isConcurrent = isConcurrent;
    }


    public String getIsconcurrent() {
        return isConcurrent;
    }

    public void setIsconcurrent(String isConcurrent) {
        this.isConcurrent = isConcurrent;
    }


}