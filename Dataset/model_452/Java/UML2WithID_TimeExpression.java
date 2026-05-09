





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TimeExpression extends ValueSpecification {

    private boolean firstTime;





    private UML2WithID_NamedElement uml2withid_namedelement;


    public UML2WithID_TimeExpression(
        boolean firstTime    ) {
        super(
        );
        this.firstTime = firstTime;
    }


    public boolean getFirsttime() {
        return firstTime;
    }

    public void setFirsttime(boolean firstTime) {
        this.firstTime = firstTime;
    }

    public UML2WithID_NamedElement getUml2withid_namedelement() {
        return uml2withid_namedelement;
    }

    public void setUml2withid_namedelement(UML2WithID_NamedElement uml2withid_namedelement) {
        this.uml2withid_namedelement = uml2withid_namedelement;
    }

}