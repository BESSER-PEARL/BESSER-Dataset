





import java.util.List;
import java.util.ArrayList;

public class behaviour_OccupationBooleanFunction extends BinaryBooleanFunction {

    private String functionName;



    public behaviour_OccupationBooleanFunction(
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