





import java.util.List;
import java.util.ArrayList;

public class eol_SimpleAnnotation extends Annotation {






    private eol_AnnotationBlock eol_annotationblock;




    private List<eol_StringExpression> eol_stringexpressions;


    public eol_SimpleAnnotation(
    ) {
        super(
        );
        this.eol_stringexpressions = new ArrayList<>();
    }

    public eol_SimpleAnnotation(
        ArrayList<eol_StringExpression> eol_stringexpressions    ) {
        this.eol_stringexpressions = eol_stringexpressions;
    }


    public eol_AnnotationBlock getEol_annotationblock() {
        return eol_annotationblock;
    }

    public void setEol_annotationblock(eol_AnnotationBlock eol_annotationblock) {
        this.eol_annotationblock = eol_annotationblock;
    }
    public List<eol_StringExpression> getEol_stringexpressions() {
        return eol_stringexpressions;
    }

    public void addEol_stringexpression(Eol_stringexpression eol_stringexpression) {
        this.eol_stringexpressions.add(eol_stringexpression);
    }

}