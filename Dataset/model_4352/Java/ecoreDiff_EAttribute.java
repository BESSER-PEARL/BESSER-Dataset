





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EAttribute extends EStructuralFeature {

    private boolean iD;





    private ecoreDiff_ChangedEAttribute ecorediff_changedeattribute;




    private ecoreDiff_EReference ecorediff_ereference;


    public ecoreDiff_EAttribute(
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

    public ecoreDiff_ChangedEAttribute getEcorediff_changedeattribute() {
        return ecorediff_changedeattribute;
    }

    public void setEcorediff_changedeattribute(ecoreDiff_ChangedEAttribute ecorediff_changedeattribute) {
        this.ecorediff_changedeattribute = ecorediff_changedeattribute;
    }
    public ecoreDiff_EReference getEcorediff_ereference() {
        return ecorediff_ereference;
    }

    public void setEcorediff_ereference(ecoreDiff_EReference ecorediff_ereference) {
        this.ecorediff_ereference = ecorediff_ereference;
    }

}