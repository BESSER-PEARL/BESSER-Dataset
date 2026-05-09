





import java.util.List;
import java.util.ArrayList;

public class encore_EModelElement  {






    private List<encore_EAnnotation> encore_eannotations;




    private encore_EAnnotation encore_eannotation;


    public encore_EModelElement(
    ) {
        this.encore_eannotations = new ArrayList<>();
    }

    public encore_EModelElement(
        ArrayList<encore_EAnnotation> encore_eannotations    ) {
        this.encore_eannotations = encore_eannotations;
    }


    public List<encore_EAnnotation> getEncore_eannotations() {
        return encore_eannotations;
    }

    public void addEncore_eannotation(Encore_eannotation encore_eannotation) {
        this.encore_eannotations.add(encore_eannotation);
    }
    public encore_EAnnotation getEncore_eannotation() {
        return encore_eannotation;
    }

    public void setEncore_eannotation(encore_EAnnotation encore_eannotation) {
        this.encore_eannotation = encore_eannotation;
    }

}