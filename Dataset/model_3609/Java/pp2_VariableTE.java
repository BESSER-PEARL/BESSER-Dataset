





import java.util.List;
import java.util.ArrayList;

public class pp2_VariableTE extends TextExpression {

    private String varName;



    public pp2_VariableTE(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}