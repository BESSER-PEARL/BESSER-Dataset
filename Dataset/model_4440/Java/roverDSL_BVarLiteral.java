





import java.util.List;
import java.util.ArrayList;

public class roverDSL_BVarLiteral extends ValueExpression {

    private String var;



    public roverDSL_BVarLiteral(
        String var    ) {
        super(
        );
        this.var = var;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }


}