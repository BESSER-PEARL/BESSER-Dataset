





import java.util.List;
import java.util.ArrayList;

public class rdal_Requirement extends RefineableElement, AbstractRequirement {






    private List<rdal_EObject> rdal_eobjects;


    public rdal_Requirement(
    ) {
        super(
        );
        this.rdal_eobjects = new ArrayList<>();
    }

    public rdal_Requirement(
        ArrayList<rdal_EObject> rdal_eobjects    ) {
        this.rdal_eobjects = rdal_eobjects;
    }


    public List<rdal_EObject> getRdal_eobjects() {
        return rdal_eobjects;
    }

    public void addRdal_eobject(Rdal_eobject rdal_eobject) {
        this.rdal_eobjects.add(rdal_eobject);
    }

}