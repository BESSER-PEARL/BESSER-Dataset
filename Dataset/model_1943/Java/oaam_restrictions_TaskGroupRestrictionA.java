





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_TaskGroupRestrictionA  {






    private List<TaskGroup> taskgroups;


    public oaam_restrictions_TaskGroupRestrictionA(
    ) {
        this.taskgroups = new ArrayList<>();
    }

    public oaam_restrictions_TaskGroupRestrictionA(
        ArrayList<TaskGroup> taskgroups    ) {
        this.taskgroups = taskgroups;
    }


    public List<TaskGroup> getTaskgroups() {
        return taskgroups;
    }

    public void addTaskgroup(Taskgroup taskgroup) {
        this.taskgroups.add(taskgroup);
    }

}