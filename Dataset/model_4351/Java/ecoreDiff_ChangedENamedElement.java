





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedENamedElement extends ENamedElement {






    private List<ecoreDiff_ENamedElement> ecorediff_enamedelements;


    public ecoreDiff_ChangedENamedElement(
    ) {
        super(
        );
        this.ecorediff_enamedelements = new ArrayList<>();
    }

    public ecoreDiff_ChangedENamedElement(
        ArrayList<ecoreDiff_ENamedElement> ecorediff_enamedelements    ) {
        this.ecorediff_enamedelements = ecorediff_enamedelements;
    }


    public List<ecoreDiff_ENamedElement> getEcorediff_enamedelements() {
        return ecorediff_enamedelements;
    }

    public void addEcorediff_enamedelement(Ecorediff_enamedelement ecorediff_enamedelement) {
        this.ecorediff_enamedelements.add(ecorediff_enamedelement);
    }

}