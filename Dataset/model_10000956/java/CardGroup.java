





import java.util.List;
import java.util.ArrayList;

public class CardGroup  {






    private List<Sprint> sprints;


    public CardGroup(
    ) {
        this.sprints = new ArrayList<>();
    }

    public CardGroup(
        ArrayList<Sprint> sprints    ) {
        this.sprints = sprints;
    }


    public List<Sprint> getSprints() {
        return sprints;
    }

    public void addSprint(Sprint sprint) {
        this.sprints.add(sprint);
    }

}