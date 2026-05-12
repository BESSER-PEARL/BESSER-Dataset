





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmFormalParameter extends JvmIdentifiableElement, JvmAnnotationTarget {

    private String name;





    private xtend_XClosure xtend_xclosure;




    private xtend_JvmTypeReference xtend_jvmtypereference;




    private xtend_XClosure xtend_xclosure;




    private xtend_XForLoopExpression xtend_xforloopexpression;


    public xtend_JvmFormalParameter(
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

    public xtend_XClosure getXtend_xclosure() {
        return xtend_xclosure;
    }

    public void setXtend_xclosure(xtend_XClosure xtend_xclosure) {
        this.xtend_xclosure = xtend_xclosure;
    }
    public xtend_JvmTypeReference getXtend_jvmtypereference() {
        return xtend_jvmtypereference;
    }

    public void setXtend_jvmtypereference(xtend_JvmTypeReference xtend_jvmtypereference) {
        this.xtend_jvmtypereference = xtend_jvmtypereference;
    }
    public xtend_XClosure getXtend_xclosure() {
        return xtend_xclosure;
    }

    public void setXtend_xclosure(xtend_XClosure xtend_xclosure) {
        this.xtend_xclosure = xtend_xclosure;
    }
    public xtend_XForLoopExpression getXtend_xforloopexpression() {
        return xtend_xforloopexpression;
    }

    public void setXtend_xforloopexpression(xtend_XForLoopExpression xtend_xforloopexpression) {
        this.xtend_xforloopexpression = xtend_xforloopexpression;
    }

}