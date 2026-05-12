





import java.util.List;
import java.util.ArrayList;

public class USECASE1_Service  {






    private List<Goal> goals;




    private List<UseCase> usecases;


    public USECASE1_Service(
    ) {
        this.goals = new ArrayList<>();
        this.usecases = new ArrayList<>();
    }

    public USECASE1_Service(
        ArrayList<Goal> goals,        ArrayList<UseCase> usecases    ) {
        this.goals = goals;
        this.usecases = usecases;
    }


    public List<Goal> getGoals() {
        return goals;
    }

    public void addGoal(Goal goal) {
        this.goals.add(goal);
    }
    public List<UseCase> getUsecases() {
        return usecases;
    }

    public void addUsecase(Usecase usecase) {
        this.usecases.add(usecase);
    }

}