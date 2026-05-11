





import java.util.List;
import java.util.ArrayList;

public class di_Edge extends DiagramElement {






    private List<di_Point> di_points;


    public di_Edge(
    ) {
        super(
        );
        this.di_points = new ArrayList<>();
    }

    public di_Edge(
        ArrayList<di_Point> di_points    ) {
        this.di_points = di_points;
    }


    public List<di_Point> getDi_points() {
        return di_points;
    }

    public void addDi_point(Di_point di_point) {
        this.di_points.add(di_point);
    }

}