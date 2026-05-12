





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Project  {






    private List<PrePostGoal> prepostgoals;


    public MavenMaven_Project(
    ) {
        this.prepostgoals = new ArrayList<>();
    }

    public MavenMaven_Project(
        ArrayList<PrePostGoal> prepostgoals    ) {
        this.prepostgoals = prepostgoals;
    }


    public List<PrePostGoal> getPrepostgoals() {
        return prepostgoals;
    }

    public void addPrepostgoal(Prepostgoal prepostgoal) {
        this.prepostgoals.add(prepostgoal);
    }

}