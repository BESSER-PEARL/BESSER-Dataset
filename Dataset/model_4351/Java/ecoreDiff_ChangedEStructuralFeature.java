





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEStructuralFeature extends EStructuralFeature {






    private List<ecoreDiff_EStructuralFeature> ecorediff_estructuralfeatures;


    public ecoreDiff_ChangedEStructuralFeature(
    ) {
        super(
        );
        this.ecorediff_estructuralfeatures = new ArrayList<>();
    }

    public ecoreDiff_ChangedEStructuralFeature(
        ArrayList<ecoreDiff_EStructuralFeature> ecorediff_estructuralfeatures    ) {
        this.ecorediff_estructuralfeatures = ecorediff_estructuralfeatures;
    }


    public List<ecoreDiff_EStructuralFeature> getEcorediff_estructuralfeatures() {
        return ecorediff_estructuralfeatures;
    }

    public void addEcorediff_estructuralfeature(Ecorediff_estructuralfeature ecorediff_estructuralfeature) {
        this.ecorediff_estructuralfeatures.add(ecorediff_estructuralfeature);
    }

}