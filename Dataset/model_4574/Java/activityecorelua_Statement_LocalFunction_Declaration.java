





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Statement_LocalFunction_Declaration extends Statement {

    private String functionName;



    public activityecorelua_Statement_LocalFunction_Declaration(
        String functionName    ) {
        super(
        );
        this.functionName = functionName;
    }


    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }


}