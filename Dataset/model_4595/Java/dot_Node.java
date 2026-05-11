





import java.util.List;
import java.util.ArrayList;

public class dot_Node  {

    private String name;





    private dot_DirectedEdge dot_directededge;




    private dot_UnDirectedEdge dot_undirectededge;




    private dot_DirectedEdge dot_directededge;




    private dot_UnDirectedEdge dot_undirectededge;


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

    public dot_DirectedEdge getDot_directededge() {
        return dot_directededge;
    }

    public void setDot_directededge(dot_DirectedEdge dot_directededge) {
        this.dot_directededge = dot_directededge;
    }
    public dot_UnDirectedEdge getDot_undirectededge() {
        return dot_undirectededge;
    }

    public void setDot_undirectededge(dot_UnDirectedEdge dot_undirectededge) {
        this.dot_undirectededge = dot_undirectededge;
    }
    public dot_DirectedEdge getDot_directededge() {
        return dot_directededge;
    }

    public void setDot_directededge(dot_DirectedEdge dot_directededge) {
        this.dot_directededge = dot_directededge;
    }
    public dot_UnDirectedEdge getDot_undirectededge() {
        return dot_undirectededge;
    }

    public void setDot_undirectededge(dot_UnDirectedEdge dot_undirectededge) {
        this.dot_undirectededge = dot_undirectededge;
    }

}