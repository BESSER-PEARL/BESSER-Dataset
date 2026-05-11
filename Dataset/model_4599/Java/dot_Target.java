





import java.util.List;
import java.util.ArrayList;

public class dot_Target extends Commentable {

    private String operation;





    private dot_Target dot_target;




    private dot_EdgeStatement dot_edgestatement;


    public dot_Target(
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

    public dot_Target getDot_target() {
        return dot_target;
    }

    public void setDot_target(dot_Target dot_target) {
        this.dot_target = dot_target;
    }
    public dot_EdgeStatement getDot_edgestatement() {
        return dot_edgestatement;
    }

    public void setDot_edgestatement(dot_EdgeStatement dot_edgestatement) {
        this.dot_edgestatement = dot_edgestatement;
    }

}