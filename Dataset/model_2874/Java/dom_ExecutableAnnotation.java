





import java.util.List;
import java.util.ArrayList;

public class dom_ExecutableAnnotation extends Annotation {






    private dom_Expression dom_expression;




    private dom_AnnotationBlock dom_annotationblock;


    public dom_ExecutableAnnotation(
    ) {
        super(
        );
    }



    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public dom_AnnotationBlock getDom_annotationblock() {
        return dom_annotationblock;
    }

    public void setDom_annotationblock(dom_AnnotationBlock dom_annotationblock) {
        this.dom_annotationblock = dom_annotationblock;
    }

}