





import java.util.List;
import java.util.ArrayList;

public class rdal_SubGoalReference extends SubElementReference {






    private rdal_GoalRefinement rdal_goalrefinement;




    private rdal_AbstractGoal rdal_abstractgoal;


    public rdal_SubGoalReference(
    ) {
        super(
        );
    }



    public rdal_GoalRefinement getRdal_goalrefinement() {
        return rdal_goalrefinement;
    }

    public void setRdal_goalrefinement(rdal_GoalRefinement rdal_goalrefinement) {
        this.rdal_goalrefinement = rdal_goalrefinement;
    }
    public rdal_AbstractGoal getRdal_abstractgoal() {
        return rdal_abstractgoal;
    }

    public void setRdal_abstractgoal(rdal_AbstractGoal rdal_abstractgoal) {
        this.rdal_abstractgoal = rdal_abstractgoal;
    }

}