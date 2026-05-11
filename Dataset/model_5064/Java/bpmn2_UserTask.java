





import java.util.List;
import java.util.ArrayList;

public class bpmn2_UserTask extends Task {

    private String implementation;





    private List<bpmn2_Rendering> bpmn2_renderings;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_UserTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
        this.bpmn2_renderings = new ArrayList<>();
    }

    public bpmn2_UserTask(
        String implementation        ArrayList<bpmn2_Rendering> bpmn2_renderings    ) {
        this.implementation = implementation;
        this.bpmn2_renderings = bpmn2_renderings;
    }

    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public List<bpmn2_Rendering> getBpmn2_renderings() {
        return bpmn2_renderings;
    }

    public void addBpmn2_rendering(Bpmn2_rendering bpmn2_rendering) {
        this.bpmn2_renderings.add(bpmn2_rendering);
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}