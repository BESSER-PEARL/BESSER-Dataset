





import java.util.List;
import java.util.ArrayList;

public class SPL_ForeachStat extends Statement {

    private String iteratorName;





    private SPL_Expression spl_expression;




    private List<SPL_Statement> spl_statements;


    public SPL_ForeachStat(
        String iteratorName    ) {
        super(
        );
        this.iteratorName = iteratorName;
        this.spl_statements = new ArrayList<>();
    }

    public SPL_ForeachStat(
        String iteratorName        ArrayList<SPL_Statement> spl_statements    ) {
        this.iteratorName = iteratorName;
        this.spl_statements = spl_statements;
    }

    public String getIteratorname() {
        return iteratorName;
    }

    public void setIteratorname(String iteratorName) {
        this.iteratorName = iteratorName;
    }

    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }
    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }

}