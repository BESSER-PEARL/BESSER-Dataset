





import java.util.List;
import java.util.ArrayList;

public class frontend_core_MethodCall extends Expression {

    private boolean withParameters;
    private String methodName;



    public frontend_core_MethodCall(
        boolean withParameters,        String methodName    ) {
        super(
        );
        this.withParameters = withParameters;
        this.methodName = methodName;
    }


    public boolean getWithparameters() {
        return withParameters;
    }

    public void setWithparameters(boolean withParameters) {
        this.withParameters = withParameters;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }


}