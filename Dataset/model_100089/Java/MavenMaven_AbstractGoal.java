





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_AbstractGoal  {






    private List<ContentsGoal> contentsgoals;


    public MavenMaven_AbstractGoal(
    ) {
        this.contentsgoals = new ArrayList<>();
    }

    public MavenMaven_AbstractGoal(
        ArrayList<ContentsGoal> contentsgoals    ) {
        this.contentsgoals = contentsgoals;
    }


    public List<ContentsGoal> getContentsgoals() {
        return contentsgoals;
    }

    public void addContentsgoal(Contentsgoal contentsgoal) {
        this.contentsgoals.add(contentsgoal);
    }

}