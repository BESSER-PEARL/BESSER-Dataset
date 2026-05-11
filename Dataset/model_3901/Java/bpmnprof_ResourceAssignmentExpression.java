





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ResourceAssignmentExpression extends BPMNExpression {






    private bpmnprof_ResourceRole bpmnprof_resourcerole;




    private bpmnprof_BPMNExpression bpmnprof_bpmnexpression;


    public bpmnprof_ResourceAssignmentExpression(
    ) {
        super(
        );
    }



    public bpmnprof_ResourceRole getBpmnprof_resourcerole() {
        return bpmnprof_resourcerole;
    }

    public void setBpmnprof_resourcerole(bpmnprof_ResourceRole bpmnprof_resourcerole) {
        this.bpmnprof_resourcerole = bpmnprof_resourcerole;
    }
    public bpmnprof_BPMNExpression getBpmnprof_bpmnexpression() {
        return bpmnprof_bpmnexpression;
    }

    public void setBpmnprof_bpmnexpression(bpmnprof_BPMNExpression bpmnprof_bpmnexpression) {
        this.bpmnprof_bpmnexpression = bpmnprof_bpmnexpression;
    }

}