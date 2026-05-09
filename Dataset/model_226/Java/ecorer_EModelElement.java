





import java.util.List;
import java.util.ArrayList;

public class ecorer_EModelElement  {






    private ecorer_EAnnotation ecorer_eannotation;




    private List<ecorer_EAnnotation> ecorer_eannotations;


    public ecorer_EModelElement(
    ) {
        this.ecorer_eannotations = new ArrayList<>();
    }

    public ecorer_EModelElement(
        ArrayList<ecorer_EAnnotation> ecorer_eannotations    ) {
        this.ecorer_eannotations = ecorer_eannotations;
    }


    public ecorer_EAnnotation getEcorer_eannotation() {
        return ecorer_eannotation;
    }

    public void setEcorer_eannotation(ecorer_EAnnotation ecorer_eannotation) {
        this.ecorer_eannotation = ecorer_eannotation;
    }
    public List<ecorer_EAnnotation> getEcorer_eannotations() {
        return ecorer_eannotations;
    }

    public void addEcorer_eannotation(Ecorer_eannotation ecorer_eannotation) {
        this.ecorer_eannotations.add(ecorer_eannotation);
    }

}