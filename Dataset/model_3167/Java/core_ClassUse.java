





import java.util.List;
import java.util.ArrayList;

public class core_ClassUse extends ImplicitlyAnnotableElement, TypeExpression {

    private String className;
    private boolean strictType;





    private core_RepresentModel core_representmodel;


    public core_ClassUse(
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

    public core_RepresentModel getCore_representmodel() {
        return core_representmodel;
    }

    public void setCore_representmodel(core_RepresentModel core_representmodel) {
        this.core_representmodel = core_representmodel;
    }

}