





import java.util.List;
import java.util.ArrayList;

public class di_View  {

    private String id;
    private String definition;
    private String sourceConnector;
    private String targetConnector;
    private String context;





    private List<di_Node> di_nodes;




    private di_DocumentRoot di_documentroot;


    public di_View(
        String id,        String definition,        String sourceConnector,        String targetConnector,        String context    ) {
        this.id = id;
        this.definition = definition;
        this.sourceConnector = sourceConnector;
        this.targetConnector = targetConnector;
        this.context = context;
        this.di_nodes = new ArrayList<>();
    }

    public di_View(
        String id,        String definition,        String sourceConnector,        String targetConnector,        String context        ArrayList<di_Node> di_nodes    ) {
        this.id = id;
        this.definition = definition;
        this.sourceConnector = sourceConnector;
        this.targetConnector = targetConnector;
        this.context = context;
        this.di_nodes = di_nodes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public String getSourceconnector() {
        return sourceConnector;
    }

    public void setSourceconnector(String sourceConnector) {
        this.sourceConnector = sourceConnector;
    }
    public String getTargetconnector() {
        return targetConnector;
    }

    public void setTargetconnector(String targetConnector) {
        this.targetConnector = targetConnector;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public List<di_Node> getDi_nodes() {
        return di_nodes;
    }

    public void addDi_node(Di_node di_node) {
        this.di_nodes.add(di_node);
    }
    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}