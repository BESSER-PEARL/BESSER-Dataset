





import java.util.List;
import java.util.ArrayList;

public class ast_EnumDeclaration extends AbstractTypeDeclaration {






    private List<ast_BodyDeclaration> ast_bodydeclarations;




    private List<ast_EnumConstantDeclaration> ast_enumconstantdeclarations;




    private List<ast_Type> ast_types;




    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_Javadoc ast_javadoc;




    private ast_SimpleName ast_simplename;


    public ast_EnumDeclaration(
    ) {
        super(
        );
        this.ast_bodydeclarations = new ArrayList<>();
        this.ast_enumconstantdeclarations = new ArrayList<>();
        this.ast_types = new ArrayList<>();
        this.ast_iextendedmodifiers = new ArrayList<>();
    }

    public ast_EnumDeclaration(
        ArrayList<ast_BodyDeclaration> ast_bodydeclarations,        ArrayList<ast_EnumConstantDeclaration> ast_enumconstantdeclarations,        ArrayList<ast_Type> ast_types,        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers    ) {
        this.ast_bodydeclarations = ast_bodydeclarations;
        this.ast_enumconstantdeclarations = ast_enumconstantdeclarations;
        this.ast_types = ast_types;
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
    }


    public List<ast_BodyDeclaration> getAst_bodydeclarations() {
        return ast_bodydeclarations;
    }

    public void addAst_bodydeclaration(Ast_bodydeclaration ast_bodydeclaration) {
        this.ast_bodydeclarations.add(ast_bodydeclaration);
    }
    public List<ast_EnumConstantDeclaration> getAst_enumconstantdeclarations() {
        return ast_enumconstantdeclarations;
    }

    public void addAst_enumconstantdeclaration(Ast_enumconstantdeclaration ast_enumconstantdeclaration) {
        this.ast_enumconstantdeclarations.add(ast_enumconstantdeclaration);
    }
    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }
    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_Javadoc getAst_javadoc() {
        return ast_javadoc;
    }

    public void setAst_javadoc(ast_Javadoc ast_javadoc) {
        this.ast_javadoc = ast_javadoc;
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}