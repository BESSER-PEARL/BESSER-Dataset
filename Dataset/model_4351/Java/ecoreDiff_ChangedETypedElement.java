





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedETypedElement extends ETypedElement {






    private List<ecoreDiff_ETypedElement> ecorediff_etypedelements;


    public ecoreDiff_ChangedETypedElement(
    ) {
        super(
        );
        this.ecorediff_etypedelements = new ArrayList<>();
    }

    public ecoreDiff_ChangedETypedElement(
        ArrayList<ecoreDiff_ETypedElement> ecorediff_etypedelements    ) {
        this.ecorediff_etypedelements = ecorediff_etypedelements;
    }


    public List<ecoreDiff_ETypedElement> getEcorediff_etypedelements() {
        return ecorediff_etypedelements;
    }

    public void addEcorediff_etypedelement(Ecorediff_etypedelement ecorediff_etypedelement) {
        this.ecorediff_etypedelements.add(ecorediff_etypedelement);
    }

}