





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_Instantiation extends Statement {

    private String VarName;
    private String VarType;



    public behaviouralProgramMM_Instantiation(
        String VarName,        String VarType    ) {
        super(
        );
        this.VarName = VarName;
        this.VarType = VarType;
    }


    public String getVarname() {
        return VarName;
    }

    public void setVarname(String VarName) {
        this.VarName = VarName;
    }
    public String getVartype() {
        return VarType;
    }

    public void setVartype(String VarType) {
        this.VarType = VarType;
    }


}