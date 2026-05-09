





import java.util.List;
import java.util.ArrayList;

public class ast_LabeledStatement extends Statement {






    private ast_SimpleName ast_simplename;




    private ast_Statement ast_statement;


    public ast_LabeledStatement(
    ) {
        super(
        );
    }



    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public ast_Statement getAst_statement() {
        return ast_statement;
    }

    public void setAst_statement(ast_Statement ast_statement) {
        this.ast_statement = ast_statement;
    }

}