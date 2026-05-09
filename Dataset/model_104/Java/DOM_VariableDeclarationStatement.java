





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclarationStatement extends Statement {






    private List<ExtendedModifier> extendedmodifiers;


    public DOM_VariableDeclarationStatement(
    ) {
        super(
        );
        this.extendedmodifiers = new ArrayList<>();
    }

    public DOM_VariableDeclarationStatement(
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