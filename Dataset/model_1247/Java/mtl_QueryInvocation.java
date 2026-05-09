





import java.util.List;
import java.util.ArrayList;

public class mtl_QueryInvocation extends TemplateExpression {






    private mtl_Query mtl_query;




    private List<OCLExpression> oclexpressions;


    public mtl_QueryInvocation(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public mtl_QueryInvocation(
        ArrayList<OCLExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public mtl_Query getMtl_query() {
        return mtl_query;
    }

    public void setMtl_query(mtl_Query mtl_query) {
        this.mtl_query = mtl_query;
    }
    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}