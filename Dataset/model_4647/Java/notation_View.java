





import java.util.List;
import java.util.ArrayList;

public class notation_View extends NotationElement {

    private String viewDetails;
    private String viewType;





    private notation_EObject notation_eobject;




    private List<notation_Node> notation_nodes;


    public notation_View(
        String viewDetails,        String viewType    ) {
        super(
        );
        this.viewDetails = viewDetails;
        this.viewType = viewType;
        this.notation_nodes = new ArrayList<>();
    }

    public notation_View(
        String viewDetails,        String viewType        ArrayList<notation_Node> notation_nodes    ) {
        this.viewDetails = viewDetails;
        this.viewType = viewType;
        this.notation_nodes = notation_nodes;
    }

    public String getViewdetails() {
        return viewDetails;
    }

    public void setViewdetails(String viewDetails) {
        this.viewDetails = viewDetails;
    }
    public String getViewtype() {
        return viewType;
    }

    public void setViewtype(String viewType) {
        this.viewType = viewType;
    }

    public notation_EObject getNotation_eobject() {
        return notation_eobject;
    }

    public void setNotation_eobject(notation_EObject notation_eobject) {
        this.notation_eobject = notation_eobject;
    }
    public List<notation_Node> getNotation_nodes() {
        return notation_nodes;
    }

    public void addNotation_node(Notation_node notation_node) {
        this.notation_nodes.add(notation_node);
    }

}