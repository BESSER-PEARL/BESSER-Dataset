





import java.util.List;
import java.util.ArrayList;

public class simplejava_MethodCall extends Statement, GenericExpression {

    private String methodName;
    private boolean thisObject;



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


}