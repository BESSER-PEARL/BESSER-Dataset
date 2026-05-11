





import java.util.List;
import java.util.ArrayList;

public class model_Polyline extends ConnectableElement {

    private boolean polyline;
    private boolean polygon;



    public model_Polyline(
        boolean polyline,        boolean polygon    ) {
        super(
        );
        this.polyline = polyline;
        this.polygon = polygon;
    }


    public boolean getPolyline() {
        return polyline;
    }

    public void setPolyline(boolean polyline) {
        this.polyline = polyline;
    }
    public boolean getPolygon() {
        return polygon;
    }

    public void setPolygon(boolean polygon) {
        this.polygon = polygon;
    }


}