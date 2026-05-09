





import java.util.List;
import java.util.ArrayList;

public class eol_SimpleAnnotationStatement extends AnnotationStatement {






    private List<eol_StringExpression> eol_stringexpressions;


    public eol_SimpleAnnotationStatement(
    ) {
        super(
        );
        this.eol_stringexpressions = new ArrayList<>();
    }

    public eol_SimpleAnnotationStatement(
        ArrayList<eol_StringExpression> eol_stringexpressions    ) {
        this.eol_stringexpressions = eol_stringexpressions;
    }


    public List<eol_StringExpression> getEol_stringexpressions() {
        return eol_stringexpressions;
    }

    public void addEol_stringexpression(Eol_stringexpression eol_stringexpression) {
        this.eol_stringexpressions.add(eol_stringexpression);
    }

}