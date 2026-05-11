





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Polyline extends Widget {






    private List<sofiagraphics_Point> sofiagraphics_points;


    public sofiagraphics_Polyline(
    ) {
        super(
        );
        this.sofiagraphics_points = new ArrayList<>();
    }

    public sofiagraphics_Polyline(
        ArrayList<sofiagraphics_Point> sofiagraphics_points    ) {
        this.sofiagraphics_points = sofiagraphics_points;
    }


    public List<sofiagraphics_Point> getSofiagraphics_points() {
        return sofiagraphics_points;
    }

    public void addSofiagraphics_point(Sofiagraphics_point sofiagraphics_point) {
        this.sofiagraphics_points.add(sofiagraphics_point);
    }

}