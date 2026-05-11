





import java.util.List;
import java.util.ArrayList;

public class UML_14_NamedElement  {

    private String name;





    private List<UML_14_Constraint> uml_14_constraints;


    public UML_14_NamedElement(
        String name    ) {
        this.name = name;
        this.uml_14_constraints = new ArrayList<>();
    }

    public UML_14_NamedElement(
        String name        ArrayList<UML_14_Constraint> uml_14_constraints    ) {
        this.name = name;
        this.uml_14_constraints = uml_14_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UML_14_Constraint> getUml_14_constraints() {
        return uml_14_constraints;
    }

    public void addUml_14_constraint(Uml_14_constraint uml_14_constraint) {
        this.uml_14_constraints.add(uml_14_constraint);
    }

}