





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Statement_GlobalFunction_Declaration extends Statement {

    private String prefix;
    private String functionName;



    public activityecorelua_Statement_GlobalFunction_Declaration(
        String prefix,        String functionName    ) {
        super(
        );
        this.prefix = prefix;
        this.functionName = functionName;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }


}