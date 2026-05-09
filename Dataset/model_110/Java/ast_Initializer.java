





import java.util.List;
import java.util.ArrayList;

public class ast_Initializer extends BodyDeclaration {






    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_Block ast_block;


    public ast_Initializer(
    ) {
        super(
        );
        this.ast_iextendedmodifiers = new ArrayList<>();
    }

    public ast_Initializer(
        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers    ) {
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
    }


    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_Block getAst_block() {
        return ast_block;
    }

    public void setAst_block(ast_Block ast_block) {
        this.ast_block = ast_block;
    }

}