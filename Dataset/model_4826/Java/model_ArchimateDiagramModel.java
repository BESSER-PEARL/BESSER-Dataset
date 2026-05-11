





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateDiagramModel extends DiagramModel {

    private String viewpoint;



    public model_ArchimateDiagramModel(
        String viewpoint    ) {
        super(
        );
        this.viewpoint = viewpoint;
    }


    public String getViewpoint() {
        return viewpoint;
    }

    public void setViewpoint(String viewpoint) {
        this.viewpoint = viewpoint;
    }


}