





import java.util.List;
import java.util.ArrayList;

public class e2_SubGoal  {

    private String GoalID;
    private String GoalText;





    private e2_Lecture e2_lecture;


    public e2_SubGoal(
        String GoalID,        String GoalText    ) {
        this.GoalID = GoalID;
        this.GoalText = GoalText;
    }


    public String getGoalid() {
        return GoalID;
    }

    public void setGoalid(String GoalID) {
        this.GoalID = GoalID;
    }
    public String getGoaltext() {
        return GoalText;
    }

    public void setGoaltext(String GoalText) {
        this.GoalText = GoalText;
    }

    public e2_Lecture getE2_lecture() {
        return e2_lecture;
    }

    public void setE2_lecture(e2_Lecture e2_lecture) {
        this.e2_lecture = e2_lecture;
    }

}