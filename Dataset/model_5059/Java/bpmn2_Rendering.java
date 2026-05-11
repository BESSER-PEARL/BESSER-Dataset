





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Rendering extends BaseElement {






    private bpmn2_UserTask bpmn2_usertask;




    private bpmn2_GlobalUserTask bpmn2_globalusertask;


    public bpmn2_Rendering(
    ) {
        super(
        );
    }



    public bpmn2_UserTask getBpmn2_usertask() {
        return bpmn2_usertask;
    }

    public void setBpmn2_usertask(bpmn2_UserTask bpmn2_usertask) {
        this.bpmn2_usertask = bpmn2_usertask;
    }
    public bpmn2_GlobalUserTask getBpmn2_globalusertask() {
        return bpmn2_globalusertask;
    }

    public void setBpmn2_globalusertask(bpmn2_GlobalUserTask bpmn2_globalusertask) {
        this.bpmn2_globalusertask = bpmn2_globalusertask;
    }

}