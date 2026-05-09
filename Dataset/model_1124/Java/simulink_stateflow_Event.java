





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_Event extends StateflowElement {

    private String name;



    public simulink_stateflow_Event(
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


}