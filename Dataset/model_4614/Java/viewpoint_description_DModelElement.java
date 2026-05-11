





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DModelElement  {






    private List<DAnnotation> dannotations;


    public viewpoint_description_DModelElement(
    ) {
        this.dannotations = new ArrayList<>();
    }

    public viewpoint_description_DModelElement(
        ArrayList<DAnnotation> dannotations    ) {
        this.dannotations = dannotations;
    }


    public List<DAnnotation> getDannotations() {
        return dannotations;
    }

    public void addDannotation(Dannotation dannotation) {
        this.dannotations.add(dannotation);
    }

}