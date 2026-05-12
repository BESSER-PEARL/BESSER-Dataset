





import java.util.List;
import java.util.ArrayList;

public class UML2_Duration extends ValueSpecification {

    private boolean firstTime;





    private List<UML2_NamedElement> uml2_namedelements;


    public UML2_Duration(
        boolean firstTime    ) {
        super(
        );
        this.firstTime = firstTime;
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Duration(
        boolean firstTime        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.firstTime = firstTime;
        this.uml2_namedelements = uml2_namedelements;
    }

    public boolean getFirsttime() {
        return firstTime;
    }

    public void setFirsttime(boolean firstTime) {
        this.firstTime = firstTime;
    }

    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }

}