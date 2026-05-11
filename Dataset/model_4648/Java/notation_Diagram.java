





import java.util.List;
import java.util.ArrayList;

public class notation_Diagram extends View {

    private String name;





    private List<notation_Edge> notation_edges;


    public notation_Diagram(
        String name    ) {
        super(
        );
        this.name = name;
        this.notation_edges = new ArrayList<>();
    }

    public notation_Diagram(
        String name        ArrayList<notation_Edge> notation_edges    ) {
        this.name = name;
        this.notation_edges = notation_edges;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }

}