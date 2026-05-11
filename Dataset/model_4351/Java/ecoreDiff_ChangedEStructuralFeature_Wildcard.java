





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEStructuralFeature_Wildcard extends EStructuralFeature_Wildcard {






    private List<ecoreDiff_EStructuralFeature_Wildcard> ecorediff_estructuralfeature_wildcards;


    public ecoreDiff_ChangedEStructuralFeature_Wildcard(
    ) {
        super(
        );
        this.ecorediff_estructuralfeature_wildcards = new ArrayList<>();
    }

    public ecoreDiff_ChangedEStructuralFeature_Wildcard(
        ArrayList<ecoreDiff_EStructuralFeature_Wildcard> ecorediff_estructuralfeature_wildcards    ) {
        this.ecorediff_estructuralfeature_wildcards = ecorediff_estructuralfeature_wildcards;
    }


    public List<ecoreDiff_EStructuralFeature_Wildcard> getEcorediff_estructuralfeature_wildcards() {
        return ecorediff_estructuralfeature_wildcards;
    }

    public void addEcorediff_estructuralfeature_wildcard(Ecorediff_estructuralfeature_wildcard ecorediff_estructuralfeature_wildcard) {
        this.ecorediff_estructuralfeature_wildcards.add(ecorediff_estructuralfeature_wildcard);
    }

}