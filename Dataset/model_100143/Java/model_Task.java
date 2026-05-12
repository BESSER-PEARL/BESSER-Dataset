





import java.util.List;
import java.util.ArrayList;

public class model_Task extends NamedElement, DescribedElement {

    private String fileName;





    private model_TaskSet model_taskset;




    private List<model_Task> model_tasks;




    private model_TaskSet model_taskset;


    public model_Task(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.model_tasks = new ArrayList<>();
    }

    public model_Task(
        String fileName        ArrayList<model_Task> model_tasks    ) {
        this.fileName = fileName;
        this.model_tasks = model_tasks;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public model_TaskSet getModel_taskset() {
        return model_taskset;
    }

    public void setModel_taskset(model_TaskSet model_taskset) {
        this.model_taskset = model_taskset;
    }
    public List<model_Task> getModel_tasks() {
        return model_tasks;
    }

    public void addModel_task(Model_task model_task) {
        this.model_tasks.add(model_task);
    }
    public model_TaskSet getModel_taskset() {
        return model_taskset;
    }

    public void setModel_taskset(model_TaskSet model_taskset) {
        this.model_taskset = model_taskset;
    }

}