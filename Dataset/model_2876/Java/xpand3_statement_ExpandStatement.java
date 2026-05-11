





import java.util.List;
import java.util.ArrayList;

public class xpand3_statement_ExpandStatement extends AbstractStatement {

    private boolean foreach;





    private AbstractExpression abstractexpression;




    private List<AbstractExpression> abstractexpressions;




    private AbstractExpression abstractexpression;


    public xpand3_statement_ExpandStatement(
        boolean foreach    ) {
        super(
        );
        this.foreach = foreach;
        this.abstractexpressions = new ArrayList<>();
    }

    public xpand3_statement_ExpandStatement(
        boolean foreach        ArrayList<AbstractExpression> abstractexpressions    ) {
        this.foreach = foreach;
        this.abstractexpressions = abstractexpressions;
    }

    public boolean getForeach() {
        return foreach;
    }

    public void setForeach(boolean foreach) {
        this.foreach = foreach;
    }

    public AbstractExpression getAbstractexpression() {
        return abstractexpression;
    }

    public void setAbstractexpression(AbstractExpression abstractexpression) {
        this.abstractexpression = abstractexpression;
    }
    public List<AbstractExpression> getAbstractexpressions() {
        return abstractexpressions;
    }

    public void addAbstractexpression(Abstractexpression abstractexpression) {
        this.abstractexpressions.add(abstractexpression);
    }
    public AbstractExpression getAbstractexpression() {
        return abstractexpression;
    }

    public void setAbstractexpression(AbstractExpression abstractexpression) {
        this.abstractexpression = abstractexpression;
    }

}