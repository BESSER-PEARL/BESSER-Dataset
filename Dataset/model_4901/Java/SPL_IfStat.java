





import java.util.List;
import java.util.ArrayList;

public class SPL_IfStat extends Statement {






    private List<SPL_Statement> spl_statements;




    private List<SPL_Statement> spl_statements;




    private SPL_Expression spl_expression;


    public SPL_IfStat(
    ) {
        super(
        );
        this.spl_statements = new ArrayList<>();
        this.spl_statements = new ArrayList<>();
    }

    public SPL_IfStat(
        ArrayList<SPL_Statement> spl_statements,        ArrayList<SPL_Statement> spl_statements    ) {
        this.spl_statements = spl_statements;
        this.spl_statements = spl_statements;
    }


    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }
    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }
    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }

}