





import java.util.List;
import java.util.ArrayList;

public class gv_Target extends Commentable {

    private String operation;





    private gv_Target gv_target;




    private gv_EdgeStatement gv_edgestatement;


    public gv_Target(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public gv_Target getGv_target() {
        return gv_target;
    }

    public void setGv_target(gv_Target gv_target) {
        this.gv_target = gv_target;
    }
    public gv_EdgeStatement getGv_edgestatement() {
        return gv_edgestatement;
    }

    public void setGv_edgestatement(gv_EdgeStatement gv_edgestatement) {
        this.gv_edgestatement = gv_edgestatement;
    }

}