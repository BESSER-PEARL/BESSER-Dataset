





import java.util.List;
import java.util.ArrayList;

public class gsml_TaskGroup extends Task {






    private List<gsml_Task> gsml_tasks;


    public gsml_TaskGroup(
    ) {
        super(
        );
        this.gsml_tasks = new ArrayList<>();
    }

    public gsml_TaskGroup(
        ArrayList<gsml_Task> gsml_tasks    ) {
        this.gsml_tasks = gsml_tasks;
    }


    public List<gsml_Task> getGsml_tasks() {
        return gsml_tasks;
    }

    public void addGsml_task(Gsml_task gsml_task) {
        this.gsml_tasks.add(gsml_task);
    }

}