





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_Polyline extends Shape {






    private List<Point> points;


    public gmf_all_gmfgraph_Polyline(
    ) {
        super(
        );
        this.points = new ArrayList<>();
    }

    public gmf_all_gmfgraph_Polyline(
        ArrayList<Point> points    ) {
        this.points = points;
    }


    public List<Point> getPoints() {
        return points;
    }

    public void addPoint(Point point) {
        this.points.add(point);
    }

}