





import java.util.List;
import java.util.ArrayList;

public class miniOCL_OperationCS  {

    private String name;





    private miniOCL_ExpCS miniocl_expcs;




    private miniOCL_PathNameCS miniocl_pathnamecs;




    private List<miniOCL_ParameterCS> miniocl_parametercss;




    private miniOCL_ClassCS miniocl_classcs;


    public miniOCL_OperationCS(
        String name    ) {
        this.name = name;
        this.miniocl_parametercss = new ArrayList<>();
    }

    public miniOCL_OperationCS(
        String name        ArrayList<miniOCL_ParameterCS> miniocl_parametercss    ) {
        this.name = name;
        this.miniocl_parametercss = miniocl_parametercss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public miniOCL_ExpCS getMiniocl_expcs() {
        return miniocl_expcs;
    }

    public void setMiniocl_expcs(miniOCL_ExpCS miniocl_expcs) {
        this.miniocl_expcs = miniocl_expcs;
    }
    public miniOCL_PathNameCS getMiniocl_pathnamecs() {
        return miniocl_pathnamecs;
    }

    public void setMiniocl_pathnamecs(miniOCL_PathNameCS miniocl_pathnamecs) {
        this.miniocl_pathnamecs = miniocl_pathnamecs;
    }
    public List<miniOCL_ParameterCS> getMiniocl_parametercss() {
        return miniocl_parametercss;
    }

    public void addMiniocl_parametercs(Miniocl_parametercs miniocl_parametercs) {
        this.miniocl_parametercss.add(miniocl_parametercs);
    }
    public miniOCL_ClassCS getMiniocl_classcs() {
        return miniocl_classcs;
    }

    public void setMiniocl_classcs(miniOCL_ClassCS miniocl_classcs) {
        this.miniocl_classcs = miniocl_classcs;
    }

}