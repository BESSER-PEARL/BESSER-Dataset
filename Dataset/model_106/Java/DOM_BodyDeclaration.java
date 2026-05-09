





import java.util.List;
import java.util.ArrayList;

public class DOM_BodyDeclaration extends ASTNode {






    private List<ExtendedModifier> extendedmodifiers;




    private Javadoc javadoc;


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


    public List<ExtendedModifier> getExtendedmodifiers() {
        return extendedmodifiers;
    }

    public void addExtendedmodifier(Extendedmodifier extendedmodifier) {
        this.extendedmodifiers.add(extendedmodifier);
    }
    public Javadoc getJavadoc() {
        return javadoc;
    }

    public void setJavadoc(Javadoc javadoc) {
        this.javadoc = javadoc;
    }

}