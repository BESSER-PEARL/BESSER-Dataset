





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Duration extends ValueSpecification {

    private boolean firstTime;





    private List<UML2WithID_NamedElement> uml2withid_namedelements;


    public UML2WithID_Duration(
        boolean firstTime    ) {
        super(
        );
        this.firstTime = firstTime;
        this.uml2withid_namedelements = new ArrayList<>();
    }

    public UML2WithID_Duration(
        boolean firstTime        ArrayList<UML2WithID_NamedElement> uml2withid_namedelements    ) {
        this.firstTime = firstTime;
        this.uml2withid_namedelements = uml2withid_namedelements;
    }

    public boolean getFirsttime() {
        return firstTime;
    }

    public void setFirsttime(boolean firstTime) {
        this.firstTime = firstTime;
    }

    public List<UML2WithID_NamedElement> getUml2withid_namedelements() {
        return uml2withid_namedelements;
    }

    public void addUml2withid_namedelement(Uml2withid_namedelement uml2withid_namedelement) {
        this.uml2withid_namedelements.add(uml2withid_namedelement);
    }

}