





import java.util.List;
import java.util.ArrayList;

public class pp_InterpolatedVariable extends Expression {

    private String varName;



    public pp_InterpolatedVariable(
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