





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_Region extends AABB, NamedElement {






    private List<dronesStructure_Task> dronesstructure_tasks;




    private dronesStructure_Scenario dronesstructure_scenario;




    private dronesStructure_Task dronesstructure_task;


    public dronesStructure_Region(
    ) {
        super(
        );
        this.dronesstructure_tasks = new ArrayList<>();
    }

    public dronesStructure_Region(
        ArrayList<dronesStructure_Task> dronesstructure_tasks    ) {
        this.dronesstructure_tasks = dronesstructure_tasks;
    }


    public List<dronesStructure_Task> getDronesstructure_tasks() {
        return dronesstructure_tasks;
    }

    public void addDronesstructure_task(Dronesstructure_task dronesstructure_task) {
        this.dronesstructure_tasks.add(dronesstructure_task);
    }
    public dronesStructure_Scenario getDronesstructure_scenario() {
        return dronesstructure_scenario;
    }

    public void setDronesstructure_scenario(dronesStructure_Scenario dronesstructure_scenario) {
        this.dronesstructure_scenario = dronesstructure_scenario;
    }
    public dronesStructure_Task getDronesstructure_task() {
        return dronesstructure_task;
    }

    public void setDronesstructure_task(dronesStructure_Task dronesstructure_task) {
        this.dronesstructure_task = dronesstructure_task;
    }

}