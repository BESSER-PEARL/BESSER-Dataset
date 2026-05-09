





import java.util.List;
import java.util.ArrayList;

public class graph_GModelElement  {

    private String cssClasses;
    private String type;
    private String trace;
    private String id;





    private graph_GModelElement graph_gmodelelement;




    private graph_GEdge graph_gedge;




    private List<graph_GModelElement> graph_gmodelelements;




    private graph_GEdge graph_gedge;


    public graph_GModelElement(
        String cssClasses,        String type,        String trace,        String id    ) {
        this.cssClasses = cssClasses;
        this.type = type;
        this.trace = trace;
        this.id = id;
        this.graph_gmodelelements = new ArrayList<>();
    }

    public graph_GModelElement(
        String cssClasses,        String type,        String trace,        String id        ArrayList<graph_GModelElement> graph_gmodelelements    ) {
        this.cssClasses = cssClasses;
        this.type = type;
        this.trace = trace;
        this.id = id;
        this.graph_gmodelelements = graph_gmodelelements;
    }

    public String getCssclasses() {
        return cssClasses;
    }

    public void setCssclasses(String cssClasses) {
        this.cssClasses = cssClasses;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTrace() {
        return trace;
    }

    public void setTrace(String trace) {
        this.trace = trace;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public graph_GModelElement getGraph_gmodelelement() {
        return graph_gmodelelement;
    }

    public void setGraph_gmodelelement(graph_GModelElement graph_gmodelelement) {
        this.graph_gmodelelement = graph_gmodelelement;
    }
    public graph_GEdge getGraph_gedge() {
        return graph_gedge;
    }

    public void setGraph_gedge(graph_GEdge graph_gedge) {
        this.graph_gedge = graph_gedge;
    }
    public List<graph_GModelElement> getGraph_gmodelelements() {
        return graph_gmodelelements;
    }

    public void addGraph_gmodelelement(Graph_gmodelelement graph_gmodelelement) {
        this.graph_gmodelelements.add(graph_gmodelelement);
    }
    public graph_GEdge getGraph_gedge() {
        return graph_gedge;
    }

    public void setGraph_gedge(graph_GEdge graph_gedge) {
        this.graph_gedge = graph_gedge;
    }

}