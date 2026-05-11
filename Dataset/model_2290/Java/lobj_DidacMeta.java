





import java.util.List;
import java.util.ArrayList;

public class lobj_DidacMeta extends SimpleDidacMeta {

    private String goal;





    private lobj_LuMeta lobj_lumeta;




    private lobj_ModuleMeta lobj_modulemeta;




    private lobj_CourseMeta lobj_coursemeta;


    public lobj_DidacMeta(
        String goal    ) {
        super(
        );
        this.goal = goal;
    }


    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }

    public lobj_LuMeta getLobj_lumeta() {
        return lobj_lumeta;
    }

    public void setLobj_lumeta(lobj_LuMeta lobj_lumeta) {
        this.lobj_lumeta = lobj_lumeta;
    }
    public lobj_ModuleMeta getLobj_modulemeta() {
        return lobj_modulemeta;
    }

    public void setLobj_modulemeta(lobj_ModuleMeta lobj_modulemeta) {
        this.lobj_modulemeta = lobj_modulemeta;
    }
    public lobj_CourseMeta getLobj_coursemeta() {
        return lobj_coursemeta;
    }

    public void setLobj_coursemeta(lobj_CourseMeta lobj_coursemeta) {
        this.lobj_coursemeta = lobj_coursemeta;
    }

}