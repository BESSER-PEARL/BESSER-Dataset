





import java.util.List;
import java.util.ArrayList;

public class DOM_SingleVariableDeclaration extends VariableDeclaration {

    private String varargs;





    private List<ExtendedModifier> extendedmodifiers;


    public DOM_SingleVariableDeclaration(
        String varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.extendedmodifiers = new ArrayList<>();
    }

    public DOM_SingleVariableDeclaration(
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

}