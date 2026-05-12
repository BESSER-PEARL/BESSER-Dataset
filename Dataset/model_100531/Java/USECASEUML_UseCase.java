





import java.util.List;
import java.util.ArrayList;

public class USECASEUML_UseCase  {






    private List<Goal> goals;


    public USECASEUML_UseCase(
    ) {
        this.goals = new ArrayList<>();
    }

    public USECASEUML_UseCase(
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