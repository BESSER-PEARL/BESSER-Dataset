





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_Variable extends Expression {

    private String VarName;



    public behaviouralProgramMM_Variable(
        String VarName    ) {
        super(
        );
        this.VarName = VarName;
    }


    public String getVarname() {
        return VarName;
    }

    public void setVarname(String VarName) {
        this.VarName = VarName;
    }


}