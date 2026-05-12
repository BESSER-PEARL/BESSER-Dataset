





import java.util.List;
import java.util.ArrayList;

public class rdal_SubRequirementReference extends SubElementReference {






    private rdal_RequirementRefinement rdal_requirementrefinement;




    private rdal_AbstractRequirement rdal_abstractrequirement;


    public rdal_SubRequirementReference(
    ) {
        super(
        );
    }



    public rdal_RequirementRefinement getRdal_requirementrefinement() {
        return rdal_requirementrefinement;
    }

    public void setRdal_requirementrefinement(rdal_RequirementRefinement rdal_requirementrefinement) {
        this.rdal_requirementrefinement = rdal_requirementrefinement;
    }
    public rdal_AbstractRequirement getRdal_abstractrequirement() {
        return rdal_abstractrequirement;
    }

    public void setRdal_abstractrequirement(rdal_AbstractRequirement rdal_abstractrequirement) {
        this.rdal_abstractrequirement = rdal_abstractrequirement;
    }

}