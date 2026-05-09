





import java.util.List;
import java.util.ArrayList;

public class DOM_BodyDeclaration extends ASTNode {






    private Javadoc javadoc;




    private List<ExtendedModifier> extendedmodifiers;


    public DOM_BodyDeclaration(
    ) {
        super(
        );
        this.extendedmodifiers = new ArrayList<>();
    }

    public DOM_BodyDeclaration(
        ArrayList<ExtendedModifier> extendedmodifiers    ) {
        this.extendedmodifiers = extendedmodifiers;
    }


    public Javadoc getJavadoc() {
        return javadoc;
    }

    public void setJavadoc(Javadoc javadoc) {
        this.javadoc = javadoc;
    }
    public List<ExtendedModifier> getExtendedmodifiers() {
        return extendedmodifiers;
    }

    public void addExtendedmodifier(Extendedmodifier extendedmodifier) {
        this.extendedmodifiers.add(extendedmodifier);
    }

}