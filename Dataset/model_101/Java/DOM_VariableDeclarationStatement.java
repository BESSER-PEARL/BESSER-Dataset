





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclarationStatement extends Statement {






    private List<ExtendedModifier> extendedmodifiers;




    private Type type;




    private List<VariableDeclarationFragment> variabledeclarationfragments;


    public DOM_VariableDeclarationStatement(
    ) {
        super(
        );
        this.extendedmodifiers = new ArrayList<>();
        this.variabledeclarationfragments = new ArrayList<>();
    }

    public DOM_VariableDeclarationStatement(
        ArrayList<ExtendedModifier> extendedmodifiers,        ArrayList<VariableDeclarationFragment> variabledeclarationfragments    ) {
        this.extendedmodifiers = extendedmodifiers;
        this.variabledeclarationfragments = variabledeclarationfragments;
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
    public List<VariableDeclarationFragment> getVariabledeclarationfragments() {
        return variabledeclarationfragments;
    }

    public void addVariabledeclarationfragment(Variabledeclarationfragment variabledeclarationfragment) {
        this.variabledeclarationfragments.add(variabledeclarationfragment);
    }

}