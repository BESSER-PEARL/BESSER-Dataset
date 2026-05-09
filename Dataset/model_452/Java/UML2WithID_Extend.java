





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Extend extends NamedElement, DirectedRelationship {






    private List<UML2WithID_ExtensionPoint> uml2withid_extensionpoints;




    private UML2WithID_UseCase uml2withid_usecase;




    private UML2WithID_UseCase uml2withid_usecase;




    private UML2WithID_UseCase uml2withid_usecase;


    public UML2WithID_Extend(
    ) {
        super(
        );
        this.uml2withid_extensionpoints = new ArrayList<>();
    }

    public UML2WithID_Extend(
        ArrayList<UML2WithID_ExtensionPoint> uml2withid_extensionpoints    ) {
        this.uml2withid_extensionpoints = uml2withid_extensionpoints;
    }


    public List<UML2WithID_ExtensionPoint> getUml2withid_extensionpoints() {
        return uml2withid_extensionpoints;
    }

    public void addUml2withid_extensionpoint(Uml2withid_extensionpoint uml2withid_extensionpoint) {
        this.uml2withid_extensionpoints.add(uml2withid_extensionpoint);
    }
    public UML2WithID_UseCase getUml2withid_usecase() {
        return uml2withid_usecase;
    }

    public void setUml2withid_usecase(UML2WithID_UseCase uml2withid_usecase) {
        this.uml2withid_usecase = uml2withid_usecase;
    }
    public UML2WithID_UseCase getUml2withid_usecase() {
        return uml2withid_usecase;
    }

    public void setUml2withid_usecase(UML2WithID_UseCase uml2withid_usecase) {
        this.uml2withid_usecase = uml2withid_usecase;
    }
    public UML2WithID_UseCase getUml2withid_usecase() {
        return uml2withid_usecase;
    }

    public void setUml2withid_usecase(UML2WithID_UseCase uml2withid_usecase) {
        this.uml2withid_usecase = uml2withid_usecase;
    }

}