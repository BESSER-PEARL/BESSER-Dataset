





import java.util.List;
import java.util.ArrayList;

public class ast_FunctionObjectDeclaration extends CallableElement {

    private String name;





    private ast_FunctionDefinition ast_functiondefinition;




    private ast_FunctionDefinition ast_functiondefinition;




    private List<ast_Expression> ast_expressions;


    public ast_FunctionObjectDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.ast_expressions = new ArrayList<>();
    }

    public ast_FunctionObjectDeclaration(
        String name        ArrayList<ast_Expression> ast_expressions    ) {
        this.name = name;
        this.ast_expressions = ast_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ast_FunctionDefinition getAst_functiondefinition() {
        return ast_functiondefinition;
    }

    public void setAst_functiondefinition(ast_FunctionDefinition ast_functiondefinition) {
        this.ast_functiondefinition = ast_functiondefinition;
    }
    public ast_FunctionDefinition getAst_functiondefinition() {
        return ast_functiondefinition;
    }

    public void setAst_functiondefinition(ast_FunctionDefinition ast_functiondefinition) {
        this.ast_functiondefinition = ast_functiondefinition;
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }

}