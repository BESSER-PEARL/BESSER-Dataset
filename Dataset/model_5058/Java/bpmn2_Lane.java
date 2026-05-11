





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Lane extends BaseElement {

    private String name;





    private bpmn2_LaneSet bpmn2_laneset;




    private bpmn2_LaneSet bpmn2_laneset;


    public bpmn2_Lane(
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

    public bpmn2_LaneSet getBpmn2_laneset() {
        return bpmn2_laneset;
    }

    public void setBpmn2_laneset(bpmn2_LaneSet bpmn2_laneset) {
        this.bpmn2_laneset = bpmn2_laneset;
    }
    public bpmn2_LaneSet getBpmn2_laneset() {
        return bpmn2_laneset;
    }

    public void setBpmn2_laneset(bpmn2_LaneSet bpmn2_laneset) {
        this.bpmn2_laneset = bpmn2_laneset;
    }

}