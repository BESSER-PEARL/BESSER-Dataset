





import java.util.List;
import java.util.ArrayList;

public class dom_SimpleAnnotation extends Annotation {






    private List<dom_StringExpression> dom_stringexpressions;




    private dom_AnnotationBlock dom_annotationblock;


    public dom_SimpleAnnotation(
    ) {
        super(
        );
        this.dom_stringexpressions = new ArrayList<>();
    }

    public dom_SimpleAnnotation(
        ArrayList<dom_StringExpression> dom_stringexpressions    ) {
        this.dom_stringexpressions = dom_stringexpressions;
    }


    public List<dom_StringExpression> getDom_stringexpressions() {
        return dom_stringexpressions;
    }

    public void addDom_stringexpression(Dom_stringexpression dom_stringexpression) {
        this.dom_stringexpressions.add(dom_stringexpression);
    }
    public dom_AnnotationBlock getDom_annotationblock() {
        return dom_annotationblock;
    }

    public void setDom_annotationblock(dom_AnnotationBlock dom_annotationblock) {
        this.dom_annotationblock = dom_annotationblock;
    }

}