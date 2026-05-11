





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_Polyline extends GraphicsAlgorithm {






    private List<styles_Point> styles_points;


    public mm_algorithms_Polyline(
    ) {
        super(
        );
        this.styles_points = new ArrayList<>();
    }

    public mm_algorithms_Polyline(
        ArrayList<styles_Point> styles_points    ) {
        this.styles_points = styles_points;
    }


    public List<styles_Point> getStyles_points() {
        return styles_points;
    }

    public void addStyles_point(Styles_point styles_point) {
        this.styles_points.add(styles_point);
    }

}