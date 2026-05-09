





import java.util.List;
import java.util.ArrayList;

public class miniOCL_NavigationPathVariableCS extends NavigationPathCS {

    private String varName;



    public miniOCL_NavigationPathVariableCS(
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