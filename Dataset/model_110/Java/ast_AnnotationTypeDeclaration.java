





import java.util.List;
import java.util.ArrayList;

public class ast_AnnotationTypeDeclaration extends AbstractTypeDeclaration {






    private ast_SimpleName ast_simplename;




    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private List<ast_BodyDeclaration> ast_bodydeclarations;




    private ast_Javadoc ast_javadoc;


    public ast_AnnotationTypeDeclaration(
    ) {
        super(
        );
        this.ast_iextendedmodifiers = new ArrayList<>();
        this.ast_bodydeclarations = new ArrayList<>();
    }

    public ast_AnnotationTypeDeclaration(
        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers,        ArrayList<ast_BodyDeclaration> ast_bodydeclarations    ) {
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
        this.ast_bodydeclarations = ast_bodydeclarations;
    }


    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public List<ast_BodyDeclaration> getAst_bodydeclarations() {
        return ast_bodydeclarations;
    }

    public void addAst_bodydeclaration(Ast_bodydeclaration ast_bodydeclaration) {
        this.ast_bodydeclarations.add(ast_bodydeclaration);
    }
    public ast_Javadoc getAst_javadoc() {
        return ast_javadoc;
    }

    public void setAst_javadoc(ast_Javadoc ast_javadoc) {
        this.ast_javadoc = ast_javadoc;
    }

}