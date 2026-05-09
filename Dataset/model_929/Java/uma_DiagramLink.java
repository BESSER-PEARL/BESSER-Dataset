





import java.util.List;
import java.util.ArrayList;

public class uma_DiagramLink extends DiagramElement {

    private String zoom;





    private uma_Point uma_point;


    public uma_DiagramLink(
        String zoom    ) {
        super(
        );
        this.zoom = zoom;
    }


    public String getZoom() {
        return zoom;
    }

    public void setZoom(String zoom) {
        this.zoom = zoom;
    }

    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}