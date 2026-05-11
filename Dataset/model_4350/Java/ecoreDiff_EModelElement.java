





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EModelElement extends EObject, DifferenceElement {






    private ecoreDiff_ChangedEModelElement ecorediff_changedemodelelement;




    private ecoreDiff_EAnnotation ecorediff_eannotation;




    private List<ecoreDiff_EAnnotation> ecorediff_eannotations;


    public ecoreDiff_EModelElement(
    ) {
        super(
        );
        this.ecorediff_eannotations = new ArrayList<>();
    }

    public ecoreDiff_EModelElement(
        ArrayList<ecoreDiff_EAnnotation> ecorediff_eannotations    ) {
        this.ecorediff_eannotations = ecorediff_eannotations;
    }


    public ecoreDiff_ChangedEModelElement getEcorediff_changedemodelelement() {
        return ecorediff_changedemodelelement;
    }

    public void setEcorediff_changedemodelelement(ecoreDiff_ChangedEModelElement ecorediff_changedemodelelement) {
        this.ecorediff_changedemodelelement = ecorediff_changedemodelelement;
    }
    public ecoreDiff_EAnnotation getEcorediff_eannotation() {
        return ecorediff_eannotation;
    }

    public void setEcorediff_eannotation(ecoreDiff_EAnnotation ecorediff_eannotation) {
        this.ecorediff_eannotation = ecorediff_eannotation;
    }
    public List<ecoreDiff_EAnnotation> getEcorediff_eannotations() {
        return ecorediff_eannotations;
    }

    public void addEcorediff_eannotation(Ecorediff_eannotation ecorediff_eannotation) {
        this.ecorediff_eannotations.add(ecorediff_eannotation);
    }

}