





import java.util.List;
import java.util.ArrayList;

public class ecore_EModelElement extends EObject {






    private ecore_EAnnotation ecore_eannotation;




    private List<ecore_EAnnotation> ecore_eannotations;


    public ecore_EModelElement(
    ) {
        super(
        );
        this.ecore_eannotations = new ArrayList<>();
    }

    public ecore_EModelElement(
        ArrayList<ecore_EAnnotation> ecore_eannotations    ) {
        this.ecore_eannotations = ecore_eannotations;
    }


    public ecore_EAnnotation getEcore_eannotation() {
        return ecore_eannotation;
    }

    public void setEcore_eannotation(ecore_EAnnotation ecore_eannotation) {
        this.ecore_eannotation = ecore_eannotation;
    }
    public List<ecore_EAnnotation> getEcore_eannotations() {
        return ecore_eannotations;
    }

    public void addEcore_eannotation(Ecore_eannotation ecore_eannotation) {
        this.ecore_eannotations.add(ecore_eannotation);
    }

}