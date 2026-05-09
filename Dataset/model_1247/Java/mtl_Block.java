





import java.util.List;
import java.util.ArrayList;

public class mtl_Block extends TemplateExpression {






    private List<OCLExpression> oclexpressions;


    public mtl_Block(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public mtl_Block(
        ArrayList<OCLExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}