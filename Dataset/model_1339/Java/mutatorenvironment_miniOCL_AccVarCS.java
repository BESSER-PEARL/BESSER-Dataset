





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_miniOCL_AccVarCS  {

    private None accVarName;





    private PathNameCS pathnamecs;




    private ExpCS expcs;


    public mutatorenvironment_miniOCL_AccVarCS(
        None accVarName    ) {
        this.accVarName = accVarName;
    }


    public None getAccvarname() {
        return accVarName;
    }

    public void setAccvarname(None accVarName) {
        this.accVarName = accVarName;
    }

    public PathNameCS getPathnamecs() {
        return pathnamecs;
    }

    public void setPathnamecs(PathNameCS pathnamecs) {
        this.pathnamecs = pathnamecs;
    }
    public ExpCS getExpcs() {
        return expcs;
    }

    public void setExpcs(ExpCS expcs) {
        this.expcs = expcs;
    }

}