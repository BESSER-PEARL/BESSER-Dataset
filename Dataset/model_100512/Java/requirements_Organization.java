





import java.util.List;
import java.util.ArrayList;

public class requirements_Organization extends AnnotableElement {






    private List<requirements_ModelElement> requirements_modelelements;


    public requirements_Organization(
    ) {
        super(
        );
        this.requirements_modelelements = new ArrayList<>();
    }

    public requirements_Organization(
        ArrayList<requirements_ModelElement> requirements_modelelements    ) {
        this.requirements_modelelements = requirements_modelelements;
    }


    public List<requirements_ModelElement> getRequirements_modelelements() {
        return requirements_modelelements;
    }

    public void addRequirements_modelelement(Requirements_modelelement requirements_modelelement) {
        this.requirements_modelelements.add(requirements_modelelement);
    }

}