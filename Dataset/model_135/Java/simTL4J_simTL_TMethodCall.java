





import java.util.List;
import java.util.ArrayList;

public class simTL4J_simTL_TMethodCall  {

    private String methodName;
    private String params;



    public simTL4J_simTL_TMethodCall(
        String methodName,        String params    ) {
        this.methodName = methodName;
        this.params = params;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }


}