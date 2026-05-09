





import java.util.List;
import java.util.ArrayList;

public class mydsl_Node  {

    private String content;
    private String name;
    private boolean isInvisible;





    private mydsl_Graph mydsl_graph;




    private mydsl_Edge mydsl_edge;




    private mydsl_Edge mydsl_edge;


    public mydsl_Node(
        String content,        String name,        boolean isInvisible    ) {
        this.content = content;
        this.name = name;
        this.isInvisible = isInvisible;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsinvisible() {
        return isInvisible;
    }

    public void setIsinvisible(boolean isInvisible) {
        this.isInvisible = isInvisible;
    }

    public mydsl_Graph getMydsl_graph() {
        return mydsl_graph;
    }

    public void setMydsl_graph(mydsl_Graph mydsl_graph) {
        this.mydsl_graph = mydsl_graph;
    }
    public mydsl_Edge getMydsl_edge() {
        return mydsl_edge;
    }

    public void setMydsl_edge(mydsl_Edge mydsl_edge) {
        this.mydsl_edge = mydsl_edge;
    }
    public mydsl_Edge getMydsl_edge() {
        return mydsl_edge;
    }

    public void setMydsl_edge(mydsl_Edge mydsl_edge) {
        this.mydsl_edge = mydsl_edge;
    }

}