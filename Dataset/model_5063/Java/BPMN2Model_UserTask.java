





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_UserTask extends Task {

    private String implementation;





    private List<BPMN2Model_Rendering> bpmn2model_renderings;


    public BPMN2Model_UserTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
        this.bpmn2model_renderings = new ArrayList<>();
    }

    public BPMN2Model_UserTask(
        String implementation        ArrayList<BPMN2Model_Rendering> bpmn2model_renderings    ) {
        this.implementation = implementation;
        this.bpmn2model_renderings = bpmn2model_renderings;
    }

    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public List<BPMN2Model_Rendering> getBpmn2model_renderings() {
        return bpmn2model_renderings;
    }

    public void addBpmn2model_rendering(Bpmn2model_rendering bpmn2model_rendering) {
        this.bpmn2model_renderings.add(bpmn2model_rendering);
    }

}