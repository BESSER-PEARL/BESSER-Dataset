





import java.util.List;
import java.util.ArrayList;

public class frontend_core_ClassUse extends core_TypeExpression, core_ImplicitlyAnnotableElement {

    private boolean strictType;
    private String className;



    public frontend_core_ClassUse(
        boolean strictType,        String className    ) {
        super(
        );
        this.strictType = strictType;
        this.className = className;
    }


    public boolean getStricttype() {
        return strictType;
    }

    public void setStricttype(boolean strictType) {
        this.strictType = strictType;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }


}