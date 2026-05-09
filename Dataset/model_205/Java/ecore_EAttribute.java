





import java.util.List;
import java.util.ArrayList;

public class ecore_EAttribute extends EStructuralFeature {

    private boolean iD;





    private ecore_EReference ecore_ereference;


    public ecore_EAttribute(
        boolean iD    ) {
        super(
        );
        this.iD = iD;
    }


    public boolean getId() {
        return iD;
    }

    public void setId(boolean iD) {
        this.iD = iD;
    }

    public ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }

}