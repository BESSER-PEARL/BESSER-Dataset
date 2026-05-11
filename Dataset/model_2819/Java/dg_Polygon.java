





import java.util.List;
import java.util.ArrayList;

public class dg_Polygon extends MarkedElement {






    private List<dg_Point> dg_points;


    public dg_Polygon(
    ) {
        super(
        );
        this.dg_points = new ArrayList<>();
    }

    public dg_Polygon(
        ArrayList<dg_Point> dg_points    ) {
        this.dg_points = dg_points;
    }


    public List<dg_Point> getDg_points() {
        return dg_points;
    }

    public void addDg_point(Dg_point dg_point) {
        this.dg_points.add(dg_point);
    }

}