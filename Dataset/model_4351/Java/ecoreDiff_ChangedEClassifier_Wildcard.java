





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEClassifier_Wildcard extends EClassifier_Wildcard {






    private List<ecoreDiff_EClassifier_Wildcard> ecorediff_eclassifier_wildcards;


    public ecoreDiff_ChangedEClassifier_Wildcard(
    ) {
        super(
        );
        this.ecorediff_eclassifier_wildcards = new ArrayList<>();
    }

    public ecoreDiff_ChangedEClassifier_Wildcard(
        ArrayList<ecoreDiff_EClassifier_Wildcard> ecorediff_eclassifier_wildcards    ) {
        this.ecorediff_eclassifier_wildcards = ecorediff_eclassifier_wildcards;
    }


    public List<ecoreDiff_EClassifier_Wildcard> getEcorediff_eclassifier_wildcards() {
        return ecorediff_eclassifier_wildcards;
    }

    public void addEcorediff_eclassifier_wildcard(Ecorediff_eclassifier_wildcard ecorediff_eclassifier_wildcard) {
        this.ecorediff_eclassifier_wildcards.add(ecorediff_eclassifier_wildcard);
    }

}