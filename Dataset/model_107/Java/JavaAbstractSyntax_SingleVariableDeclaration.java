





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_SingleVariableDeclaration extends VariableDeclaration {

    private String varargs;





    private List<ExtendedModifier> extendedmodifiers;




    private Type type;


    public JavaAbstractSyntax_SingleVariableDeclaration(
        String varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.extendedmodifiers = new ArrayList<>();
    }

    public JavaAbstractSyntax_SingleVariableDeclaration(
        String varargs        ArrayList<ExtendedModifier> extendedmodifiers    ) {
        this.varargs = varargs;
        this.extendedmodifiers = extendedmodifiers;
    }

    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
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