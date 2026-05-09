





import java.util.List;
import java.util.ArrayList;

public class ast_EnumLiteral extends ClassifierMemberStatement {






    private ast_ClassBlock ast_classblock;




    private ast_Identifier ast_identifier;




    private List<ast_Expression> ast_expressions;


    public ast_EnumLiteral(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
    }

    public ast_EnumLiteral(
        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
    }


    public ast_ClassBlock getAst_classblock() {
        return ast_classblock;
    }

    public void setAst_classblock(ast_ClassBlock ast_classblock) {
        this.ast_classblock = ast_classblock;
    }
    public ast_Identifier getAst_identifier() {
        return ast_identifier;
    }

    public void setAst_identifier(ast_Identifier ast_identifier) {
        this.ast_identifier = ast_identifier;
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }

}