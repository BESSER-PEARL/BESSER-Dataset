





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DResourceContainer extends DResource {






    private List<viewpoint_DResource> viewpoint_dresources;


    public viewpoint_DResourceContainer(
    ) {
        super(
        );
        this.viewpoint_dresources = new ArrayList<>();
    }

    public viewpoint_DResourceContainer(
        ArrayList<viewpoint_DResource> viewpoint_dresources    ) {
        this.viewpoint_dresources = viewpoint_dresources;
    }


    public List<viewpoint_DResource> getViewpoint_dresources() {
        return viewpoint_dresources;
    }

    public void addViewpoint_dresource(Viewpoint_dresource viewpoint_dresource) {
        this.viewpoint_dresources.add(viewpoint_dresource);
    }

}