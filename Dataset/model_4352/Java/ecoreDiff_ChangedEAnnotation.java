





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEAnnotation extends EAnnotation {






    private ecoreDiff_EObject ecorediff_eobject;




    private List<ecoreDiff_EAnnotation> ecorediff_eannotations;


    public ecoreDiff_ChangedEAnnotation(
    ) {
        super(
        );
        this.ecorediff_eannotations = new ArrayList<>();
    }

    public ecoreDiff_ChangedEAnnotation(
        ArrayList<ecoreDiff_EAnnotation> ecorediff_eannotations    ) {
        this.ecorediff_eannotations = ecorediff_eannotations;
    }


    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }
    public List<ecoreDiff_EAnnotation> getEcorediff_eannotations() {
        return ecorediff_eannotations;
    }

    public void addEcorediff_eannotation(Ecorediff_eannotation ecorediff_eannotation) {
        this.ecorediff_eannotations.add(ecorediff_eannotation);
    }

}