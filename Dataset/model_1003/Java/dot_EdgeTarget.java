





import java.util.List;
import java.util.ArrayList;

public class dot_EdgeTarget  {

    private String operator;





    private dot_EdgeStatement dot_edgestatement;




    private dot_Subgraph dot_subgraph;




    private dot_Node dot_node;


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

    public dot_EdgeStatement getDot_edgestatement() {
        return dot_edgestatement;
    }

    public void setDot_edgestatement(dot_EdgeStatement dot_edgestatement) {
        this.dot_edgestatement = dot_edgestatement;
    }
    public dot_Subgraph getDot_subgraph() {
        return dot_subgraph;
    }

    public void setDot_subgraph(dot_Subgraph dot_subgraph) {
        this.dot_subgraph = dot_subgraph;
    }
    public dot_Node getDot_node() {
        return dot_node;
    }

    public void setDot_node(dot_Node dot_node) {
        this.dot_node = dot_node;
    }

}