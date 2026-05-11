





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_activity_graphs_SubactivityState extends SubmachineState {

    private String isDynamic;



    public behavioral_elements_activity_graphs_SubactivityState(
        String isDynamic    ) {
        super(
        );
        this.isDynamic = isDynamic;
    }


    public String getIsdynamic() {
        return isDynamic;
    }

    public void setIsdynamic(String isDynamic) {
        this.isDynamic = isDynamic;
    }


}