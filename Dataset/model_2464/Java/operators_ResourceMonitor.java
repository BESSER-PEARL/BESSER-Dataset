





import java.util.List;
import java.util.ArrayList;

public class operators_ResourceMonitor  {






    private List<operators_Marker> operators_markers;


    public operators_ResourceMonitor(
    ) {
        this.operators_markers = new ArrayList<>();
    }

    public operators_ResourceMonitor(
        ArrayList<operators_Marker> operators_markers    ) {
        this.operators_markers = operators_markers;
    }


    public List<operators_Marker> getOperators_markers() {
        return operators_markers;
    }

    public void addOperators_marker(Operators_marker operators_marker) {
        this.operators_markers.add(operators_marker);
    }

}