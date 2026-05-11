





import java.util.List;
import java.util.ArrayList;

public class e2_Goal  {

    private String GoalText;
    private String GoalID;





    private e2_Course e2_course;




    private List<e2_SubGoal> e2_subgoals;


    public e2_Goal(
        String GoalText,        String GoalID    ) {
        this.GoalText = GoalText;
        this.GoalID = GoalID;
        this.e2_subgoals = new ArrayList<>();
    }

    public e2_Goal(
        String GoalText,        String GoalID        ArrayList<e2_SubGoal> e2_subgoals    ) {
        this.GoalText = GoalText;
        this.GoalID = GoalID;
        this.e2_subgoals = e2_subgoals;
    }

    public String getGoaltext() {
        return GoalText;
    }

    public void setGoaltext(String GoalText) {
        this.GoalText = GoalText;
    }
    public String getGoalid() {
        return GoalID;
    }

    public void setGoalid(String GoalID) {
        this.GoalID = GoalID;
    }

    public e2_Course getE2_course() {
        return e2_course;
    }

    public void setE2_course(e2_Course e2_course) {
        this.e2_course = e2_course;
    }
    public List<e2_SubGoal> getE2_subgoals() {
        return e2_subgoals;
    }

    public void addE2_subgoal(E2_subgoal e2_subgoal) {
        this.e2_subgoals.add(e2_subgoal);
    }

}