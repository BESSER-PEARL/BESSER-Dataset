





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Constraint extends PackageableElement {

    private String context;
    private String constrainedElement;





    private UMLModel_State umlmodel_state;




    private UMLModel_ValueSpecification umlmodel_valuespecification;


    public UMLModel_Constraint(
        String context,        String constrainedElement    ) {
        super(
        );
        this.context = context;
        this.constrainedElement = constrainedElement;
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getConstrainedelement() {
        return constrainedElement;
    }

    public void setConstrainedelement(String constrainedElement) {
        this.constrainedElement = constrainedElement;
    }

    public UMLModel_State getUmlmodel_state() {
        return umlmodel_state;
    }

    public void setUmlmodel_state(UMLModel_State umlmodel_state) {
        this.umlmodel_state = umlmodel_state;
    }
    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }

}