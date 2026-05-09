





import java.util.List;
import java.util.ArrayList;

public class mydsl_Graph  {

    private String name;





    private List<mydsl_Graph> mydsl_graphs;


    public mydsl_Graph(
        String name    ) {
        this.name = name;
        this.mydsl_graphs = new ArrayList<>();
    }

    public mydsl_Graph(
        String name        ArrayList<mydsl_Graph> mydsl_graphs    ) {
        this.name = name;
        this.mydsl_graphs = mydsl_graphs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mydsl_Graph> getMydsl_graphs() {
        return mydsl_graphs;
    }

    public void addMydsl_graph(Mydsl_graph mydsl_graph) {
        this.mydsl_graphs.add(mydsl_graph);
    }

}