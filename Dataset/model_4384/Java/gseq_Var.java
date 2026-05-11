





import java.util.List;
import java.util.ArrayList;

public class gseq_Var extends IntegerExpression {

    private String varName;



    public gseq_Var(
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