





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendParameter extends XtendAnnotationTarget {

    private boolean varArg;
    private String name;
    private boolean extension;





    private JvmTypeReference jvmtypereference;


    public model_ss_XtendParameter(
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

    public JvmTypeReference getJvmtypereference() {
        return jvmtypereference;
    }

    public void setJvmtypereference(JvmTypeReference jvmtypereference) {
        this.jvmtypereference = jvmtypereference;
    }

}