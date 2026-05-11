





import java.util.List;
import java.util.ArrayList;

public class operators_ResourceForecast  {






    private List<operators_Marker> operators_markers;


    public operators_ResourceForecast(
    ) {
        this.operators_markers = new ArrayList<>();
    }

    public operators_ResourceForecast(
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