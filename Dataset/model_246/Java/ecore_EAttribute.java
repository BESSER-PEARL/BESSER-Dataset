





import java.util.List;
import java.util.ArrayList;

public class ecore_EAttribute extends EStructuralFeature {

    private boolean iD;





    private ecore_EDataType ecore_edatatype;


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

    public ecore_EDataType getEcore_edatatype() {
        return ecore_edatatype;
    }

    public void setEcore_edatatype(ecore_EDataType ecore_edatatype) {
        this.ecore_edatatype = ecore_edatatype;
    }

}