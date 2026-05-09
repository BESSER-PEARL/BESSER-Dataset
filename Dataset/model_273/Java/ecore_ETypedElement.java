





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private int lowerBound;
    private int upperBound;





    private ecore_EClassifier ecore_eclassifier;




    private ecore_EGenericType ecore_egenerictype;


    public ecore_ETypedElement(
        int lowerBound,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }

}