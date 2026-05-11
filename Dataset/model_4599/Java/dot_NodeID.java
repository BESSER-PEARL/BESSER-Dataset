





import java.util.List;
import java.util.ArrayList;

public class dot_NodeID extends Commentable, Connectable, StrictIdentifiable {






    private dot_Port dot_port;




    private dot_NodeStatement dot_nodestatement;


    public dot_NodeID(
    ) {
        super(
        );
    }



    public dot_Port getDot_port() {
        return dot_port;
    }

    public void setDot_port(dot_Port dot_port) {
        this.dot_port = dot_port;
    }
    public dot_NodeStatement getDot_nodestatement() {
        return dot_nodestatement;
    }

    public void setDot_nodestatement(dot_NodeStatement dot_nodestatement) {
        this.dot_nodestatement = dot_nodestatement;
    }

}