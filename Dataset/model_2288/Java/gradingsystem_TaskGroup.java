





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_TaskGroup extends Task {






    private List<gradingsystem_Task> gradingsystem_tasks;


    public gradingsystem_TaskGroup(
    ) {
        super(
        );
        this.gradingsystem_tasks = new ArrayList<>();
    }

    public gradingsystem_TaskGroup(
        ArrayList<gradingsystem_Task> gradingsystem_tasks    ) {
        this.gradingsystem_tasks = gradingsystem_tasks;
    }


    public List<gradingsystem_Task> getGradingsystem_tasks() {
        return gradingsystem_tasks;
    }

    public void addGradingsystem_task(Gradingsystem_task gradingsystem_task) {
        this.gradingsystem_tasks.add(gradingsystem_task);
    }

}