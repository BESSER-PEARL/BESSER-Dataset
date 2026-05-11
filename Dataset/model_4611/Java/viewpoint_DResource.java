





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DResource  {

    private String path;
    private String name;





    private viewpoint_DResourceContainer viewpoint_dresourcecontainer;


    public viewpoint_DResource(
        String path,        String name    ) {
        this.path = path;
        this.name = name;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public viewpoint_DResourceContainer getViewpoint_dresourcecontainer() {
        return viewpoint_dresourcecontainer;
    }

    public void setViewpoint_dresourcecontainer(viewpoint_DResourceContainer viewpoint_dresourcecontainer) {
        this.viewpoint_dresourcecontainer = viewpoint_dresourcecontainer;
    }

}