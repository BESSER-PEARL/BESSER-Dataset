





import java.util.List;
import java.util.ArrayList;

public class behaviour_DeclarationStatement extends Statement {

    private String varName;
    private String varType;



    public behaviour_DeclarationStatement(
        String varName,        String varType    ) {
        super(
        );
        this.varName = varName;
        this.varType = varType;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }
    public String getVartype() {
        return varType;
    }

    public void setVartype(String varType) {
        this.varType = varType;
    }


}