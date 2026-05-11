





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_GlobalUserTask extends GlobalTask {

    private String implementation;





    private List<bpmnprof_Rendering> bpmnprof_renderings;


    public bpmnprof_GlobalUserTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
        this.bpmnprof_renderings = new ArrayList<>();
    }

    public bpmnprof_GlobalUserTask(
        String implementation        ArrayList<bpmnprof_Rendering> bpmnprof_renderings    ) {
        this.implementation = implementation;
        this.bpmnprof_renderings = bpmnprof_renderings;
    }

    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public List<bpmnprof_Rendering> getBpmnprof_renderings() {
        return bpmnprof_renderings;
    }

    public void addBpmnprof_rendering(Bpmnprof_rendering bpmnprof_rendering) {
        this.bpmnprof_renderings.add(bpmnprof_rendering);
    }

}