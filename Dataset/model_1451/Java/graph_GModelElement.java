





import java.util.List;
import java.util.ArrayList;

public class graph_GModelElement  {

    private String id;
    private String trace;
    private String type;
    private String cssClasses;





    private graph_GModelElement graph_gmodelelement;




    private List<graph_GModelElement> graph_gmodelelements;


    public graph_GModelElement(
        String id,        String trace,        String type,        String cssClasses    ) {
        this.id = id;
        this.trace = trace;
        this.type = type;
        this.cssClasses = cssClasses;
        this.graph_gmodelelements = new ArrayList<>();
    }

    public graph_GModelElement(
        String id,        String trace,        String type,        String cssClasses        ArrayList<graph_GModelElement> graph_gmodelelements    ) {
        this.id = id;
        this.trace = trace;
        this.type = type;
        this.cssClasses = cssClasses;
        this.graph_gmodelelements = graph_gmodelelements;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTrace() {
        return trace;
    }

    public void setTrace(String trace) {
        this.trace = trace;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCssclasses() {
        return cssClasses;
    }

    public void setCssclasses(String cssClasses) {
        this.cssClasses = cssClasses;
    }

    public graph_GModelElement getGraph_gmodelelement() {
        return graph_gmodelelement;
    }

    public void setGraph_gmodelelement(graph_GModelElement graph_gmodelelement) {
        this.graph_gmodelelement = graph_gmodelelement;
    }
    public List<graph_GModelElement> getGraph_gmodelelements() {
        return graph_gmodelelements;
    }

    public void addGraph_gmodelelement(Graph_gmodelelement graph_gmodelelement) {
        this.graph_gmodelelements.add(graph_gmodelelement);
    }

}