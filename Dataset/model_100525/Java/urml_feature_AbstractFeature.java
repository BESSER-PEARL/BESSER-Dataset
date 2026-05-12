





import java.util.List;
import java.util.ArrayList;

public class urml_feature_AbstractFeature extends UrmlModelElement {






    private List<Goal> goals;


    public urml_feature_AbstractFeature(
    ) {
        super(
        );
        this.goals = new ArrayList<>();
    }

    public urml_feature_AbstractFeature(
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