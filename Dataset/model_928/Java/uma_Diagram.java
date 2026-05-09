





import java.util.List;
import java.util.ArrayList;

public class uma_Diagram extends GraphNode {

    private String zoom;





    private uma_ProcessPackage uma_processpackage;




    private uma_Point uma_point;


    public uma_Diagram(
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

    public uma_ProcessPackage getUma_processpackage() {
        return uma_processpackage;
    }

    public void setUma_processpackage(uma_ProcessPackage uma_processpackage) {
        this.uma_processpackage = uma_processpackage;
    }
    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}