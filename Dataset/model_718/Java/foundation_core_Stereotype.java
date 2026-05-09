





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Stereotype extends GeneralizableElement {

    private String icon;
    private String baseClass;





    private List<Constraint> constraints;




    private List<ModelElement> modelelements;


    public foundation_core_Stereotype(
        String icon,        String baseClass    ) {
        super(
        );
        this.icon = icon;
        this.baseClass = baseClass;
        this.constraints = new ArrayList<>();
        this.modelelements = new ArrayList<>();
    }

    public foundation_core_Stereotype(
        String icon,        String baseClass        ArrayList<Constraint> constraints,        ArrayList<ModelElement> modelelements    ) {
        this.icon = icon;
        this.baseClass = baseClass;
        this.constraints = constraints;
        this.modelelements = modelelements;
    }

    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getBaseclass() {
        return baseClass;
    }

    public void setBaseclass(String baseClass) {
        this.baseClass = baseClass;
    }

    public List<Constraint> getConstraints() {
        return constraints;
    }

    public void addConstraint(Constraint constraint) {
        this.constraints.add(constraint);
    }
    public List<ModelElement> getModelelements() {
        return modelelements;
    }

    public void addModelelement(Modelelement modelelement) {
        this.modelelements.add(modelelement);
    }

}