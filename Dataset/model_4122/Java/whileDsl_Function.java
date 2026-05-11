





import java.util.List;
import java.util.ArrayList;

public class whileDsl_Function  {

    private String functionName;





    private whileDsl_Model whiledsl_model;


    public whileDsl_Function(
        String functionName    ) {
        this.functionName = functionName;
    }


    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }

    public whileDsl_Model getWhiledsl_model() {
        return whiledsl_model;
    }

    public void setWhiledsl_model(whileDsl_Model whiledsl_model) {
        this.whiledsl_model = whiledsl_model;
    }

}