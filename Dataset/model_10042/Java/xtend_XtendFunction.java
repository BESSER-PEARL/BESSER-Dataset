





import java.util.List;
import java.util.ArrayList;

public class xtend_XtendFunction extends XtendExecutable {

    private String name;





    private xtend_JvmTypeReference xtend_jvmtypereference;


    public xtend_XtendFunction(
        String name    ) {
        super(
        );
        this.name = name;
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