





import java.util.List;
import java.util.ArrayList;

public class model_ZentaDiagramModel extends DiagramModel {

    private int viewpoint;



    public model_ZentaDiagramModel(
        int viewpoint    ) {
        super(
        );
        this.viewpoint = viewpoint;
    }


    public int getViewpoint() {
        return viewpoint;
    }

    public void setViewpoint(int viewpoint) {
        this.viewpoint = viewpoint;
    }


}