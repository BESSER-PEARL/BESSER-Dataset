





import java.util.List;
import java.util.ArrayList;

public class GraphWiki_Revision  {

    private String date;
    private int text_id;
    private String user;





    private GraphWiki_Node graphwiki_node;




    private GraphWiki_Node graphwiki_node;




    private GraphWiki_Node graphwiki_node;




    private GraphWiki_Wiki graphwiki_wiki;


    public GraphWiki_Revision(
        String date,        int text_id,        String user    ) {
        this.date = date;
        this.text_id = text_id;
        this.user = user;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getText_id() {
        return text_id;
    }

    public void setText_id(int text_id) {
        this.text_id = text_id;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
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
    public GraphWiki_Node getGraphwiki_node() {
        return graphwiki_node;
    }

    public void setGraphwiki_node(GraphWiki_Node graphwiki_node) {
        this.graphwiki_node = graphwiki_node;
    }
    public GraphWiki_Wiki getGraphwiki_wiki() {
        return graphwiki_wiki;
    }

    public void setGraphwiki_wiki(GraphWiki_Wiki graphwiki_wiki) {
        this.graphwiki_wiki = graphwiki_wiki;
    }

}