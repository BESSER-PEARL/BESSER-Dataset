





import java.util.List;
import java.util.ArrayList;

public class behavior_UseCaseRepository  {






    private List<behavior_UseCase> behavior_usecases;


    public behavior_UseCaseRepository(
    ) {
        this.behavior_usecases = new ArrayList<>();
    }

    public behavior_UseCaseRepository(
        ArrayList<behavior_UseCase> behavior_usecases    ) {
        this.behavior_usecases = behavior_usecases;
    }


    public List<behavior_UseCase> getBehavior_usecases() {
        return behavior_usecases;
    }

    public void addBehavior_usecase(Behavior_usecase behavior_usecase) {
        this.behavior_usecases.add(behavior_usecase);
    }

}