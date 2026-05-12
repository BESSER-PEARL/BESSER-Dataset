





import java.util.List;
import java.util.ArrayList;

public class rdal_RequirementsPackage extends RdalOrgPackage, SatisfiableElement, VerifiableElement {






    private List<rdal_RequirementRefinement> rdal_requirementrefinements;


    public rdal_RequirementsPackage(
    ) {
        super(
        );
        this.rdal_requirementrefinements = new ArrayList<>();
    }

    public rdal_RequirementsPackage(
        ArrayList<rdal_RequirementRefinement> rdal_requirementrefinements    ) {
        this.rdal_requirementrefinements = rdal_requirementrefinements;
    }


    public List<rdal_RequirementRefinement> getRdal_requirementrefinements() {
        return rdal_requirementrefinements;
    }

    public void addRdal_requirementrefinement(Rdal_requirementrefinement rdal_requirementrefinement) {
        this.rdal_requirementrefinements.add(rdal_requirementrefinement);
    }

}