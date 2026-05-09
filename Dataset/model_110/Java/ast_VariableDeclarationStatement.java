





import java.util.List;
import java.util.ArrayList;

public class ast_VariableDeclarationStatement extends Statement {






    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_Type ast_type;


    public ast_VariableDeclarationStatement(
    ) {
        super(
        );
        this.ast_iextendedmodifiers = new ArrayList<>();
    }

    public ast_VariableDeclarationStatement(
        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers    ) {
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
    }


    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }

}