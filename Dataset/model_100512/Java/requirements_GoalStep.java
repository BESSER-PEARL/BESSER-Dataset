





import java.util.List;
import java.util.ArrayList;

public class requirements_GoalStep  {






    private List<requirements_Goal> requirements_goals;




    private requirements_Goal requirements_goal;




    private requirements_Process requirements_process;


    public requirements_GoalStep(
    ) {
        this.requirements_goals = new ArrayList<>();
    }

    public requirements_GoalStep(
        ArrayList<requirements_Goal> requirements_goals    ) {
        this.requirements_goals = requirements_goals;
    }


    public List<requirements_Goal> getRequirements_goals() {
        return requirements_goals;
    }

    public void addRequirements_goal(Requirements_goal requirements_goal) {
        this.requirements_goals.add(requirements_goal);
    }
    public requirements_Goal getRequirements_goal() {
        return requirements_goal;
    }

    public void setRequirements_goal(requirements_Goal requirements_goal) {
        this.requirements_goal = requirements_goal;
    }
    public requirements_Process getRequirements_process() {
        return requirements_process;
    }

    public void setRequirements_process(requirements_Process requirements_process) {
        this.requirements_process = requirements_process;
    }

}