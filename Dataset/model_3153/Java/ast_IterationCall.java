





import java.util.List;
import java.util.ArrayList;

public class ast_IterationCall extends Expression {

    private String identifier;





    private List<ast_IterationVariable> ast_iterationvariables;




    private ast_IterationAccumulator ast_iterationaccumulator;




    private ast_Expression ast_expression;




    private ast_Expression ast_expression;




    private ast_Expression ast_expression;


    public ast_IterationCall(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
        this.ast_iterationvariables = new ArrayList<>();
    }

    public ast_IterationCall(
        String identifier        ArrayList<ast_IterationVariable> ast_iterationvariables    ) {
        this.identifier = identifier;
        this.ast_iterationvariables = ast_iterationvariables;
    }

    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public List<ast_IterationVariable> getAst_iterationvariables() {
        return ast_iterationvariables;
    }

    public void addAst_iterationvariable(Ast_iterationvariable ast_iterationvariable) {
        this.ast_iterationvariables.add(ast_iterationvariable);
    }
    public ast_IterationAccumulator getAst_iterationaccumulator() {
        return ast_iterationaccumulator;
    }

    public void setAst_iterationaccumulator(ast_IterationAccumulator ast_iterationaccumulator) {
        this.ast_iterationaccumulator = ast_iterationaccumulator;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}