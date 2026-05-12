





import java.util.List;
import java.util.ArrayList;

public class xtend_XtendParameter extends XtendAnnotationTarget {

    private boolean varArg;
    private String name;
    private boolean extension;





    private xtend_JvmTypeReference xtend_jvmtypereference;




    private xtend_XtendExecutable xtend_xtendexecutable;


    public xtend_XtendParameter(
        boolean varArg,        String name,        boolean extension    ) {
        super(
        );
        this.varArg = varArg;
        this.name = name;
        this.extension = extension;
    }


    public boolean getVararg() {
        return varArg;
    }

    public void setVararg(boolean varArg) {
        this.varArg = varArg;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }

    public xtend_JvmTypeReference getXtend_jvmtypereference() {
        return xtend_jvmtypereference;
    }

    public void setXtend_jvmtypereference(xtend_JvmTypeReference xtend_jvmtypereference) {
        this.xtend_jvmtypereference = xtend_jvmtypereference;
    }
    public xtend_XtendExecutable getXtend_xtendexecutable() {
        return xtend_xtendexecutable;
    }

    public void setXtend_xtendexecutable(xtend_XtendExecutable xtend_xtendexecutable) {
        this.xtend_xtendexecutable = xtend_xtendexecutable;
    }

}