





import java.util.List;
import java.util.ArrayList;

public class minioclcs_OperationCS extends CSTrace {

    private String name;





    private minioclcs_ClassCS minioclcs_classcs;




    private List<minioclcs_ParameterCS> minioclcs_parametercss;




    private minioclcs_PathNameCS minioclcs_pathnamecs;




    private minioclcs_ExpCS minioclcs_expcs;


    public minioclcs_OperationCS(
        String name    ) {
        super(
        );
        this.name = name;
        this.minioclcs_parametercss = new ArrayList<>();
    }

    public minioclcs_OperationCS(
        String name        ArrayList<minioclcs_ParameterCS> minioclcs_parametercss    ) {
        this.name = name;
        this.minioclcs_parametercss = minioclcs_parametercss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public minioclcs_ClassCS getMinioclcs_classcs() {
        return minioclcs_classcs;
    }

    public void setMinioclcs_classcs(minioclcs_ClassCS minioclcs_classcs) {
        this.minioclcs_classcs = minioclcs_classcs;
    }
    public List<minioclcs_ParameterCS> getMinioclcs_parametercss() {
        return minioclcs_parametercss;
    }

    public void addMinioclcs_parametercs(Minioclcs_parametercs minioclcs_parametercs) {
        this.minioclcs_parametercss.add(minioclcs_parametercs);
    }
    public minioclcs_PathNameCS getMinioclcs_pathnamecs() {
        return minioclcs_pathnamecs;
    }

    public void setMinioclcs_pathnamecs(minioclcs_PathNameCS minioclcs_pathnamecs) {
        this.minioclcs_pathnamecs = minioclcs_pathnamecs;
    }
    public minioclcs_ExpCS getMinioclcs_expcs() {
        return minioclcs_expcs;
    }

    public void setMinioclcs_expcs(minioclcs_ExpCS minioclcs_expcs) {
        this.minioclcs_expcs = minioclcs_expcs;
    }

}