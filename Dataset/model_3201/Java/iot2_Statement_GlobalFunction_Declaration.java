





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_GlobalFunction_Declaration extends Statement {

    private String functionName;
    private String prefix;



    public iot2_Statement_GlobalFunction_Declaration(
        String functionName,        String prefix    ) {
        super(
        );
        this.functionName = functionName;
        this.prefix = prefix;
    }


    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}