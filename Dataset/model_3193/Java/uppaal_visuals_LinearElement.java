





import java.util.List;
import java.util.ArrayList;

public class uppaal_visuals_LinearElement  {






    private List<Point> points;


    public uppaal_visuals_LinearElement(
    ) {
        this.points = new ArrayList<>();
    }

    public uppaal_visuals_LinearElement(
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