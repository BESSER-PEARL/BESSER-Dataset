





import java.util.List;
import java.util.ArrayList;

public class frontend_core_ClassUse extends core_TypeExpression, core_ImplicitlyAnnotableElement {

    private String className;
    private boolean strictType;





    private RepresentModel representmodel;


    public frontend_core_ClassUse(
        String className,        boolean strictType    ) {
        super(
        );
        this.className = className;
        this.strictType = strictType;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public boolean getStricttype() {
        return strictType;
    }

    public void setStricttype(boolean strictType) {
        this.strictType = strictType;
    }

    public RepresentModel getRepresentmodel() {
        return representmodel;
    }

    public void setRepresentmodel(RepresentModel representmodel) {
        this.representmodel = representmodel;
    }

}