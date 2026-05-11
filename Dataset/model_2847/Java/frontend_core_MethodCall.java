





import java.util.List;
import java.util.ArrayList;

public class frontend_core_MethodCall extends Expression {

    private String methodName;
    private boolean withParameters;



    public frontend_core_MethodCall(
        String methodName,        boolean withParameters    ) {
        super(
        );
        this.methodName = methodName;
        this.withParameters = withParameters;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public boolean getWithparameters() {
        return withParameters;
    }

    public void setWithparameters(boolean withParameters) {
        this.withParameters = withParameters;
    }


}