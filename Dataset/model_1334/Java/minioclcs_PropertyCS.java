





import java.util.List;
import java.util.ArrayList;

public class minioclcs_PropertyCS extends CSTrace {

    private String name;





    private minioclcs_PathNameCS minioclcs_pathnamecs;




    private minioclcs_MultiplicityCS minioclcs_multiplicitycs;




    private minioclcs_ClassCS minioclcs_classcs;


    public minioclcs_PropertyCS(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public minioclcs_PathNameCS getMinioclcs_pathnamecs() {
        return minioclcs_pathnamecs;
    }

    public void setMinioclcs_pathnamecs(minioclcs_PathNameCS minioclcs_pathnamecs) {
        this.minioclcs_pathnamecs = minioclcs_pathnamecs;
    }
    public minioclcs_MultiplicityCS getMinioclcs_multiplicitycs() {
        return minioclcs_multiplicitycs;
    }

    public void setMinioclcs_multiplicitycs(minioclcs_MultiplicityCS minioclcs_multiplicitycs) {
        this.minioclcs_multiplicitycs = minioclcs_multiplicitycs;
    }
    public minioclcs_ClassCS getMinioclcs_classcs() {
        return minioclcs_classcs;
    }

    public void setMinioclcs_classcs(minioclcs_ClassCS minioclcs_classcs) {
        this.minioclcs_classcs = minioclcs_classcs;
    }

}