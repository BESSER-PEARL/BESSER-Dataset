





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Polyline extends Shape {






    private List<gmfgraph_Point> gmfgraph_points;


    public gmfgraph_Polyline(
    ) {
        super(
        );
        this.gmfgraph_points = new ArrayList<>();
    }

    public gmfgraph_Polyline(
        ArrayList<gmfgraph_Point> gmfgraph_points    ) {
        this.gmfgraph_points = gmfgraph_points;
    }


    public List<gmfgraph_Point> getGmfgraph_points() {
        return gmfgraph_points;
    }

    public void addGmfgraph_point(Gmfgraph_point gmfgraph_point) {
        this.gmfgraph_points.add(gmfgraph_point);
    }

}