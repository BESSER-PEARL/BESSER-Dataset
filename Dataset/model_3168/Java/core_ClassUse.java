





import java.util.List;
import java.util.ArrayList;

public class core_ClassUse extends ImplicitlyAnnotableElement, TypeExpression {

    private String className;
    private boolean strictType;





    private core_TypedWithClass core_typedwithclass;


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

    public core_TypedWithClass getCore_typedwithclass() {
        return core_typedwithclass;
    }

    public void setCore_typedwithclass(core_TypedWithClass core_typedwithclass) {
        this.core_typedwithclass = core_typedwithclass;
    }

}