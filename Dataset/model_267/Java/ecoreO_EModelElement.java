





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EModelElement  {






    private List<ecoreO_EAnnotation> ecoreo_eannotations;




    private ecoreO_EAnnotation ecoreo_eannotation;


    public ecoreO_EModelElement(
    ) {
        this.ecoreo_eannotations = new ArrayList<>();
    }

    public ecoreO_EModelElement(
        ArrayList<ecoreO_EAnnotation> ecoreo_eannotations    ) {
        this.ecoreo_eannotations = ecoreo_eannotations;
    }


    public List<ecoreO_EAnnotation> getEcoreo_eannotations() {
        return ecoreo_eannotations;
    }

    public void addEcoreo_eannotation(Ecoreo_eannotation ecoreo_eannotation) {
        this.ecoreo_eannotations.add(ecoreo_eannotation);
    }
    public ecoreO_EAnnotation getEcoreo_eannotation() {
        return ecoreo_eannotation;
    }

    public void setEcoreo_eannotation(ecoreO_EAnnotation ecoreo_eannotation) {
        this.ecoreo_eannotation = ecoreo_eannotation;
    }

}