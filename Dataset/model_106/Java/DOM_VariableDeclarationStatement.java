





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclarationStatement extends Statement {






    private List<VariableDeclarationFragment> variabledeclarationfragments;




    private Type type;




    private List<ExtendedModifier> extendedmodifiers;


    public DOM_VariableDeclarationStatement(
    ) {
        super(
        );
        this.variabledeclarationfragments = new ArrayList<>();
        this.extendedmodifiers = new ArrayList<>();
    }

    public DOM_VariableDeclarationStatement(
        ArrayList<VariableDeclarationFragment> variabledeclarationfragments,        ArrayList<ExtendedModifier> extendedmodifiers    ) {
        this.variabledeclarationfragments = variabledeclarationfragments;
        this.extendedmodifiers = extendedmodifiers;
    }


    public List<VariableDeclarationFragment> getVariabledeclarationfragments() {
        return variabledeclarationfragments;
    }

    public void addVariabledeclarationfragment(Variabledeclarationfragment variabledeclarationfragment) {
        this.variabledeclarationfragments.add(variabledeclarationfragment);
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