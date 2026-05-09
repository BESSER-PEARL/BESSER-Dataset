





import java.util.List;
import java.util.ArrayList;

public class UML2_Extend extends NamedElement, DirectedRelationship {






    private UML2_UseCase uml2_usecase;




    private List<UML2_ExtensionPoint> uml2_extensionpoints;




    private UML2_UseCase uml2_usecase;




    private UML2_Constraint uml2_constraint;




    private UML2_UseCase uml2_usecase;


    public UML2_Extend(
    ) {
        super(
        );
        this.uml2_extensionpoints = new ArrayList<>();
    }

    public UML2_Extend(
        ArrayList<UML2_ExtensionPoint> uml2_extensionpoints    ) {
        this.uml2_extensionpoints = uml2_extensionpoints;
    }


    public UML2_UseCase getUml2_usecase() {
        return uml2_usecase;
    }

    public void setUml2_usecase(UML2_UseCase uml2_usecase) {
        this.uml2_usecase = uml2_usecase;
    }
    public List<UML2_ExtensionPoint> getUml2_extensionpoints() {
        return uml2_extensionpoints;
    }

    public void addUml2_extensionpoint(Uml2_extensionpoint uml2_extensionpoint) {
        this.uml2_extensionpoints.add(uml2_extensionpoint);
    }
    public UML2_UseCase getUml2_usecase() {
        return uml2_usecase;
    }

    public void setUml2_usecase(UML2_UseCase uml2_usecase) {
        this.uml2_usecase = uml2_usecase;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public UML2_UseCase getUml2_usecase() {
        return uml2_usecase;
    }

    public void setUml2_usecase(UML2_UseCase uml2_usecase) {
        this.uml2_usecase = uml2_usecase;
    }

}