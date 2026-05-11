





import java.util.List;
import java.util.ArrayList;

public class bpmn2_OutputSet extends BaseElement {

    private String name;





    private bpmn2_CatchEvent bpmn2_catchevent;


    public bpmn2_OutputSet(
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

    public bpmn2_CatchEvent getBpmn2_catchevent() {
        return bpmn2_catchevent;
    }

    public void setBpmn2_catchevent(bpmn2_CatchEvent bpmn2_catchevent) {
        this.bpmn2_catchevent = bpmn2_catchevent;
    }

}