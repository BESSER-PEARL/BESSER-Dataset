





import java.util.List;
import java.util.ArrayList;

public class gv_NodeID extends StrictIdentifiable, Commentable, Connectable {






    private gv_Port gv_port;




    private gv_NodeStatement gv_nodestatement;


    public gv_NodeID(
    ) {
        super(
        );
    }



    public gv_Port getGv_port() {
        return gv_port;
    }

    public void setGv_port(gv_Port gv_port) {
        this.gv_port = gv_port;
    }
    public gv_NodeStatement getGv_nodestatement() {
        return gv_nodestatement;
    }

    public void setGv_nodestatement(gv_NodeStatement gv_nodestatement) {
        this.gv_nodestatement = gv_nodestatement;
    }

}