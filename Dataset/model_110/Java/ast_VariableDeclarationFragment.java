





import java.util.List;
import java.util.ArrayList;

public class ast_VariableDeclarationFragment extends VariableDeclaration {






    private ast_FieldDeclaration ast_fielddeclaration;




    private ast_VariableDeclarationExpression ast_variabledeclarationexpression;




    private List<ast_Dimension> ast_dimensions;




    private ast_SimpleName ast_simplename;




    private ast_VariableDeclarationStatement ast_variabledeclarationstatement;




    private ast_Expression ast_expression;


    public ast_VariableDeclarationFragment(
    ) {
        super(
        );
        this.ast_dimensions = new ArrayList<>();
    }

    public ast_VariableDeclarationFragment(
        ArrayList<ast_Dimension> ast_dimensions    ) {
        this.ast_dimensions = ast_dimensions;
    }


    public ast_FieldDeclaration getAst_fielddeclaration() {
        return ast_fielddeclaration;
    }

    public void setAst_fielddeclaration(ast_FieldDeclaration ast_fielddeclaration) {
        this.ast_fielddeclaration = ast_fielddeclaration;
    }
    public ast_VariableDeclarationExpression getAst_variabledeclarationexpression() {
        return ast_variabledeclarationexpression;
    }

    public void setAst_variabledeclarationexpression(ast_VariableDeclarationExpression ast_variabledeclarationexpression) {
        this.ast_variabledeclarationexpression = ast_variabledeclarationexpression;
    }
    public List<ast_Dimension> getAst_dimensions() {
        return ast_dimensions;
    }

    public void addAst_dimension(Ast_dimension ast_dimension) {
        this.ast_dimensions.add(ast_dimension);
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public ast_VariableDeclarationStatement getAst_variabledeclarationstatement() {
        return ast_variabledeclarationstatement;
    }

    public void setAst_variabledeclarationstatement(ast_VariableDeclarationStatement ast_variabledeclarationstatement) {
        this.ast_variabledeclarationstatement = ast_variabledeclarationstatement;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}