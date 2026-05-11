





import java.util.List;
import java.util.ArrayList;

public class wiki_Graph  {

    private String name;





    private List<wiki_Edge> wiki_edges;




    private List<wiki_Node> wiki_nodes;


    public wiki_Graph(
        String name    ) {
        this.name = name;
        this.wiki_edges = new ArrayList<>();
        this.wiki_nodes = new ArrayList<>();
    }

    public wiki_Graph(
        String name        ArrayList<wiki_Edge> wiki_edges,        ArrayList<wiki_Node> wiki_nodes    ) {
        this.name = name;
        this.wiki_edges = wiki_edges;
        this.wiki_nodes = wiki_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<wiki_Edge> getWiki_edges() {
        return wiki_edges;
    }

    public void addWiki_edge(Wiki_edge wiki_edge) {
        this.wiki_edges.add(wiki_edge);
    }
    public List<wiki_Node> getWiki_nodes() {
        return wiki_nodes;
    }

    public void addWiki_node(Wiki_node wiki_node) {
        this.wiki_nodes.add(wiki_node);
    }

}