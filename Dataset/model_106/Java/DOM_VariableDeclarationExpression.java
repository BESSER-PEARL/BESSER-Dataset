





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclarationExpression extends Expression {






    private List<ExtendedModifier> extendedmodifiers;




    private Type type;


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


    public List<ExtendedModifier> getExtendedmodifiers() {
        return extendedmodifiers;
    }

    public void addExtendedmodifier(Extendedmodifier extendedmodifier) {
        this.extendedmodifiers.add(extendedmodifier);
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}