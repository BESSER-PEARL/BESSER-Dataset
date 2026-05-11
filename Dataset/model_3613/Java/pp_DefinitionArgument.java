





import java.util.List;
import java.util.ArrayList;

public class pp_DefinitionArgument  {

    private String op;
    private String argName;





    private pp_Expression pp_expression;


    public pp_DefinitionArgument(
        String op,        String argName    ) {
        this.op = op;
        this.argName = argName;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getArgname() {
        return argName;
    }

    public void setArgname(String argName) {
        this.argName = argName;
    }

    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }

}