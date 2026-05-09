





import java.util.List;
import java.util.ArrayList;

public class uma_GraphEdge extends GraphElement {






    private List<uma_Point> uma_points;


    public uma_GraphEdge(
    ) {
        super(
        );
        this.uma_points = new ArrayList<>();
    }

    public uma_GraphEdge(
        ArrayList<uma_Point> uma_points    ) {
        this.uma_points = uma_points;
    }


    public List<uma_Point> getUma_points() {
        return uma_points;
    }

    public void addUma_point(Uma_point uma_point) {
        this.uma_points.add(uma_point);
    }

}