





import java.util.List;
import java.util.ArrayList;

public class types_Parameter extends NamedElement, TypedElement, AnnotatableElement {

    private boolean optional;
    private boolean varArgs;



    public types_Parameter(
        boolean optional,        boolean varArgs    ) {
        super(
        );
        this.optional = optional;
        this.varArgs = varArgs;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }


}