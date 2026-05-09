





import java.util.List;
import java.util.ArrayList;

public class dot_Node  {

    private String name;





    private dot_EdgeStatement dot_edgestatement;




    private dot_NodeStatement dot_nodestatement;


    public dot_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dot_EdgeStatement getDot_edgestatement() {
        return dot_edgestatement;
    }

    public void setDot_edgestatement(dot_EdgeStatement dot_edgestatement) {
        this.dot_edgestatement = dot_edgestatement;
    }
    public dot_NodeStatement getDot_nodestatement() {
        return dot_nodestatement;
    }

    public void setDot_nodestatement(dot_NodeStatement dot_nodestatement) {
        this.dot_nodestatement = dot_nodestatement;
    }

}