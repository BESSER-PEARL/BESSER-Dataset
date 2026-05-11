





import java.util.List;
import java.util.ArrayList;

public class simplejava_MethodCall extends Statement, GenericExpression {

    private String methodName;
    private boolean thisObject;





    private simplejava_Parameter simplejava_parameter;




    private List<simplejava_GenericExpression> simplejava_genericexpressions;




    private simplejava_Method simplejava_method;


    public simplejava_MethodCall(
        String methodName,        boolean thisObject    ) {
        super(
        );
        this.methodName = methodName;
        this.thisObject = thisObject;
        this.simplejava_genericexpressions = new ArrayList<>();
    }

    public simplejava_MethodCall(
        String methodName,        boolean thisObject        ArrayList<simplejava_GenericExpression> simplejava_genericexpressions    ) {
        this.methodName = methodName;
        this.thisObject = thisObject;
        this.simplejava_genericexpressions = simplejava_genericexpressions;
    }

    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public boolean getThisobject() {
        return thisObject;
    }

    public void setThisobject(boolean thisObject) {
        this.thisObject = thisObject;
    }

    public simplejava_Parameter getSimplejava_parameter() {
        return simplejava_parameter;
    }

    public void setSimplejava_parameter(simplejava_Parameter simplejava_parameter) {
        this.simplejava_parameter = simplejava_parameter;
    }
    public List<simplejava_GenericExpression> getSimplejava_genericexpressions() {
        return simplejava_genericexpressions;
    }

    public void addSimplejava_genericexpression(Simplejava_genericexpression simplejava_genericexpression) {
        this.simplejava_genericexpressions.add(simplejava_genericexpression);
    }
    public simplejava_Method getSimplejava_method() {
        return simplejava_method;
    }

    public void setSimplejava_method(simplejava_Method simplejava_method) {
        this.simplejava_method = simplejava_method;
    }

}