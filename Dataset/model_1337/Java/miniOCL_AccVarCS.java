





import java.util.List;
import java.util.ArrayList;

public class miniOCL_AccVarCS  {

    private String accVarName;





    private miniOCL_ExistsExpCS miniocl_existsexpcs;




    private miniOCL_ExpCS miniocl_expcs;




    private miniOCL_IterateExpCS miniocl_iterateexpcs;




    private miniOCL_PathNameCS miniocl_pathnamecs;




    private miniOCL_ForAllExpCS miniocl_forallexpcs;


    public miniOCL_AccVarCS(
        String accVarName    ) {
        this.accVarName = accVarName;
    }


    public String getAccvarname() {
        return accVarName;
    }

    public void setAccvarname(String accVarName) {
        this.accVarName = accVarName;
    }

    public miniOCL_ExistsExpCS getMiniocl_existsexpcs() {
        return miniocl_existsexpcs;
    }

    public void setMiniocl_existsexpcs(miniOCL_ExistsExpCS miniocl_existsexpcs) {
        this.miniocl_existsexpcs = miniocl_existsexpcs;
    }
    public miniOCL_ExpCS getMiniocl_expcs() {
        return miniocl_expcs;
    }

    public void setMiniocl_expcs(miniOCL_ExpCS miniocl_expcs) {
        this.miniocl_expcs = miniocl_expcs;
    }
    public miniOCL_IterateExpCS getMiniocl_iterateexpcs() {
        return miniocl_iterateexpcs;
    }

    public void setMiniocl_iterateexpcs(miniOCL_IterateExpCS miniocl_iterateexpcs) {
        this.miniocl_iterateexpcs = miniocl_iterateexpcs;
    }
    public miniOCL_PathNameCS getMiniocl_pathnamecs() {
        return miniocl_pathnamecs;
    }

    public void setMiniocl_pathnamecs(miniOCL_PathNameCS miniocl_pathnamecs) {
        this.miniocl_pathnamecs = miniocl_pathnamecs;
    }
    public miniOCL_ForAllExpCS getMiniocl_forallexpcs() {
        return miniocl_forallexpcs;
    }

    public void setMiniocl_forallexpcs(miniOCL_ForAllExpCS miniocl_forallexpcs) {
        this.miniocl_forallexpcs = miniocl_forallexpcs;
    }

}