





import java.util.List;
import java.util.ArrayList;

public class simplejava_MethodCall extends Statement, GenericExpression {

    private String methodName;
    private boolean thisObject;





    private simplejava_Method simplejava_method;




    private simplejava_Parameter simplejava_parameter;


    public simplejava_MethodCall(
        String methodName,        boolean thisObject    ) {
        super(
        );
        this.methodName = methodName;
        this.thisObject = thisObject;
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

    public simplejava_Method getSimplejava_method() {
        return simplejava_method;
    }

    public void setSimplejava_method(simplejava_Method simplejava_method) {
        this.simplejava_method = simplejava_method;
    }
    public simplejava_Parameter getSimplejava_parameter() {
        return simplejava_parameter;
    }

    public void setSimplejava_parameter(simplejava_Parameter simplejava_parameter) {
        this.simplejava_parameter = simplejava_parameter;
    }

}