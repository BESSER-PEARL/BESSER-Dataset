





import java.util.List;
import java.util.ArrayList;

public class rdal_AbstractGoal extends RefineableElement, SatisfiableElement, TextualContractualElement {






    private rdal_GoalRefinement rdal_goalrefinement;




    private rdal_GoalsPackage rdal_goalspackage;




    private rdal_Conflict rdal_conflict;




    private List<rdal_Conflict> rdal_conflicts;




    private rdal_GoalRefinement rdal_goalrefinement;




    private rdal_GoalsPackage rdal_goalspackage;


    public rdal_AbstractGoal(
    ) {
        super(
        );
        this.rdal_conflicts = new ArrayList<>();
    }

    public rdal_AbstractGoal(
        ArrayList<rdal_Conflict> rdal_conflicts    ) {
        this.rdal_conflicts = rdal_conflicts;
    }


    public rdal_GoalRefinement getRdal_goalrefinement() {
        return rdal_goalrefinement;
    }

    public void setRdal_goalrefinement(rdal_GoalRefinement rdal_goalrefinement) {
        this.rdal_goalrefinement = rdal_goalrefinement;
    }
    public rdal_GoalsPackage getRdal_goalspackage() {
        return rdal_goalspackage;
    }

    public void setRdal_goalspackage(rdal_GoalsPackage rdal_goalspackage) {
        this.rdal_goalspackage = rdal_goalspackage;
    }
    public rdal_Conflict getRdal_conflict() {
        return rdal_conflict;
    }

    public void setRdal_conflict(rdal_Conflict rdal_conflict) {
        this.rdal_conflict = rdal_conflict;
    }
    public List<rdal_Conflict> getRdal_conflicts() {
        return rdal_conflicts;
    }

    public void addRdal_conflict(Rdal_conflict rdal_conflict) {
        this.rdal_conflicts.add(rdal_conflict);
    }
    public rdal_GoalRefinement getRdal_goalrefinement() {
        return rdal_goalrefinement;
    }

    public void setRdal_goalrefinement(rdal_GoalRefinement rdal_goalrefinement) {
        this.rdal_goalrefinement = rdal_goalrefinement;
    }
    public rdal_GoalsPackage getRdal_goalspackage() {
        return rdal_goalspackage;
    }

    public void setRdal_goalspackage(rdal_GoalsPackage rdal_goalspackage) {
        this.rdal_goalspackage = rdal_goalspackage;
    }

}