





import java.util.List;
import java.util.ArrayList;

public class graph_Graph  {

    private String name;





    private List<graph_Element> graph_elements;




    private graph_Element graph_element;


    public graph_Graph(
        String name    ) {
        this.name = name;
        this.graph_elements = new ArrayList<>();
    }

    public graph_Graph(
        String name        ArrayList<graph_Element> graph_elements    ) {
        this.name = name;
        this.graph_elements = graph_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<graph_Element> getGraph_elements() {
        return graph_elements;
    }

    public void addGraph_element(Graph_element graph_element) {
        this.graph_elements.add(graph_element);
    }
    public graph_Element getGraph_element() {
        return graph_element;
    }

    public void setGraph_element(graph_Element graph_element) {
        this.graph_element = graph_element;
    }

}