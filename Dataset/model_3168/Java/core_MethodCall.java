





import java.util.List;
import java.util.ArrayList;

public class core_MethodCall extends Expression {

    private boolean withParameters;
    private String methodName;



    public core_MethodCall(
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