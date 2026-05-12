





import java.util.List;
import java.util.ArrayList;

public class xtend_XVariableDeclaration extends JvmIdentifiableElement, XExpression {

    private boolean writeable;
    private String name;





    private xtend_JvmTypeReference xtend_jvmtypereference;


    public xtend_XVariableDeclaration(
        boolean writeable,        String name    ) {
        super(
        );
        this.writeable = writeable;
        this.name = name;
    }


    public boolean getWriteable() {
        return writeable;
    }

    public void setWriteable(boolean writeable) {
        this.writeable = writeable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xtend_JvmTypeReference getXtend_jvmtypereference() {
        return xtend_jvmtypereference;
    }

    public void setXtend_jvmtypereference(xtend_JvmTypeReference xtend_jvmtypereference) {
        this.xtend_jvmtypereference = xtend_jvmtypereference;
    }

}