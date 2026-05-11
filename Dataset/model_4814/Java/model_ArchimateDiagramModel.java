





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateDiagramModel extends DiagramModel {

    private int viewpoint;



    public model_ArchimateDiagramModel(
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