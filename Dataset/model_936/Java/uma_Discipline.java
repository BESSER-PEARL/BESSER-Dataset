





import java.util.List;
import java.util.ArrayList;

public class uma_Discipline extends ContentCategory {

    private String task;
    private String group2;
    private String referenceWorkflow;





    private List<uma_Discipline> uma_disciplines;


    public uma_Discipline(
        String task,        String group2,        String referenceWorkflow    ) {
        super(
        );
        this.task = task;
        this.group2 = group2;
        this.referenceWorkflow = referenceWorkflow;
        this.uma_disciplines = new ArrayList<>();
    }

    public uma_Discipline(
        String task,        String group2,        String referenceWorkflow        ArrayList<uma_Discipline> uma_disciplines    ) {
        this.task = task;
        this.group2 = group2;
        this.referenceWorkflow = referenceWorkflow;
        this.uma_disciplines = uma_disciplines;
    }

    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getReferenceworkflow() {
        return referenceWorkflow;
    }

    public void setReferenceworkflow(String referenceWorkflow) {
        this.referenceWorkflow = referenceWorkflow;
    }

    public List<uma_Discipline> getUma_disciplines() {
        return uma_disciplines;
    }

    public void addUma_discipline(Uma_discipline uma_discipline) {
        this.uma_disciplines.add(uma_discipline);
    }

}