





import java.util.List;
import java.util.ArrayList;

public class model_Edge  {

    private String type;





    private model_Diagram model_diagram;




    private model_Node model_node;




    private model_Node model_node;


    public model_Edge(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_Diagram getModel_diagram() {
        return model_diagram;
    }

    public void setModel_diagram(model_Diagram model_diagram) {
        this.model_diagram = model_diagram;
    }
    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }
    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }

}