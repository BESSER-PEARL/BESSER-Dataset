





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_TimeEventNode extends ActivityNode {

    private String cycle;



    public activitydiagram_TimeEventNode(
        String cycle    ) {
        super(
        );
        this.cycle = cycle;
    }


    public String getCycle() {
        return cycle;
    }

    public void setCycle(String cycle) {
        this.cycle = cycle;
    }


}