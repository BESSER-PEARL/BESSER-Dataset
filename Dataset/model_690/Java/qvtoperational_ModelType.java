





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_ModelType extends URIExtent, Class {

    private String conformanceKind;





    private List<OclExpression> oclexpressions;


    public qvtoperational_ModelType(
        String conformanceKind    ) {
        super(
        );
        this.conformanceKind = conformanceKind;
        this.oclexpressions = new ArrayList<>();
    }

    public qvtoperational_ModelType(
        String conformanceKind        ArrayList<OclExpression> oclexpressions    ) {
        this.conformanceKind = conformanceKind;
        this.oclexpressions = oclexpressions;
    }

    public String getConformancekind() {
        return conformanceKind;
    }

    public void setConformancekind(String conformanceKind) {
        this.conformanceKind = conformanceKind;
    }

    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}