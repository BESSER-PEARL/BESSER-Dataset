





import java.util.List;
import java.util.ArrayList;

public class uma_Polyline extends GraphicPrimitive {

    private String closed;





    private List<uma_Point> uma_points;


    public uma_Polyline(
        String closed    ) {
        super(
        );
        this.closed = closed;
        this.uma_points = new ArrayList<>();
    }

    public uma_Polyline(
        String closed        ArrayList<uma_Point> uma_points    ) {
        this.closed = closed;
        this.uma_points = uma_points;
    }

    public String getClosed() {
        return closed;
    }

    public void setClosed(String closed) {
        this.closed = closed;
    }

    public List<uma_Point> getUma_points() {
        return uma_points;
    }

    public void addUma_point(Uma_point uma_point) {
        this.uma_points.add(uma_point);
    }

}