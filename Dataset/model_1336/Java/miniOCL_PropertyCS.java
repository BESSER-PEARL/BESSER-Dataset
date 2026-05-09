





import java.util.List;
import java.util.ArrayList;

public class miniOCL_PropertyCS  {

    private String name;





    private miniOCL_PathNameCS miniocl_pathnamecs;




    private miniOCL_ClassCS miniocl_classcs;


    public miniOCL_PropertyCS(
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
    public miniOCL_ClassCS getMiniocl_classcs() {
        return miniocl_classcs;
    }

    public void setMiniocl_classcs(miniOCL_ClassCS miniocl_classcs) {
        this.miniocl_classcs = miniocl_classcs;
    }

}