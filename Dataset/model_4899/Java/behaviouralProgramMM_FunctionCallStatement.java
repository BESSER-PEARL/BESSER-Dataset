





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_FunctionCallStatement extends Statement {

    private String FuncName;



    public behaviouralProgramMM_FunctionCallStatement(
        String FuncName    ) {
        super(
        );
        this.FuncName = FuncName;
    }


    public String getFuncname() {
        return FuncName;
    }

    public void setFuncname(String FuncName) {
        this.FuncName = FuncName;
    }


}