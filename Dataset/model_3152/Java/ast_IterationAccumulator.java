





import java.util.List;
import java.util.ArrayList;

public class ast_IterationAccumulator extends CallableElement {

    private String name;





    private ast_Expression ast_expression;


    public ast_IterationAccumulator(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}