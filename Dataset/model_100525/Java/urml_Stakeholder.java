





import java.util.List;
import java.util.ArrayList;

public class urml_Stakeholder extends UrmlModelElement {






    private List<Goal> goals;


    public urml_Stakeholder(
    ) {
        super(
        );
        this.goals = new ArrayList<>();
    }

    public urml_Stakeholder(
        ArrayList<Goal> goals    ) {
        this.goals = goals;
    }


    public List<Goal> getGoals() {
        return goals;
    }

    public void addGoal(Goal goal) {
        this.goals.add(goal);
    }

}