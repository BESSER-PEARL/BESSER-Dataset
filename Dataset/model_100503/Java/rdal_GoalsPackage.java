





import java.util.List;
import java.util.ArrayList;

public class rdal_GoalsPackage extends SatisfiableElement, RdalOrgPackage {






    private List<rdal_GoalRefinement> rdal_goalrefinements;


    public rdal_GoalsPackage(
    ) {
        super(
        );
        this.rdal_goalrefinements = new ArrayList<>();
    }

    public rdal_GoalsPackage(
        ArrayList<rdal_GoalRefinement> rdal_goalrefinements    ) {
        this.rdal_goalrefinements = rdal_goalrefinements;
    }


    public List<rdal_GoalRefinement> getRdal_goalrefinements() {
        return rdal_goalrefinements;
    }

    public void addRdal_goalrefinement(Rdal_goalrefinement rdal_goalrefinement) {
        this.rdal_goalrefinements.add(rdal_goalrefinement);
    }

}