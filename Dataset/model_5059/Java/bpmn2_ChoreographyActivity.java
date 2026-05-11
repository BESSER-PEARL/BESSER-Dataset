





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ChoreographyActivity extends FlowNode {

    private String loopType;



    public bpmn2_ChoreographyActivity(
        String loopType    ) {
        super(
        );
        this.loopType = loopType;
    }


    public String getLooptype() {
        return loopType;
    }

    public void setLooptype(String loopType) {
        this.loopType = loopType;
    }


}