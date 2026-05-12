





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmExecutable extends JvmTypeParameterDeclarator, JvmFeature {

    private boolean varArgs;





    private List<xtend_JvmFormalParameter> xtend_jvmformalparameters;




    private List<xtend_JvmTypeReference> xtend_jvmtypereferences;


    public xtend_JvmExecutable(
        boolean varArgs    ) {
        super(
        );
        this.varArgs = varArgs;
        this.xtend_jvmformalparameters = new ArrayList<>();
        this.xtend_jvmtypereferences = new ArrayList<>();
    }

    public xtend_JvmExecutable(
        boolean varArgs        ArrayList<xtend_JvmFormalParameter> xtend_jvmformalparameters,        ArrayList<xtend_JvmTypeReference> xtend_jvmtypereferences    ) {
        this.varArgs = varArgs;
        this.xtend_jvmformalparameters = xtend_jvmformalparameters;
        this.xtend_jvmtypereferences = xtend_jvmtypereferences;
    }

    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }

    public List<xtend_JvmFormalParameter> getXtend_jvmformalparameters() {
        return xtend_jvmformalparameters;
    }

    public void addXtend_jvmformalparameter(Xtend_jvmformalparameter xtend_jvmformalparameter) {
        this.xtend_jvmformalparameters.add(xtend_jvmformalparameter);
    }
    public List<xtend_JvmTypeReference> getXtend_jvmtypereferences() {
        return xtend_jvmtypereferences;
    }

    public void addXtend_jvmtypereference(Xtend_jvmtypereference xtend_jvmtypereference) {
        this.xtend_jvmtypereferences.add(xtend_jvmtypereference);
    }

}