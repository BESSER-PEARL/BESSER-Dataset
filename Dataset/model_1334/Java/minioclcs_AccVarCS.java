





import java.util.List;
import java.util.ArrayList;

public class minioclcs_AccVarCS extends CSTrace {

    private String accName;





    private minioclcs_ExpCS minioclcs_expcs;




    private minioclcs_PathNameCS minioclcs_pathnamecs;


    public minioclcs_AccVarCS(
        String accName    ) {
        super(
        );
        this.accName = accName;
    }


    public String getAccname() {
        return accName;
    }

    public void setAccname(String accName) {
        this.accName = accName;
    }

    public minioclcs_ExpCS getMinioclcs_expcs() {
        return minioclcs_expcs;
    }

    public void setMinioclcs_expcs(minioclcs_ExpCS minioclcs_expcs) {
        this.minioclcs_expcs = minioclcs_expcs;
    }
    public minioclcs_PathNameCS getMinioclcs_pathnamecs() {
        return minioclcs_pathnamecs;
    }

    public void setMinioclcs_pathnamecs(minioclcs_PathNameCS minioclcs_pathnamecs) {
        this.minioclcs_pathnamecs = minioclcs_pathnamecs;
    }

}