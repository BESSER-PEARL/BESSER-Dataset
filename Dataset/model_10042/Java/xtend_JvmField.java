





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmField extends JvmFeature {

    private boolean final;
    private boolean static;





    private xtend_JvmTypeReference xtend_jvmtypereference;


    public xtend_JvmField(
        boolean final,        boolean static    ) {
        super(
        );
        this.final = final;
        this.static = static;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public xtend_JvmTypeReference getXtend_jvmtypereference() {
        return xtend_jvmtypereference;
    }

    public void setXtend_jvmtypereference(xtend_JvmTypeReference xtend_jvmtypereference) {
        this.xtend_jvmtypereference = xtend_jvmtypereference;
    }

}