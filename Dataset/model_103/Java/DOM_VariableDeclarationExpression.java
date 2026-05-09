





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclarationExpression extends Expression {






    private Type type;




    private List<ExtendedModifier> extendedmodifiers;


    public DOM_VariableDeclarationExpression(
    ) {
        super(
        );
        this.extendedmodifiers = new ArrayList<>();
    }

    public DOM_VariableDeclarationExpression(
        ArrayList<ExtendedModifier> extendedmodifiers    ) {
        this.extendedmodifiers = extendedmodifiers;
    }


    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public List<ExtendedModifier> getExtendedmodifiers() {
        return extendedmodifiers;
    }

    public void addExtendedmodifier(Extendedmodifier extendedmodifier) {
        this.extendedmodifiers.add(extendedmodifier);
    }

}