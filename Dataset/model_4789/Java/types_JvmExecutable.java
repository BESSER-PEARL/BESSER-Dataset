





import java.util.List;
import java.util.ArrayList;

public class types_JvmExecutable extends JvmFeature, JvmTypeParameterDeclarator {

    private boolean varArgs;



    public types_JvmExecutable(
        boolean varArgs    ) {
        super(
        );
        this.varArgs = varArgs;
    }


    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }


}