





import java.util.List;
import java.util.ArrayList;

public class minioclcs_IteratorVarCS extends CSTrace {

    private String itName;





    private minioclcs_PathNameCS minioclcs_pathnamecs;


    public minioclcs_IteratorVarCS(
        String itName    ) {
        super(
        );
        this.itName = itName;
    }


    public String getItname() {
        return itName;
    }

    public void setItname(String itName) {
        this.itName = itName;
    }

    public minioclcs_PathNameCS getMinioclcs_pathnamecs() {
        return minioclcs_pathnamecs;
    }

    public void setMinioclcs_pathnamecs(minioclcs_PathNameCS minioclcs_pathnamecs) {
        this.minioclcs_pathnamecs = minioclcs_pathnamecs;
    }

}