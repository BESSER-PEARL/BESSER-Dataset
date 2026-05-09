





import java.util.List;
import java.util.ArrayList;

public class eol_ExecutableAnnotation extends Annotation {






    private eol_Expression eol_expression;




    private eol_AnnotationBlock eol_annotationblock;


    public eol_ExecutableAnnotation(
    ) {
        super(
        );
    }



    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }
    public eol_AnnotationBlock getEol_annotationblock() {
        return eol_annotationblock;
    }

    public void setEol_annotationblock(eol_AnnotationBlock eol_annotationblock) {
        this.eol_annotationblock = eol_annotationblock;
    }

}