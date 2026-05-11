





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ChoreographyActivity extends FlowNode {

    private String loopType;





    private bpmn2_DocumentRoot bpmn2_documentroot;


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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}