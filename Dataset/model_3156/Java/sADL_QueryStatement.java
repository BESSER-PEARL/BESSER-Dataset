





import java.util.List;
import java.util.ArrayList;

public class sADL_QueryStatement extends ExpressionScope {

    private String start;





    private List<sADL_NamedStructureAnnotation> sadl_namedstructureannotations;




    private sADL_SadlResource sadl_sadlresource;




    private sADL_Expression sadl_expression;


    public sADL_QueryStatement(
        String start    ) {
        super(
        );
        this.start = start;
        this.sadl_namedstructureannotations = new ArrayList<>();
    }

    public sADL_QueryStatement(
        String start        ArrayList<sADL_NamedStructureAnnotation> sadl_namedstructureannotations    ) {
        this.start = start;
        this.sadl_namedstructureannotations = sadl_namedstructureannotations;
    }

    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public List<sADL_NamedStructureAnnotation> getSadl_namedstructureannotations() {
        return sadl_namedstructureannotations;
    }

    public void addSadl_namedstructureannotation(Sadl_namedstructureannotation sadl_namedstructureannotation) {
        this.sadl_namedstructureannotations.add(sadl_namedstructureannotation);
    }
    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }

}