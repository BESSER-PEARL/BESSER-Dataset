





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_VariableDeclarationExpression extends Expression {






    private List<ExtendedModifier> extendedmodifiers;


    public JavaAbstractSyntax_VariableDeclarationExpression(
    ) {
        super(
        );
        this.extendedmodifiers = new ArrayList<>();
    }

    public JavaAbstractSyntax_VariableDeclarationExpression(
        ArrayList<ExtendedModifier> extendedmodifiers    ) {
        this.extendedmodifiers = extendedmodifiers;
    }


    public List<ExtendedModifier> getExtendedmodifiers() {
        return extendedmodifiers;
    }

    public void addExtendedmodifier(Extendedmodifier extendedmodifier) {
        this.extendedmodifiers.add(extendedmodifier);
    }

}