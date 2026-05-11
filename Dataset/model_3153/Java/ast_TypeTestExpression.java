





import java.util.List;
import java.util.ArrayList;

public class ast_TypeTestExpression extends Expression {






    private ast_Expression ast_expression;




    private ast_DataTypeSpecifier ast_datatypespecifier;


    public ast_TypeTestExpression(
    ) {
        super(
        );
    }



    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_DataTypeSpecifier getAst_datatypespecifier() {
        return ast_datatypespecifier;
    }

    public void setAst_datatypespecifier(ast_DataTypeSpecifier ast_datatypespecifier) {
        this.ast_datatypespecifier = ast_datatypespecifier;
    }

}