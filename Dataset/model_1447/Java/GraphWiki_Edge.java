





import java.util.List;
import java.util.ArrayList;

public class GraphWiki_Edge  {

    private String type;





    private GraphWiki_Wiki graphwiki_wiki;




    private GraphWiki_Node graphwiki_node;




    private GraphWiki_Node graphwiki_node;


    public GraphWiki_Edge(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public GraphWiki_Wiki getGraphwiki_wiki() {
        return graphwiki_wiki;
    }

    public void setGraphwiki_wiki(GraphWiki_Wiki graphwiki_wiki) {
        this.graphwiki_wiki = graphwiki_wiki;
    }
    public GraphWiki_Node getGraphwiki_node() {
        return graphwiki_node;
    }

    public void setGraphwiki_node(GraphWiki_Node graphwiki_node) {
        this.graphwiki_node = graphwiki_node;
    }
    public GraphWiki_Node getGraphwiki_node() {
        return graphwiki_node;
    }

    public void setGraphwiki_node(GraphWiki_Node graphwiki_node) {
        this.graphwiki_node = graphwiki_node;
    }

}