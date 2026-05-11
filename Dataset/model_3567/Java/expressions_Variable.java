





import java.util.List;
import java.util.ArrayList;

public class expressions_Variable extends AExpression, LExpression {

    private String varName;



    public expressions_Variable(
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