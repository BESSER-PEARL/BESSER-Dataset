





import java.util.List;
import java.util.ArrayList;

public class ecoreO_ETypeParameter extends ENamedElement {






    private List<ecoreO_EGenericType> ecoreo_egenerictypes;




    private ecoreO_EGenericType ecoreo_egenerictype;




    private ecoreO_EClassifier ecoreo_eclassifier;


    public ecoreO_ETypeParameter(
    ) {
        super(
        );
        this.ecoreo_egenerictypes = new ArrayList<>();
    }

    public ecoreO_ETypeParameter(
        ArrayList<ecoreO_EGenericType> ecoreo_egenerictypes    ) {
        this.ecoreo_egenerictypes = ecoreo_egenerictypes;
    }


    public List<ecoreO_EGenericType> getEcoreo_egenerictypes() {
        return ecoreo_egenerictypes;
    }

    public void addEcoreo_egenerictype(Ecoreo_egenerictype ecoreo_egenerictype) {
        this.ecoreo_egenerictypes.add(ecoreo_egenerictype);
    }
    public ecoreO_EGenericType getEcoreo_egenerictype() {
        return ecoreo_egenerictype;
    }

    public void setEcoreo_egenerictype(ecoreO_EGenericType ecoreo_egenerictype) {
        this.ecoreo_egenerictype = ecoreo_egenerictype;
    }
    public ecoreO_EClassifier getEcoreo_eclassifier() {
        return ecoreo_eclassifier;
    }

    public void setEcoreo_eclassifier(ecoreO_EClassifier ecoreo_eclassifier) {
        this.ecoreo_eclassifier = ecoreo_eclassifier;
    }

}