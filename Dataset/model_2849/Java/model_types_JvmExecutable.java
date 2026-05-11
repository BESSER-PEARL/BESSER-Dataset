





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmExecutable extends types_JvmFeature, types_JvmTypeParameterDeclarator {

    private boolean varArgs;



    public model_types_JvmExecutable(
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