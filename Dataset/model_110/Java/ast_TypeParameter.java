





import java.util.List;
import java.util.ArrayList;

public class ast_TypeParameter extends ASTNode {






    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_SimpleName ast_simplename;


    public ast_TypeParameter(
    ) {
        super(
        );
        this.ast_iextendedmodifiers = new ArrayList<>();
    }

    public ast_TypeParameter(
        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers    ) {
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
    }


    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}