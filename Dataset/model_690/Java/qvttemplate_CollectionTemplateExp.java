





import java.util.List;
import java.util.ArrayList;

public class qvttemplate_CollectionTemplateExp extends TemplateExp {

    private String kind;





    private List<OclExpression> oclexpressions;




    private OclExpression oclexpression;


    public qvttemplate_CollectionTemplateExp(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.oclexpressions = new ArrayList<>();
    }

    public qvttemplate_CollectionTemplateExp(
        String kind        ArrayList<OclExpression> oclexpressions    ) {
        this.kind = kind;
        this.oclexpressions = oclexpressions;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}