





import java.util.List;
import java.util.ArrayList;

public class dot_EdgeTarget  {

    private String operator;





    private dot_Node dot_node;




    private dot_EdgeStatement dot_edgestatement;


    public dot_EdgeTarget(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public dot_Node getDot_node() {
        return dot_node;
    }

    public void setDot_node(dot_Node dot_node) {
        this.dot_node = dot_node;
    }
    public dot_EdgeStatement getDot_edgestatement() {
        return dot_edgestatement;
    }

    public void setDot_edgestatement(dot_EdgeStatement dot_edgestatement) {
        this.dot_edgestatement = dot_edgestatement;
    }

}