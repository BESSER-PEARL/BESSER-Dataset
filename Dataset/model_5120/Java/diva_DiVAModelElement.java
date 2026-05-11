





import java.util.List;
import java.util.ArrayList;

public class diva_DiVAModelElement  {






    private List<diva_Annotation> diva_annotations;


    public diva_DiVAModelElement(
    ) {
        this.diva_annotations = new ArrayList<>();
    }

    public diva_DiVAModelElement(
        ArrayList<diva_Annotation> diva_annotations    ) {
        this.diva_annotations = diva_annotations;
    }


    public List<diva_Annotation> getDiva_annotations() {
        return diva_annotations;
    }

    public void addDiva_annotation(Diva_annotation diva_annotation) {
        this.diva_annotations.add(diva_annotation);
    }

}