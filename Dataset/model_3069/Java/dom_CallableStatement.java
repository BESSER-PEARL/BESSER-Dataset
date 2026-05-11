





import java.util.List;
import java.util.ArrayList;

public class dom_CallableStatement extends QlStatement {

    private boolean functionCall;
    private String name;



    public dom_CallableStatement(
        boolean functionCall,        String name    ) {
        super(
        );
        this.functionCall = functionCall;
        this.name = name;
    }


    public boolean getFunctioncall() {
        return functionCall;
    }

    public void setFunctioncall(boolean functionCall) {
        this.functionCall = functionCall;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}