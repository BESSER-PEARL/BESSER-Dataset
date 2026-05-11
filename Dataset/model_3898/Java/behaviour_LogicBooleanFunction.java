





import java.util.List;
import java.util.ArrayList;

public class behaviour_LogicBooleanFunction extends BinaryBooleanFunction {

    private String functionName;



    public behaviour_LogicBooleanFunction(
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