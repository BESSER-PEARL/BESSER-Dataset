





import java.util.List;
import java.util.ArrayList;

public class wiki_Node  {

    private String title;
    private int node_namespace;
    private int node_id;
    private String type;
    private int visits;
    private int editions;





    private wiki_Wiki wiki_wiki;


    public wiki_Node(
        String title,        int node_namespace,        int node_id,        String type,        int visits,        int editions    ) {
        this.title = title;
        this.node_namespace = node_namespace;
        this.node_id = node_id;
        this.type = type;
        this.visits = visits;
        this.editions = editions;
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
    public int getNode_id() {
        return node_id;
    }

    public void setNode_id(int node_id) {
        this.node_id = node_id;
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
    public int getEditions() {
        return editions;
    }

    public void setEditions(int editions) {
        this.editions = editions;
    }

    public wiki_Wiki getWiki_wiki() {
        return wiki_wiki;
    }

    public void setWiki_wiki(wiki_Wiki wiki_wiki) {
        this.wiki_wiki = wiki_wiki;
    }

}