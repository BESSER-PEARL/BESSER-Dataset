





import java.util.List;
import java.util.ArrayList;

public class simplegraph_Graph  {

    private String name;





    private List<simplegraph_Element> simplegraph_elements;




    private simplegraph_Element simplegraph_element;


    public simplegraph_Graph(
        String name    ) {
        this.name = name;
        this.simplegraph_elements = new ArrayList<>();
    }

    public simplegraph_Graph(
        String name        ArrayList<simplegraph_Element> simplegraph_elements    ) {
        this.name = name;
        this.simplegraph_elements = simplegraph_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<simplegraph_Element> getSimplegraph_elements() {
        return simplegraph_elements;
    }

    public void addSimplegraph_element(Simplegraph_element simplegraph_element) {
        this.simplegraph_elements.add(simplegraph_element);
    }
    public simplegraph_Element getSimplegraph_element() {
        return simplegraph_element;
    }

    public void setSimplegraph_element(simplegraph_Element simplegraph_element) {
        this.simplegraph_element = simplegraph_element;
    }

}