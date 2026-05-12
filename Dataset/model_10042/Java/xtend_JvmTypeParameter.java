





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmTypeParameter extends JvmConstraintOwner, JvmComponentType {

    private String name;





    private xtend_XtendClass xtend_xtendclass;




    private xtend_XtendInterface xtend_xtendinterface;




    private xtend_XtendExecutable xtend_xtendexecutable;


    public xtend_JvmTypeParameter(
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

    public xtend_XtendClass getXtend_xtendclass() {
        return xtend_xtendclass;
    }

    public void setXtend_xtendclass(xtend_XtendClass xtend_xtendclass) {
        this.xtend_xtendclass = xtend_xtendclass;
    }
    public xtend_XtendInterface getXtend_xtendinterface() {
        return xtend_xtendinterface;
    }

    public void setXtend_xtendinterface(xtend_XtendInterface xtend_xtendinterface) {
        this.xtend_xtendinterface = xtend_xtendinterface;
    }
    public xtend_XtendExecutable getXtend_xtendexecutable() {
        return xtend_xtendexecutable;
    }

    public void setXtend_xtendexecutable(xtend_XtendExecutable xtend_xtendexecutable) {
        this.xtend_xtendexecutable = xtend_xtendexecutable;
    }

}