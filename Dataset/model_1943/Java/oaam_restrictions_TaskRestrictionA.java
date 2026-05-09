





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_TaskRestrictionA  {






    private List<Task> tasks;


    public oaam_restrictions_TaskRestrictionA(
    ) {
        this.tasks = new ArrayList<>();
    }

    public oaam_restrictions_TaskRestrictionA(
        ArrayList<Task> tasks    ) {
        this.tasks = tasks;
    }


    public List<Task> getTasks() {
        return tasks;
    }

    public void addTask(Task task) {
        this.tasks.add(task);
    }

}