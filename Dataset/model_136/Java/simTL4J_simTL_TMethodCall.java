





import java.util.List;
import java.util.ArrayList;

public class simTL4J_simTL_TMethodCall  {

    private String params;
    private String methodName;



    public simTL4J_simTL_TMethodCall(
        String params,        String methodName    ) {
        this.params = params;
        this.methodName = methodName;
    }


    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }


}