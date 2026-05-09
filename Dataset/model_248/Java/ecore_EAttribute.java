





import java.util.List;
import java.util.ArrayList;

public class ecore_EAttribute extends EStructuralFeature {

    private boolean iD;





    private List<ecore_EDataType> ecore_edatatypes;


    public ecore_EAttribute(
        boolean iD    ) {
        super(
        );
        this.iD = iD;
        this.ecore_edatatypes = new ArrayList<>();
    }

    public ecore_EAttribute(
        boolean iD        ArrayList<ecore_EDataType> ecore_edatatypes    ) {
        this.iD = iD;
        this.ecore_edatatypes = ecore_edatatypes;
    }

    public boolean getId() {
        return iD;
    }

    public void setId(boolean iD) {
        this.iD = iD;
    }

    public List<ecore_EDataType> getEcore_edatatypes() {
        return ecore_edatatypes;
    }

    public void addEcore_edatatype(Ecore_edatatype ecore_edatatype) {
        this.ecore_edatatypes.add(ecore_edatatype);
    }

}