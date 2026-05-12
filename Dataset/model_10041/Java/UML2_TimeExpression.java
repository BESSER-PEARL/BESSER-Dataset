





import java.util.List;
import java.util.ArrayList;

public class UML2_TimeExpression extends ValueSpecification {

    private boolean firstTime;





    private UML2_NamedElement uml2_namedelement;


    public UML2_TimeExpression(
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

    public UML2_NamedElement getUml2_namedelement() {
        return uml2_namedelement;
    }

    public void setUml2_namedelement(UML2_NamedElement uml2_namedelement) {
        this.uml2_namedelement = uml2_namedelement;
    }

}