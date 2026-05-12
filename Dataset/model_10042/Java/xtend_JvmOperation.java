





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmOperation extends JvmExecutable {

    private boolean static;
    private boolean abstract;
    private boolean final;





    private xtend_JvmTypeReference xtend_jvmtypereference;


    public xtend_JvmOperation(
        boolean static,        boolean abstract,        boolean final    ) {
        super(
        );
        this.static = static;
        this.abstract = abstract;
        this.final = final;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public xtend_JvmTypeReference getXtend_jvmtypereference() {
        return xtend_jvmtypereference;
    }

    public void setXtend_jvmtypereference(xtend_JvmTypeReference xtend_jvmtypereference) {
        this.xtend_jvmtypereference = xtend_jvmtypereference;
    }

}