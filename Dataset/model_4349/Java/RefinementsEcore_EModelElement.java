





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EModelElement  {






    private RefinementsEcore_EAnnotation refinementsecore_eannotation;




    private List<RefinementsEcore_EAnnotation> refinementsecore_eannotations;


    public RefinementsEcore_EModelElement(
    ) {
        this.refinementsecore_eannotations = new ArrayList<>();
    }

    public RefinementsEcore_EModelElement(
        ArrayList<RefinementsEcore_EAnnotation> refinementsecore_eannotations    ) {
        this.refinementsecore_eannotations = refinementsecore_eannotations;
    }


    public RefinementsEcore_EAnnotation getRefinementsecore_eannotation() {
        return refinementsecore_eannotation;
    }

    public void setRefinementsecore_eannotation(RefinementsEcore_EAnnotation refinementsecore_eannotation) {
        this.refinementsecore_eannotation = refinementsecore_eannotation;
    }
    public List<RefinementsEcore_EAnnotation> getRefinementsecore_eannotations() {
        return refinementsecore_eannotations;
    }

    public void addRefinementsecore_eannotation(Refinementsecore_eannotation refinementsecore_eannotation) {
        this.refinementsecore_eannotations.add(refinementsecore_eannotation);
    }

}