





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypeParameter extends ENamedElement {






    private ecore_EOperation ecore_eoperation;




    private ecore_EClassifier ecore_eclassifier;


    public ecore_ETypeParameter(
    ) {
        super(
        );
    }



    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }
    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }

}