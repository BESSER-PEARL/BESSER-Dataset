





import java.util.List;
import java.util.ArrayList;

public class basic_TAnnotatable  {






    private List<basic_TAnnotation> basic_tannotations;




    private basic_TAnnotation basic_tannotation;


    public basic_TAnnotatable(
    ) {
        this.basic_tannotations = new ArrayList<>();
    }

    public basic_TAnnotatable(
        ArrayList<basic_TAnnotation> basic_tannotations    ) {
        this.basic_tannotations = basic_tannotations;
    }


    public List<basic_TAnnotation> getBasic_tannotations() {
        return basic_tannotations;
    }

    public void addBasic_tannotation(Basic_tannotation basic_tannotation) {
        this.basic_tannotations.add(basic_tannotation);
    }
    public basic_TAnnotation getBasic_tannotation() {
        return basic_tannotation;
    }

    public void setBasic_tannotation(basic_TAnnotation basic_tannotation) {
        this.basic_tannotation = basic_tannotation;
    }

}