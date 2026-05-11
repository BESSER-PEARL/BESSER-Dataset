





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Conditional extends Statement {






    private CompleteDSLPckg_Expression completedslpckg_expression;




    private List<CompleteDSLPckg_Statement> completedslpckg_statements;


    public CompleteDSLPckg_Conditional(
    ) {
        super(
        );
        this.completedslpckg_statements = new ArrayList<>();
    }

    public CompleteDSLPckg_Conditional(
        ArrayList<CompleteDSLPckg_Statement> completedslpckg_statements    ) {
        this.completedslpckg_statements = completedslpckg_statements;
    }


    public CompleteDSLPckg_Expression getCompletedslpckg_expression() {
        return completedslpckg_expression;
    }

    public void setCompletedslpckg_expression(CompleteDSLPckg_Expression completedslpckg_expression) {
        this.completedslpckg_expression = completedslpckg_expression;
    }
    public List<CompleteDSLPckg_Statement> getCompletedslpckg_statements() {
        return completedslpckg_statements;
    }

    public void addCompletedslpckg_statement(Completedslpckg_statement completedslpckg_statement) {
        this.completedslpckg_statements.add(completedslpckg_statement);
    }

}