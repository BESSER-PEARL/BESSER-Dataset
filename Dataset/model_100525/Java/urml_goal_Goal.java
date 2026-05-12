





import java.util.List;
import java.util.ArrayList;

public class urml_goal_Goal extends UrmlModelElement {

    private boolean soft;
    private String type;





    private List<Goal> goals;




    private Goal goal;


    public urml_goal_Goal(
        boolean soft,        String type    ) {
        super(
        );
        this.soft = soft;
        this.type = type;
        this.goals = new ArrayList<>();
    }

    public urml_goal_Goal(
        boolean soft,        String type        ArrayList<Goal> goals    ) {
        this.soft = soft;
        this.type = type;
        this.goals = goals;
    }

    public boolean getSoft() {
        return soft;
    }

    public void setSoft(boolean soft) {
        this.soft = soft;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<Goal> getGoals() {
        return goals;
    }

    public void addGoal(Goal goal) {
        this.goals.add(goal);
    }
    public Goal getGoal() {
        return goal;
    }

    public void setGoal(Goal goal) {
        this.goal = goal;
    }

}