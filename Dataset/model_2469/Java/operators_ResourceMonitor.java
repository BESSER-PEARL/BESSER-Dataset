





import java.util.List;
import java.util.ArrayList;

public class operators_ResourceMonitor extends Base {






    private operators_Node operators_node;




    private List<operators_Marker> operators_markers;


    public operators_ResourceMonitor(
    ) {
        super(
        );
        this.operators_markers = new ArrayList<>();
    }

    public operators_ResourceMonitor(
        ArrayList<operators_Marker> operators_markers    ) {
        this.operators_markers = operators_markers;
    }


    public operators_Node getOperators_node() {
        return operators_node;
    }

    public void setOperators_node(operators_Node operators_node) {
        this.operators_node = operators_node;
    }
    public List<operators_Marker> getOperators_markers() {
        return operators_markers;
    }

    public void addOperators_marker(Operators_marker operators_marker) {
        this.operators_markers.add(operators_marker);
    }

}