





import java.util.List;
import java.util.ArrayList;

public class miniOCL_ParameterCS  {

    private String name;





    private miniOCL_PathNameCS miniocl_pathnamecs;




    private miniOCL_OperationCS miniocl_operationcs;


    public miniOCL_ParameterCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public miniOCL_PathNameCS getMiniocl_pathnamecs() {
        return miniocl_pathnamecs;
    }

    public void setMiniocl_pathnamecs(miniOCL_PathNameCS miniocl_pathnamecs) {
        this.miniocl_pathnamecs = miniocl_pathnamecs;
    }
    public miniOCL_OperationCS getMiniocl_operationcs() {
        return miniocl_operationcs;
    }

    public void setMiniocl_operationcs(miniOCL_OperationCS miniocl_operationcs) {
        this.miniocl_operationcs = miniocl_operationcs;
    }

}