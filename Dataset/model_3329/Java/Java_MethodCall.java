





import java.util.List;
import java.util.ArrayList;

public class Java_MethodCall extends Statement {

    private String methodName;
    private String variableName;



    public Java_MethodCall(
        String methodName,        String variableName    ) {
        super(
        );
        this.methodName = methodName;
        this.variableName = variableName;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }


}