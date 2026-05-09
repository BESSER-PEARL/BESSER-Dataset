





import java.util.List;
import java.util.ArrayList;

public class GraphWiki_Node  {

    private String title;
    private int node_namespace;
    private int editions;
    private String type;
    private int visits;
    private int node_id;





    private GraphWiki_Wiki graphwiki_wiki;


    public GraphWiki_Node(
        String title,        int node_namespace,        int editions,        String type,        int visits,        int node_id    ) {
        this.title = title;
        this.node_namespace = node_namespace;
        this.editions = editions;
        this.type = type;
        this.visits = visits;
        this.node_id = node_id;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getNode_namespace() {
        return node_namespace;
    }

    public void setNode_namespace(int node_namespace) {
        this.node_namespace = node_namespace;
    }
    public int getEditions() {
        return editions;
    }

    public void setEditions(int editions) {
        this.editions = editions;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getVisits() {
        return visits;
    }

    public void setVisits(int visits) {
        this.visits = visits;
    }
    public int getNode_id() {
        return node_id;
    }

    public void setNode_id(int node_id) {
        this.node_id = node_id;
    }

    public GraphWiki_Wiki getGraphwiki_wiki() {
        return graphwiki_wiki;
    }

    public void setGraphwiki_wiki(GraphWiki_Wiki graphwiki_wiki) {
        this.graphwiki_wiki = graphwiki_wiki;
    }

}