





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Subhypotheses  {

    private String relationOp;





    private jpdl31_Hyphotesis jpdl31_hyphotesis;


    public jpdl31_Subhypotheses(
        String relationOp    ) {
        this.relationOp = relationOp;
    }


    public String getRelationop() {
        return relationOp;
    }

    public void setRelationop(String relationOp) {
        this.relationOp = relationOp;
    }

    public jpdl31_Hyphotesis getJpdl31_hyphotesis() {
        return jpdl31_hyphotesis;
    }

    public void setJpdl31_hyphotesis(jpdl31_Hyphotesis jpdl31_hyphotesis) {
        this.jpdl31_hyphotesis = jpdl31_hyphotesis;
    }

}