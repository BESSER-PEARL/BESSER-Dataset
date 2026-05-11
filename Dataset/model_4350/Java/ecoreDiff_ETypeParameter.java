





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ETypeParameter extends ENamedElement {






    private ecoreDiff_EGenericType ecorediff_egenerictype;




    private ecoreDiff_EOperation ecorediff_eoperation;




    private List<ecoreDiff_EGenericType> ecorediff_egenerictypes;




    private ecoreDiff_EClassifier ecorediff_eclassifier;


    public ecoreDiff_ETypeParameter(
    ) {
        super(
        );
        this.ecorediff_egenerictypes = new ArrayList<>();
    }

    public ecoreDiff_ETypeParameter(
        ArrayList<ecoreDiff_EGenericType> ecorediff_egenerictypes    ) {
        this.ecorediff_egenerictypes = ecorediff_egenerictypes;
    }


    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }
    public ecoreDiff_EOperation getEcorediff_eoperation() {
        return ecorediff_eoperation;
    }

    public void setEcorediff_eoperation(ecoreDiff_EOperation ecorediff_eoperation) {
        this.ecorediff_eoperation = ecorediff_eoperation;
    }
    public List<ecoreDiff_EGenericType> getEcorediff_egenerictypes() {
        return ecorediff_egenerictypes;
    }

    public void addEcorediff_egenerictype(Ecorediff_egenerictype ecorediff_egenerictype) {
        this.ecorediff_egenerictypes.add(ecorediff_egenerictype);
    }
    public ecoreDiff_EClassifier getEcorediff_eclassifier() {
        return ecorediff_eclassifier;
    }

    public void setEcorediff_eclassifier(ecoreDiff_EClassifier ecorediff_eclassifier) {
        this.ecorediff_eclassifier = ecorediff_eclassifier;
    }

}