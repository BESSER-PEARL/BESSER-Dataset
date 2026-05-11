





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNRelationship extends BaseElement {

    private String direction;
    private String type;





    private BPMNProfile_Definitions bpmnprofile_definitions;




    private BPMNProfile_Definitions bpmnprofile_definitions;


    public BPMNProfile_BPMNRelationship(
        String direction,        String type    ) {
        super(
        );
        this.direction = direction;
        this.type = type;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public BPMNProfile_Definitions getBpmnprofile_definitions() {
        return bpmnprofile_definitions;
    }

    public void setBpmnprofile_definitions(BPMNProfile_Definitions bpmnprofile_definitions) {
        this.bpmnprofile_definitions = bpmnprofile_definitions;
    }
    public BPMNProfile_Definitions getBpmnprofile_definitions() {
        return bpmnprofile_definitions;
    }

    public void setBpmnprofile_definitions(BPMNProfile_Definitions bpmnprofile_definitions) {
        this.bpmnprofile_definitions = bpmnprofile_definitions;
    }

}