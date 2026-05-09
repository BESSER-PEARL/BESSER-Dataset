





import java.util.List;
import java.util.ArrayList;

public class uma_Discipline extends ContentCategory {

    private String referenceWorkflow;
    private String group2;
    private String task;





    private uma_Discipline uma_discipline;


    public uma_Discipline(
        String referenceWorkflow,        String group2,        String task    ) {
        super(
        );
        this.referenceWorkflow = referenceWorkflow;
        this.group2 = group2;
        this.task = task;
    }


    public String getReferenceworkflow() {
        return referenceWorkflow;
    }

    public void setReferenceworkflow(String referenceWorkflow) {
        this.referenceWorkflow = referenceWorkflow;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }

    public uma_Discipline getUma_discipline() {
        return uma_discipline;
    }

    public void setUma_discipline(uma_Discipline uma_discipline) {
        this.uma_discipline = uma_discipline;
    }

}