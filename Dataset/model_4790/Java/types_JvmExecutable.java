





import java.util.List;
import java.util.ArrayList;

public class types_JvmExecutable extends JvmTypeParameterDeclarator, JvmFeature {

    private boolean varArgs;





    private List<types_JvmTypeReference> types_jvmtypereferences;


    public types_JvmExecutable(
        boolean varArgs    ) {
        super(
        );
        this.varArgs = varArgs;
        this.types_jvmtypereferences = new ArrayList<>();
    }

    public types_JvmExecutable(
        boolean varArgs        ArrayList<types_JvmTypeReference> types_jvmtypereferences    ) {
        this.varArgs = varArgs;
        this.types_jvmtypereferences = types_jvmtypereferences;
    }

    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }

    public List<types_JvmTypeReference> getTypes_jvmtypereferences() {
        return types_jvmtypereferences;
    }

    public void addTypes_jvmtypereference(Types_jvmtypereference types_jvmtypereference) {
        this.types_jvmtypereferences.add(types_jvmtypereference);
    }

}