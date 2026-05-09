





import java.util.List;
import java.util.ArrayList;

public class javaless_EModelElement extends EObject {






    private javaless_EAnnotation javaless_eannotation;




    private List<javaless_EAnnotation> javaless_eannotations;


    public javaless_EModelElement(
    ) {
        super(
        );
        this.javaless_eannotations = new ArrayList<>();
    }

    public javaless_EModelElement(
        ArrayList<javaless_EAnnotation> javaless_eannotations    ) {
        this.javaless_eannotations = javaless_eannotations;
    }


    public javaless_EAnnotation getJavaless_eannotation() {
        return javaless_eannotation;
    }

    public void setJavaless_eannotation(javaless_EAnnotation javaless_eannotation) {
        this.javaless_eannotation = javaless_eannotation;
    }
    public List<javaless_EAnnotation> getJavaless_eannotations() {
        return javaless_eannotations;
    }

    public void addJavaless_eannotation(Javaless_eannotation javaless_eannotation) {
        this.javaless_eannotations.add(javaless_eannotation);
    }

}