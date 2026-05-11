





import java.util.List;
import java.util.ArrayList;

public class ast_Check  {






    private ast_FunctionDefinition ast_functiondefinition;




    private ast_FunctionDefinition ast_functiondefinition;




    private List<ast_Expression> ast_expressions;




    private List<ast_DataTypeSpecifier> ast_datatypespecifiers;




    private List<ast_DataTypeSpecifier> ast_datatypespecifiers;


    public ast_Check(
    ) {
        this.ast_expressions = new ArrayList<>();
        this.ast_datatypespecifiers = new ArrayList<>();
        this.ast_datatypespecifiers = new ArrayList<>();
    }

    public ast_Check(
        ArrayList<ast_Expression> ast_expressions,        ArrayList<ast_DataTypeSpecifier> ast_datatypespecifiers,        ArrayList<ast_DataTypeSpecifier> ast_datatypespecifiers    ) {
        this.ast_expressions = ast_expressions;
        this.ast_datatypespecifiers = ast_datatypespecifiers;
        this.ast_datatypespecifiers = ast_datatypespecifiers;
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
    public List<ast_DataTypeSpecifier> getAst_datatypespecifiers() {
        return ast_datatypespecifiers;
    }

    public void addAst_datatypespecifier(Ast_datatypespecifier ast_datatypespecifier) {
        this.ast_datatypespecifiers.add(ast_datatypespecifier);
    }
    public List<ast_DataTypeSpecifier> getAst_datatypespecifiers() {
        return ast_datatypespecifiers;
    }

    public void addAst_datatypespecifier(Ast_datatypespecifier ast_datatypespecifier) {
        this.ast_datatypespecifiers.add(ast_datatypespecifier);
    }

}