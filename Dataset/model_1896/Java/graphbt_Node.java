





import java.util.List;
import java.util.ArrayList;

public class graphbt_Node  {

    private int index;
    private String id;





    private graphbt_Link graphbt_link;




    private graphbt_Link graphbt_link;




    private graphbt_Edge graphbt_edge;




    private graphbt_SpecialEdge graphbt_specialedge;




    private graphbt_Edge graphbt_edge;


    public graphbt_Node(
        int index,        String id    ) {
        this.index = index;
        this.id = id;
    }


    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public graphbt_Link getGraphbt_link() {
        return graphbt_link;
    }

    public void setGraphbt_link(graphbt_Link graphbt_link) {
        this.graphbt_link = graphbt_link;
    }
    public graphbt_Link getGraphbt_link() {
        return graphbt_link;
    }

    public void setGraphbt_link(graphbt_Link graphbt_link) {
        this.graphbt_link = graphbt_link;
    }
    public graphbt_Edge getGraphbt_edge() {
        return graphbt_edge;
    }

    public void setGraphbt_edge(graphbt_Edge graphbt_edge) {
        this.graphbt_edge = graphbt_edge;
    }
    public graphbt_SpecialEdge getGraphbt_specialedge() {
        return graphbt_specialedge;
    }

    public void setGraphbt_specialedge(graphbt_SpecialEdge graphbt_specialedge) {
        this.graphbt_specialedge = graphbt_specialedge;
    }
    public graphbt_Edge getGraphbt_edge() {
        return graphbt_edge;
    }

    public void setGraphbt_edge(graphbt_Edge graphbt_edge) {
        this.graphbt_edge = graphbt_edge;
    }

}