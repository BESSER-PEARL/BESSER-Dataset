





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEReference extends EReference {






    private List<ecoreDiff_EReference> ecorediff_ereferences;


    public ecoreDiff_ChangedEReference(
    ) {
        super(
        );
        this.ecorediff_ereferences = new ArrayList<>();
    }

    public ecoreDiff_ChangedEReference(
        ArrayList<ecoreDiff_EReference> ecorediff_ereferences    ) {
        this.ecorediff_ereferences = ecorediff_ereferences;
    }


    public List<ecoreDiff_EReference> getEcorediff_ereferences() {
        return ecorediff_ereferences;
    }

    public void addEcorediff_ereference(Ecorediff_ereference ecorediff_ereference) {
        this.ecorediff_ereferences.add(ecorediff_ereference);
    }

}