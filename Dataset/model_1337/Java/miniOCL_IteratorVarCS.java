





import java.util.List;
import java.util.ArrayList;

public class miniOCL_IteratorVarCS  {

    private String itName;





    private miniOCL_LoopExpCS miniocl_loopexpcs;




    private miniOCL_PathNameCS miniocl_pathnamecs;


    public miniOCL_IteratorVarCS(
        String itName    ) {
        this.itName = itName;
    }


    public String getItname() {
        return itName;
    }

    public void setItname(String itName) {
        this.itName = itName;
    }

    public miniOCL_LoopExpCS getMiniocl_loopexpcs() {
        return miniocl_loopexpcs;
    }

    public void setMiniocl_loopexpcs(miniOCL_LoopExpCS miniocl_loopexpcs) {
        this.miniocl_loopexpcs = miniocl_loopexpcs;
    }
    public miniOCL_PathNameCS getMiniocl_pathnamecs() {
        return miniocl_pathnamecs;
    }

    public void setMiniocl_pathnamecs(miniOCL_PathNameCS miniocl_pathnamecs) {
        this.miniocl_pathnamecs = miniocl_pathnamecs;
    }

}