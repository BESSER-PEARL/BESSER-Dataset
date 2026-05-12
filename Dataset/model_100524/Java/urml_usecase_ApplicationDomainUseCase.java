





import java.util.List;
import java.util.ArrayList;

public class urml_usecase_ApplicationDomainUseCase extends UseCase {






    private List<Goal> goals;


    public urml_usecase_ApplicationDomainUseCase(
    ) {
        super(
        );
        this.goals = new ArrayList<>();
    }

    public urml_usecase_ApplicationDomainUseCase(
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