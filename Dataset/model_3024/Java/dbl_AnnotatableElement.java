





import java.util.List;
import java.util.ArrayList;

public class dbl_AnnotatableElement  {






    private List<dbl_SimpleAnnotation> dbl_simpleannotations;


    public dbl_AnnotatableElement(
    ) {
        this.dbl_simpleannotations = new ArrayList<>();
    }

    public dbl_AnnotatableElement(
        ArrayList<dbl_SimpleAnnotation> dbl_simpleannotations    ) {
        this.dbl_simpleannotations = dbl_simpleannotations;
    }


    public List<dbl_SimpleAnnotation> getDbl_simpleannotations() {
        return dbl_simpleannotations;
    }

    public void addDbl_simpleannotation(Dbl_simpleannotation dbl_simpleannotation) {
        this.dbl_simpleannotations.add(dbl_simpleannotation);
    }

}