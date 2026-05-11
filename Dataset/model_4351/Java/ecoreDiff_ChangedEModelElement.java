





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEModelElement extends EModelElement {






    private List<ecoreDiff_EModelElement> ecorediff_emodelelements;


    public ecoreDiff_ChangedEModelElement(
    ) {
        super(
        );
        this.ecorediff_emodelelements = new ArrayList<>();
    }

    public ecoreDiff_ChangedEModelElement(
        ArrayList<ecoreDiff_EModelElement> ecorediff_emodelelements    ) {
        this.ecorediff_emodelelements = ecorediff_emodelelements;
    }


    public List<ecoreDiff_EModelElement> getEcorediff_emodelelements() {
        return ecorediff_emodelelements;
    }

    public void addEcorediff_emodelelement(Ecorediff_emodelelement ecorediff_emodelelement) {
        this.ecorediff_emodelelements.add(ecorediff_emodelelement);
    }

}