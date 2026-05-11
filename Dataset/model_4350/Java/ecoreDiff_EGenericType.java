





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EGenericType extends EObject {






    private ecoreDiff_EGenericType ecorediff_egenerictype;




    private ecoreDiff_EGenericType ecorediff_egenerictype;




    private ecoreDiff_EClass ecorediff_eclass;




    private List<ecoreDiff_EGenericType> ecorediff_egenerictypes;




    private ecoreDiff_EClass ecorediff_eclass;




    private ecoreDiff_EOperation ecorediff_eoperation;


    public ecoreDiff_EGenericType(
    ) {
        super(
        );
        this.ecorediff_egenerictypes = new ArrayList<>();
    }

    public ecoreDiff_EGenericType(
        ArrayList<ecoreDiff_EGenericType> ecorediff_egenerictypes    ) {
        this.ecorediff_egenerictypes = ecorediff_egenerictypes;
    }


    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }
    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public List<ecoreDiff_EGenericType> getEcorediff_egenerictypes() {
        return ecorediff_egenerictypes;
    }

    public void addEcorediff_egenerictype(Ecorediff_egenerictype ecorediff_egenerictype) {
        this.ecorediff_egenerictypes.add(ecorediff_egenerictype);
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public ecoreDiff_EOperation getEcorediff_eoperation() {
        return ecorediff_eoperation;
    }

    public void setEcorediff_eoperation(ecoreDiff_EOperation ecorediff_eoperation) {
        this.ecorediff_eoperation = ecorediff_eoperation;
    }

}