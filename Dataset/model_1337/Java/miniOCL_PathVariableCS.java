





import java.util.List;
import java.util.ArrayList;

public class miniOCL_PathVariableCS extends PathCS {

    private String varName;



    public miniOCL_PathVariableCS(
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